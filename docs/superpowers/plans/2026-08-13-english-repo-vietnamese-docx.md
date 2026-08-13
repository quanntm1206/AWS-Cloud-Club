# English Repository, Vietnamese DOCX: Implementation Plan

**Goal:** Publish natural B2 English learner content on GitHub while keeping the generated roadmap DOCX fully Vietnamese and reproducible.

**Architecture:** Freeze the current Vietnamese curriculum prose into a dedicated DOCX source tree. Point the DOCX builder at that tree. Translate the active learner-facing repository and update its validation contract. Add alignment tests so the English and Vietnamese tracks cannot silently drift.

**Quality bar:** No curriculum loss, no weakened AWS guardrail, no new learner GitHub workflow, no translated command or technical identifier, and no future DOCX rebuild that changes the document language.

---

## 1. Lock the bilingual contract with tests

**Files:**
- Modify: `tests/curriculum/test_docx_content.py`
- Modify: `tests/curriculum/test_validate_learner_docs.py`
- Create: `tests/curriculum/test_bilingual_content.py`

Add failing tests that require English learner headings, reject common Vietnamese instructional prose in learner-facing files, require Vietnamese DOCX sources, compare curriculum IDs and spiral vocabulary between both source trees, and verify `vi-VN` plus Vietnamese text in the built document.

Run the focused tests. Confirm failure because the source separation and English headings do not exist yet.

## 2. Separate Vietnamese DOCX inputs

**Files:**
- Create: `docs/docx-vi/curriculum/curriculum.yml`
- Create: `docs/docx-vi/curriculum/assessment.yml`
- Create: `docs/docx-vi/curriculum/glossary.yml`
- Create: `docs/docx-vi/roadmap/weeks/week-01.md` through `week-24.md`
- Modify: `scripts/build_docx.py`

Copy the current Vietnamese sources without rewriting them. Add one explicit DOCX-source constant. Change only prose-input paths in the builder. Keep repository URLs, lab paths, commands, official source metadata, output name, and hardcoded Vietnamese document text unchanged.

Run DOCX-focused tests. Confirm the rebuilt document still contains all 24 Vietnamese weeks, safety language, glossary entries, hyperlinks, and `vi-VN`.

## 3. Translate the curriculum contract

**Files:**
- Modify: `curriculum/curriculum.yml`
- Modify: `curriculum/assessment.yml`
- Modify: `curriculum/glossary.yml`
- Modify: `scripts/validate_learner_docs.py`
- Modify: related curriculum tests

Translate learner-facing values, not schema keys or IDs. Use plain B2 English. Update validator headings and field labels to `Why this week matters`, `Keywords for this week`, `Signs that you understand`, `When you get stuck`, `New terms`, `Review`, `Use in this lab`, and `Explain it yourself`. Keep chronology rules identical.

Run learner-doc and bilingual tests.

## 4. Translate the 24-week roadmap

**Files:**
- Modify: `roadmap/00-getting-started.md`
- Modify: `roadmap/weeks/week-01.md` through `week-24.md`
- Modify: `roadmap/checkpoints/*.md`
- Modify: `roadmap/learning-log-template.md`
- Modify: `roadmap/sau-24-tuan.md`

Translate in four six-week batches. Preserve tables, links, commands, lab paths, time totals, checkpoints as learning outcomes, and spiral vocabulary lists. Run learner-doc and bilingual tests after each batch.

## 5. Translate labs and expected receipts

**Files:**
- Modify: `labs/README.md`
- Modify: `labs/lab-00-*/README.md` through `labs/lab-20-*/README.md`
- Modify: every `labs/lab-*/expected/README.md`

Translate instructions and expected explanations. Keep code, commands, file names, values, metrics, and term names exact. Every lab must still introduce current terms, recall earlier terms, apply both, and include a distinct terminology oracle.

Translate in small batches. Run `scripts/validate_learner_docs.py` plus curriculum tests after each batch.

## 6. Translate compute and capstone guidance

**Files:**
- Modify: `notebooks/README.md`
- Modify: notebook Markdown cells under `notebooks/` and `capstones/cv-image-classification/notebooks/`
- Modify: learner prose under `capstones/`
- Modify: `aws/README.md`
- Modify: learner-facing descriptions in AWS YAML/JSON where applicable
- Modify: `docs/source-notes/*.md`
- Modify: `README.md`

Use natural English. Keep Colab Free and Kaggle Free as the default GPU options. Keep AWS optional, private, short-lived, region-scoped, and cleanup-first. Do not add AWS training. Preserve all budget disclaimers and cleanup commands.

Run notebook validation, AWS safety checks, link checks, learner-doc validation, and curriculum tests.

## 7. Audit language and completeness

Scan only the defined learner-facing scope for Vietnamese instructional phrases. Review every match manually because Vietnamese source files and proper names are allowed outside that scope. Check that no learner is asked to fork, submit, commit, push, or open a pull request. Check that every link and relative path still resolves.

Run formatting, Ruff, mypy, unit tests, validators, and notebook checks. Fix all fallout.

## 8. Rebuild and inspect the Vietnamese DOCX

Build `dist/ML-Roadmap-24-Tuan-AWS-Cloud-Club.docx` with the bundled document runtime. Render every page. Inspect the contact sheet and any suspicious page at full resolution. Run DOCX accessibility checks. Confirm Vietnamese body text, 24 weeks, glossary, safety warnings, navigation, hyperlinks, and `vi-VN`.

## 9. Release verification and independent audit

Run:

```powershell
.\scripts\check.ps1 -Scope all -Profile release
git diff --check
```

Send the complete worktree and generated document to the existing `gpt-5.6-sol` auditor with `xhigh` reasoning. Require review of ML progression, term reuse, B2 English quality, Vietnamese DOCX integrity, Colab/Kaggle free-compute guidance, AWS cost containment, repository completeness, tests, and rendered layout.

For any result other than exact `SATISFACTORY`, record actionable feedback, fix it, rerun focused and release checks, rebuild the DOCX if needed, and request another audit. Repeat until exact `SATISFACTORY`.

## 10. Publish

Review `git status` and the final diff. Commit without amending previous commits. Push `main` to `https://github.com/quanntm1206/AWS-Cloud-Club`. Watch the GitHub Actions run and report its final state.
