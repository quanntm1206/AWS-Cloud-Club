from pathlib import Path
from zipfile import ZipFile

from docx import Document
from docx.oxml.ns import qn

from scripts.build_docx import build


def _extract_text(document: Document) -> str:
    return "\n".join(node.text or "" for node in document.element.iter(qn("w:t")))


def test_docx_contains_all_weeks_and_safety_language(tmp_path: Path) -> None:
    output = tmp_path / "roadmap.docx"
    build(output)
    document = Document(output)
    text = _extract_text(document)
    for week in range(1, 25):
        assert f"Tuần {week:02d}" in text
    assert "Budget không phải hard cap" in text or "Budgets chỉ cảnh báo" in text
    assert "Residual scan" in text or "residual scan" in text
    assert "Capstone A" in text and "Capstone B" in text
    assert "Mở tài liệu AWS Free Tier" in text
    assert "Thực hành:" in text and "Kết quả hướng tới:" in text
    assert "Mốc năng lực" in text
    assert text.count("Minh chứng đạt mốc") == 6
    assert "Tổng kết năng lực" in text
    assert "GitHub chỉ dùng để clone/download repo mẫu do chủ repo phát hành" in text
    assert text.count("GitHub") == 1
    assert "Nộp GitHub" not in text
    assert "Portfolio GitHub" not in text
    assert "Lab, checkpoint và rubric" not in text
    assert "checkpoint-01" not in text
    assert "Checkpoint/resume" in text
    assert "Checkpoint gồm model, optimizer" in text
    assert "AcknowledgeBudgetConfigured" in text
    assert "CloudFormation/S3/Lambda/Logs/IAM/API Gateway" in text
    assert document.core_properties.title == "Machine Learning Engineer Roadmap - AWS Cloud Club"
    assert document.core_properties.author == "AWS Cloud Club"
    assert "local-first" in document.core_properties.subject
    with ZipFile(output) as archive:
        settings = archive.read("word/settings.xml").decode("utf-8")
        relationships = archive.read("word/_rels/document.xml.rels").decode("utf-8")
    assert "vi-VN" in settings
    assert relationships.count("relationships/hyperlink") >= 9
    assert "https://aws.amazon.com/free/" in relationships
