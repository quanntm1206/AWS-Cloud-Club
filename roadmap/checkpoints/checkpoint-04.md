# Competency milestone 04 - Week 16

## Target

Evaluate your ability to turn a notebook into testable and operational ML software.

## You have reached the if mark

- Training/evaluation is separated from the notebook into modules, config and CLI running from a clean environment.
- Test covers schema, transform, model artifact and valid/invalid boundary of inference API.
- Artifact attaches model version, checksum, config, metrics and source run.
- CI runs lint/test on mini profile; Docker is only an extension if the machine does not support it.

## Proof of reaching the milestone

- Package tree, quickstart and command train/evaluate/serve are saved locally.
- Test report has at least one negative case for the schema or API contract.
- Artifact manifest and parity check between batch path and inference.
- CI log or local CI-equivalent; Specify environment/Docker limits if not running yet.

## Rubric

| Criteria | Score |
|---|---:|
| Package structure and CLI | 25 |
| Test and contract inference | 30 |
| CI and artifact versioning | 25 |
| Operation and limitations | 20 |

Passing score: 70/100. Gate: no secret, mini run re-established, malformed input returns errors with contract instead of crashing the process.

## Self-reflection question

- What does someone else need to know at least to run the artifact again?
- Which test protects the most dangerous boundaries of the system?
- What responsibilities do notebooks still hold that should be moved to the package?