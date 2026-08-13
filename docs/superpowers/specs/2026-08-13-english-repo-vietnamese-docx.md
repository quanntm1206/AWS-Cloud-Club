# English Repository, Vietnamese DOCX

## Decision

The learner-facing GitHub repository uses clear B2 English, roughly IELTS 6.5. The downloadable DOCX remains Vietnamese and continues to target Vietnamese learners.

The two outputs have separate prose sources:

- GitHub source: `README.md`, `roadmap/`, `labs/`, `notebooks/`, `capstones/`, `aws/`, `docs/source-notes/`, and `curriculum/`.
- Vietnamese DOCX source: `docs/docx-vi/roadmap/weeks/` and `docs/docx-vi/curriculum/`.
- Shared machine-readable sources that do not contain learner prose may remain shared.
- `scripts/build_docx.py` must never read translated learner prose when it builds the Vietnamese document.

## Language Standard

English learner prose should use short or medium sentences, familiar verbs, concrete examples, and limited idioms. It should sound like a patient mentor, not a literal translation or a compliance checklist.

Keep technical tokens unchanged when translation would reduce precision. This includes commands, paths, code identifiers, AWS service names, and established ML terms such as `dataset`, `validation set`, `augmentation`, and `fine-tuning`. Explain those terms in simple English when they first appear, then reuse them in later labs.

Vietnamese DOCX prose stays natural, beginner-friendly Vietnamese. Its OOXML language remains `vi-VN`.

## Learning Contract

The language change must not alter the curriculum:

- 24 weeks at 8-10 hours per week.
- Local-first work; Colab Free and Kaggle Free for heavier training.
- AWS is optional and limited to the cost-safe capstone path.
- No heavy AWS training.
- GitHub is only the source repository learners clone or download. Learners do not need to fork, commit, push, open a pull request, or submit work.
- Every lab introduces new terms, reviews earlier terms, applies them, and asks the learner to explain them.
- All AWS budget, cleanup, residual-scan, private-Lambda, and no-API-Gateway guardrails remain mandatory.

## Source Separation

Before translating the repository, copy the current Vietnamese inputs used by the builder:

- `curriculum/curriculum.yml`
- `curriculum/assessment.yml`
- `curriculum/glossary.yml`
- `roadmap/weeks/week-01.md` through `week-24.md`

The builder then reads the copies under `docs/docx-vi/`. Lab paths and command strings may still be discovered from the repository because they are language-neutral identifiers.

Automated checks must prove both sides of the contract:

- English headings and vocabulary fields exist in learner-facing GitHub files.
- Common Vietnamese instructional headings are absent from that learner-facing scope.
- The Vietnamese source tree contains the expected Vietnamese headings and glossary prose.
- The English and Vietnamese curricula retain the same week IDs, lab IDs, term names, introduction labs, and spiral review order.
- A rebuilt DOCX contains Vietnamese markers and `vi-VN`.

## Verification

Run focused tests while translating. Finish with the release profile, a clean diff check, a complete DOCX rebuild, full-page rendering, visual inspection, and accessibility inspection. An independent `gpt-5.6-sol` subagent at `xhigh` reasoning reviews knowledge quality, language, completeness, cost safety, and generated artifacts. Fix findings and repeat until the auditor returns exactly `SATISFACTORY`.
