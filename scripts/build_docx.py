from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
BLUE = "2E74B5"
DARK_BLUE = "1F4D78"
TABLE_FILL = "E8EEF5"
WARNING_FILL = "FFF2CC"
WARNING_BORDER = "C65911"


def set_cell_shading(cell: object, fill: str) -> None:
    properties = cell._tc.get_or_add_tcPr()  # type: ignore[attr-defined]
    shading = properties.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        properties.append(shading)
    shading.set(qn("w:fill"), fill)


def set_cell_margins(cell: object, top: int = 80, start: int = 120, bottom: int = 80, end: int = 120) -> None:
    properties = cell._tc.get_or_add_tcPr()  # type: ignore[attr-defined]
    margins = properties.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        properties.append(margins)
    for edge, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        element = margins.find(qn(f"w:{edge}"))
        if element is None:
            element = OxmlElement(f"w:{edge}")
            margins.append(element)
        element.set(qn("w:w"), str(value))
        element.set(qn("w:type"), "dxa")


def set_table_geometry(table: object, widths: list[float]) -> None:
    table.alignment = WD_TABLE_ALIGNMENT.LEFT  # type: ignore[attr-defined]
    table.autofit = False  # type: ignore[attr-defined]
    properties = table._tbl.tblPr  # type: ignore[attr-defined]
    width = properties.first_child_found_in("w:tblW")
    width.set(qn("w:w"), "9360")
    width.set(qn("w:type"), "dxa")
    indent = properties.first_child_found_in("w:tblInd")
    if indent is None:
        indent = OxmlElement("w:tblInd")
        properties.append(indent)
    indent.set(qn("w:w"), "120")
    indent.set(qn("w:type"), "dxa")
    grid = table._tbl.tblGrid  # type: ignore[attr-defined]
    for child in list(grid):
        grid.remove(child)
    for inches in widths:
        column = OxmlElement("w:gridCol")
        column.set(qn("w:w"), str(round(inches * 1440)))
        grid.append(column)
    for row in table.rows:  # type: ignore[attr-defined]
        row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        for index, cell in enumerate(row.cells):
            cell.width = Inches(widths[index])
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_margins(cell)
            cell_properties = cell._tc.get_or_add_tcPr()
            cell_width = cell_properties.first_child_found_in("w:tcW")
            cell_width.set(qn("w:w"), str(round(widths[index] * 1440)))
            cell_width.set(qn("w:type"), "dxa")


def add_table(document: Document, headers: list[str], rows: list[list[str]], widths: list[float]) -> object:
    table = document.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    header = table.rows[0]
    header._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    for index, text in enumerate(headers):
        set_cell_shading(header.cells[index], TABLE_FILL)
        paragraph = header.cells[index].paragraphs[0]
        run = paragraph.add_run(text)
        run.bold = True
    for values in rows:
        cells = table.add_row().cells
        for index, text in enumerate(values):
            cells[index].text = text
    set_table_geometry(table, widths)
    document.add_paragraph("")
    return table


def add_warning(document: Document, title: str, body: str) -> None:
    table = document.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.cell(0, 0)
    table.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    set_cell_shading(cell, WARNING_FILL)
    properties = cell._tc.get_or_add_tcPr()
    borders = properties.first_child_found_in("w:tcBorders")
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        properties.append(borders)
    for edge in ("top", "left", "bottom", "right"):
        border = OxmlElement(f"w:{edge}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), "12")
        border.set(qn("w:color"), WARNING_BORDER)
        borders.append(border)
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run(f"CẢNH BÁO CHI PHÍ - {title}\n")
    run.bold = True
    run.font.color.rgb = RGBColor.from_string(WARNING_BORDER)
    paragraph.add_run(body)
    set_table_geometry(table, [6.5])
    document.add_paragraph("")


def configure_styles(document: Document) -> None:
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = section.bottom_margin = Inches(1)
    section.left_margin = section.right_margin = Inches(1)
    section.header_distance = section.footer_distance = Inches(0.492)
    normal = document.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25
    for name, size, color, before, after in (
        ("Title", 24, DARK_BLUE, 0, 12),
        ("Heading 1", 16, BLUE, 18, 10),
        ("Heading 2", 13, BLUE, 14, 7),
        ("Heading 3", 12, DARK_BLUE, 10, 5),
    ):
        style = document.styles[name]
        style.font.name = "Calibri"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor.from_string(color)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True
    if "Cost Warning" not in document.styles:
        warning = document.styles.add_style("Cost Warning", WD_STYLE_TYPE.PARAGRAPH)
        warning.font.name = "Calibri"
        warning.font.size = Pt(11)
        warning.font.color.rgb = RGBColor.from_string(WARNING_BORDER)
        warning.font.bold = True
    for section in document.sections:
        header = section.header.paragraphs[0]
        header.text = "AWS Cloud Club | Machine Learning Engineer Roadmap"
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        header.runs[0].font.size = Pt(8)
        header.runs[0].font.color.rgb = RGBColor(100, 100, 100)
        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer.add_run("AWS Cloud Club  |  Tài liệu học tập - kiểm tra nguồn trước mỗi cohort")
        footer.runs[0].font.size = Pt(8)


def add_bullets(document: Document, items: list[str]) -> None:
    for item in items:
        paragraph = document.add_paragraph(style="List Bullet")
        paragraph.add_run(item)
        paragraph.paragraph_format.left_indent = Inches(0.375)
        paragraph.paragraph_format.first_line_indent = Inches(-0.188)
        paragraph.paragraph_format.space_after = Pt(4)
        paragraph.paragraph_format.line_spacing = 1.25


def add_hyperlink(paragraph: object, label: str, url: str) -> None:
    relationship_id = paragraph.part.relate_to(  # type: ignore[attr-defined]
        url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), relationship_id)
    run = OxmlElement("w:r")
    properties = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), BLUE)
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    properties.extend([color, underline])
    text = OxmlElement("w:t")
    text.text = label
    run.extend([properties, text])
    hyperlink.append(run)
    paragraph._p.append(hyperlink)  # type: ignore[attr-defined]


def build(output: Path) -> None:
    curriculum = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    assessments = yaml.safe_load((ROOT / "curriculum/assessment.yml").read_text(encoding="utf-8"))
    sources = yaml.safe_load((ROOT / "docs/sources.yml").read_text(encoding="utf-8"))["sources"]
    document = Document()
    document.core_properties.title = "Machine Learning Engineer Roadmap - AWS Cloud Club"
    document.core_properties.subject = "Roadmap 24 tuần, local-first, free-compute-first và AWS cost-safe"
    document.core_properties.author = "AWS Cloud Club"
    document.core_properties.keywords = "Machine Learning, MLOps, AWS, Colab, Kaggle, roadmap"
    language = OxmlElement("w:themeFontLang")
    language.set(qn("w:val"), "vi-VN")
    document.settings.element.append(language)
    configure_styles(document)
    document.add_heading("Machine Learning Engineer Roadmap", 0)
    subtitle = document.add_paragraph("AWS CLOUD CLUB  |  24 TUẦN  |  8-10 GIỜ/TUẦN")
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].bold = True
    document.add_paragraph("Từ nền tảng Machine Learning đến ML Engineering và AWS capstone tối ưu chi phí.")
    add_warning(
        document,
        "ĐỌC TRƯỚC KHI DÙNG AWS",
        "Core path không dùng GPU, NAT Gateway, EC2 hay SageMaker runtime. AWS Budgets chỉ cảnh báo, "
        "không phải hard cap; billing có thể trễ. Luôn cleanup và residual scan trong cùng phiên lab.",
    )
    add_table(
        document,
        ["Thông tin", "Giá trị"],
        [
            ["Đối tượng", "Đã biết lập trình, chưa học Machine Learning"],
            ["Hình thức", "Tự học cá nhân trong AWS Cloud Club"],
            ["Training", "Local CPU; chọn Colab Free hoặc Kaggle Free cho CV"],
            ["Capstone", "Tabular AWS bắt buộc; CV transfer learning mở rộng"],
            ["Ngày kiểm nguồn volatile", "12/08/2026; kiểm lại trước mỗi cohort"],
        ],
        [1.875, 4.625],
    )
    document.add_page_break()
    document.add_heading("Mục lục", level=1)
    for item in (
        "1. Cách dùng và chuẩn đầu ra",
        "2. Roadmap 24 tuần",
        "3. Colab Free và Kaggle Free",
        "4. AWS cost-safe capstone",
        "5. Lab, mốc năng lực và rubric",
        "6. Tổng kết năng lực",
        "7. Glossary và nguồn",
    ):
        document.add_paragraph(item)
    document.add_heading("1. Cách dùng và chuẩn đầu ra", level=1)
    document.add_paragraph(
        "GitHub chỉ dùng để clone/download repo mẫu do chủ repo phát hành. Kết quả học tập và minh chứng "
        "được lưu cục bộ để người học tự đánh giá."
    )
    add_bullets(
        document,
        [
            "Mỗi tuần: 2 giờ lý thuyết, 2 giờ guided practice, 3-4 giờ lab, 1 giờ assessment, 1 giờ learning log.",
            "Core hoàn thành trước Stretch; không sweep và không mua compute để pass.",
            "Mọi experiment ghi question, baseline, split, seed, metric, runtime, artifact và limitation.",
            "Mốc năng lực dùng sản phẩm chạy được để tự đánh giá; accuracy đơn lẻ không đủ.",
        ],
    )
    document.add_heading("Chuẩn đầu ra sau 24 tuần", level=2)
    add_bullets(
        document,
        [
            "Xây pipeline tabular chống leakage và đánh giá theo constraint.",
            "Xây CV transfer-learning baseline với CPU fallback và failure analysis.",
            "Đóng gói, test, phục vụ inference và quản lý artifact.",
            "Triển khai Lambda private invoke, quan sát log, cleanup và cost audit trên AWS.",
            "Trình bày hai bộ tổng kết năng lực có model card và reproduction guide.",
        ],
    )
    document.add_heading("2. Roadmap 24 tuần", level=1)
    phase_rows: list[list[str]] = []
    for phase, label in (
        ("foundation", "Nền tảng dữ liệu và toán"),
        ("classical-ml", "ML cổ điển"),
        ("applied-ml", "ML thực hành"),
        ("engineering", "Engineering"),
        ("deep-learning", "Deep Learning và CV"),
        ("aws-capstone", "AWS capstone"),
    ):
        phase_weeks = [str(week["id"]) for week in curriculum["weeks"] if week["phase"] == phase]
        phase_rows.append([label, f"{phase_weeks[0]}-{phase_weeks[-1]}", "Xem mục tiêu và kết quả từng tuần"])
    add_table(document, ["Giai đoạn", "Tuần", "Đầu ra"], phase_rows, [2.5, 0.75, 3.25])
    for week in curriculum["weeks"]:
        document.add_heading(f"Tuần {week['id']:02d} - {week['title']}", level=2)
        environment = ", ".join(week["environments"])
        add_table(
            document,
            ["Mục", "Chi tiết"],
            [
                ["Môi trường", environment],
                ["Workload", f"{week['hours']} giờ; core trước stretch"],
                ["Lab", week["lab"]],
                ["Mốc năng lực", week["milestone"] or "Không"],
                ["Cost class", week["cost_class"]],
            ],
            [1.181, 5.319],
        )
        week_doc = (ROOT / f"roadmap/weeks/week-{week['id']:02d}.md").read_text(encoding="utf-8")
        goal = week_doc.split("## Mục tiêu tuần", 1)[1].split("##", 1)[0].strip()
        document.add_paragraph(goal)
        core = week_doc.split("## Kiến thức cốt lõi", 1)[1].split("##", 1)[0].strip()
        document.add_heading("Kiến thức cốt lõi", level=3)
        add_bullets(
            document,
            [line[2:].strip().replace("`", "") for line in core.splitlines() if line.startswith("- ")],
        )
        guided = week_doc.split("## Guided practice", 1)[1].split("##", 1)[0].strip()
        document.add_heading("Guided practice", level=3)
        add_bullets(
            document,
            [line.split(". ", 1)[1] for line in guided.splitlines() if ". " in line],
        )
        lab_section = week_doc.split("## Lab", 1)[1].split("##", 1)[0].strip()
        paragraph = document.add_paragraph()
        paragraph.add_run("Thực hành: ").bold = True
        paragraph.add_run(lab_section.replace("**", ""))
        outcome = week_doc.split("## Kết quả hướng tới", 1)[1].split("##", 1)[0].strip()
        paragraph = document.add_paragraph()
        paragraph.add_run("Kết quả hướng tới: ").bold = True
        paragraph.add_run(outcome)
        self_check = week_doc.split("## Tự kiểm tra", 1)[1].split("##", 1)[0].strip()
        document.add_heading("Tự kiểm tra", level=3)
        add_bullets(
            document,
            [line.split(". ", 1)[1] for line in self_check.splitlines() if ". " in line],
        )
        mistakes = week_doc.split("## Lỗi thường gặp", 1)[1].split("##", 1)[0].strip()
        paragraph = document.add_paragraph()
        paragraph.add_run("Lỗi thường gặp: ").bold = True
        paragraph.add_run("; ".join(line[2:].strip() for line in mistakes.splitlines() if line.startswith("- ")))
        if week["id"] >= 21:
            add_warning(
                document,
                f"TUẦN {week['id']}",
                "Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit. "
                "Không đánh dấu hoàn thành nếu còn resource.",
            )
    document.add_heading("3. Colab Free và Kaggle Free", level=1)
    document.add_paragraph(
        "Người học chọn một nền tảng. Resource miễn phí không được bảo đảm; accelerator, quota và runtime "
        "có thể thay đổi. Notebook tự phát hiện CUDA, dùng cpu-mini nếu GPU không có."
    )
    add_table(
        document,
        ["Bước", "Colab Free", "Kaggle Free"],
        [
            ["Mở", "Upload từ repo mẫu đã clone; Copy to Drive", "Import/Upload notebook"],
            ["Dữ liệu", "Download nhỏ hoặc Drive optional", "Add Dataset; không dùng private token trong cell"],
            ["Compute", "GPU chỉ khi dùng; cpu-mini fallback", "Accelerator nếu có; cpu-mini fallback"],
            ["Training", "Frozen backbone; 3-5 epoch max", "Frozen backbone; 3-5 epoch max"],
            ["Export", "Download artifacts.zip", "Save Version rồi download output"],
            ["Kết thúc", "Disconnect and delete runtime", "Tắt accelerator/session"],
        ],
        [1.1, 2.7, 2.7],
    )
    document.add_heading("Notebook contract", level=2)
    add_bullets(
        document,
        [
            "Environment check; dependency verification; configuration và seed.",
            "Data acquisition có mini fallback; validation trước model.",
            "Baseline; training; evaluation và error analysis.",
            "Artifact manifest, checkpoint export và release runtime.",
        ],
    )
    document.add_heading("4. AWS cost-safe capstone", level=1)
    add_warning(
        document,
        "HARD GUARDRAILS",
        "Core chỉ IAM, S3, Lambda, CloudWatch Logs và Budgets. HTTP API optional, tắt mặc định. "
        "Cấm GPU, EC2, NAT Gateway, SageMaker notebook/training/endpoint và resource chạy nền ngoài allowlist.",
    )
    add_table(
        document,
        ["Control", "Giới hạn"],
        [
            ["Region", "us-east-1 mặc định"],
            ["Tags", "Project, Owner, Environment=learning, ExpiresAt"],
            ["Artifact", "Mục tiêu <50 MB; hard limit 200 MB"],
            ["Lambda", "512 MB; 15 giây; reserved concurrency 1"],
            ["Logs", "Retention một ngày"],
            ["S3", "Public block + encryption + lifecycle bảy ngày"],
            ["Cleanup", "Dry-run mặc định; exact project ID; CloudFormation delete; residual scan"],
        ],
        [1.875, 4.625],
    )
    document.add_heading("AWS lab - lệnh thực thi", level=2)
    document.add_paragraph(
        "1) Tạo actual + forecast Budget alerts trên Billing console. 2) Chạy preflight với "
        "AcknowledgeBudgetConfigured. 3) Deploy private Lambda bằng portable_model.json. "
        "4) Invoke valid/invalid events. 5) Kiểm logs. 6) Cleanup dry-run rồi execute. "
        "7) Residual scan CloudFormation/S3/Lambda/Logs/IAM/API Gateway và audit Billing."
    )
    add_warning(
        document,
        "STOP CONDITIONS",
        "Dừng khi sai account/Region, chưa có Budget alerts, artifact quá 200 MB, template có forbidden "
        "resource hoặc cleanup target không khớp exact project ID.",
    )
    document.add_heading("Capstone A - Tabular classification", level=2)
    add_bullets(
        document,
        [
            "Train local CPU; export sklearn artifact và portable logistic JSON.",
            "Upload portable_model.json lên S3; Lambda chỉ dùng Python stdlib + boto3.",
            "Private invoke là core; public HTTP API chỉ optional trong một phiên lab.",
            "Cleanup và residual scan là gate bắt buộc.",
        ],
    )
    document.add_heading("Capstone B - Image classification", level=2)
    add_bullets(
        document,
        [
            "Train trên một trong Colab/Kaggle; frozen backbone baseline; optional unfreeze block cuối; "
            "CPU mini fallback.",
            "Pretrained normalization phải lấy từ ResNet18 weights; FakeData/random weights chỉ là execution smoke.",
            "Checkpoint gồm model, optimizer, epoch, best metric, history, config, seed và class mapping; "
            "có resume path.",
            "Macro/per-class metric, confusion matrix và tối đa 20 failure cases; nếu ít hơn, "
            "export toàn bộ và ghi limitation.",
            "AWS chỉ artifact checksum/upload optional và architecture ADR; không endpoint CV.",
        ],
    )
    document.add_heading("5. Lab, mốc năng lực và rubric", level=1)
    add_table(
        document,
        ["Nhóm", "Số lượng", "Gate"],
        [
            ["Lab", "20 + setup lab", "Mini path, config, test, failure evidence"],
            ["Mốc năng lực", "6", "70/100; cuối kỳ 75/100"],
            ["Capstone", "2", "Không leakage/secret; AWS cleanup nếu áp dụng"],
        ],
        [1.5, 1.0, 4.0],
    )
    for index, milestone in enumerate(assessments["milestones"], start=1):
        document.add_heading(f"Mốc năng lực {index:02d} - tuần {milestone['week']}", level=2)
        document.add_paragraph(
            f"Trọng tâm: {milestone['focus']}. Điểm đạt: {milestone['pass_score']}/100. "
            "Minh chứng đạt mốc: README, code/notebook, test evidence, metric, learning log và limitations; "
            "lưu cục bộ để tự kiểm tra."
        )
    document.add_heading("6. Tổng kết năng lực", level=1)
    add_bullets(
        document,
        [
            "README có problem, architecture, quickstart, metric, demo, limitations và cost note.",
            "Repository không chứa secret, raw data/model lớn hoặc notebook output dư thừa.",
            "Experiment report ghi baseline, controlled candidates, negative results và reproduction command.",
            "Model card ghi intended use, out-of-scope, subgroup/failure behavior, safety/privacy "
            "và artifact checksum.",
            "AWS evidence gồm preflight, cost manifest, deployment manifest, cleanup và zero-residual report.",
        ],
    )
    document.add_heading("7. Glossary và nguồn", level=1)
    glossary = yaml.safe_load((ROOT / "curriculum/glossary.yml").read_text(encoding="utf-8"))["terms"]
    add_table(document, ["Thuật ngữ", "Nghĩa"], [[item["term"], item["meaning"]] for item in glossary], [1.875, 4.625])
    document.add_heading("Nguồn chính thức", level=2)
    for source in sources:
        paragraph = document.add_paragraph()
        paragraph.add_run(f"{source['title']} ({source['verified_on']}): ").bold = True
        add_hyperlink(paragraph, f"Mở tài liệu {source['title']}", source["url"])
    output.parent.mkdir(parents=True, exist_ok=True)
    document.save(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx")
    args = parser.parse_args()
    build(args.output)
    print(f"DOCX BUILT: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
