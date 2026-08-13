# Spiral ML Vocabulary Design

## Mục tiêu

Giúp người đã biết lập trình nhưng mới học ML hiểu thuật ngữ đúng lúc, dùng lại nhiều lần và không chỉ học thuộc glossary.

## Cấu trúc dữ liệu

Mỗi mục trong `curriculum/glossary.yml` có `term`, `meaning`, `example`, `introduced_in`. `introduced_in` là lab 00-20 nơi thuật ngữ xuất hiện lần đầu.

## Hợp đồng cho lab

Mỗi README lab có `## Thuật ngữ trong lab` gồm bốn dòng: `Thuật ngữ mới`, `Ôn lại`, `Áp dụng trong lab`, `Tự giải thích`. Lab 00 không có từ cũ; lab 01-20 phải dùng lại ít nhất hai thuật ngữ đã giới thiệu. Tất cả từ mới phải xuất hiện trong thao tác áp dụng; mọi từ ôn lại phải có mặt trong phần áp dụng hoặc câu tự giải thích. `expected/README.md` nhắc learner dùng thuật ngữ để giải thích evidence.

## Roadmap và DOCX

Tuần tương ứng có `## Từ khóa tuần này`, lấy từ lab chính của tuần. Tuần 22-24 dùng lại lab 20 nhưng tập trung các cụm AWS khác nhau. DOCX render phần từ khóa từng tuần và bảng glossary gồm nghĩa, ví dụ, lab giới thiệu.

## Kiểm định

`validate_learner_docs.py` kiểm schema, uniqueness, đủ 50+ mục, đúng tiến trình, headings, từ mới/ôn lại có sử dụng thật, expected receipt và không dùng từ tương lai. Test curriculum khóa ba nghĩa dễ nhầm: data validation, validation set, model validation.
