# Week 22 - Upload model to Lambda, keep everything private

## Weekly goals

Deploy small serverless inference, call privately, read logs and clean up in the same session.

## Why this week matters

Training model is only the first half of the job. When the model runs behind a service boundary, wrong input, artifact
Errors and sensitive logs all become engineering problems. Private invoke allows you to learn this part correctly without
need to open the endpoint to the Internet.

## Core knowledge

- Lambda handler has a clear contract; error JSON/type returned response intentionally.
- Artifact portable resides in S3; checksum and schema are checked before scoring.
- Memory 512 MB, timeout 15 seconds, reserved concurrency 1 helps narrow blast radius, but not
  hard spending cap.
- CloudWatch log does not contain raw payload/secret and has one day retention.
- Tag `ExpiresAt` is only metadata that prompts cleanup, does not clear the stack itself.

## Keywords for this week

**New or focus terms:** `Lambda`, `CloudWatch Logs`, `API contract`

**Review:** `IAM`, `S3`, `budget alert`

**Use:** Use `Lambda` to perform inference according to `API contract`, check `CloudWatch Logs` does not reveal sensitive samples; review IAM and S3 from last week.

## 8-10 hour schedule

| Activities | Hours |
|---|---:|
| Read handler, template and policy | 2 |
| Test local handler with true/false input | 2 |
| Deploy, private invoke, see log | 3 |
| Cleanup and residual scan | 1 |
| Learning log and self-assessment | 1 |

## Guided practice

1. Call local handler with valid JSON, malformed JSON, missing fields and wrong type.
2. Open a separate terminal, set the cleanup timer; Run cost check and preflight before deploying.
3. Deploy stack, invoke Lambda using AWS CLI at most a few times, read log.
4. Clean up now; scan must fail-closed if AWS CLI fails or lacks permissions.

## Lab

**lab-20:** S3 + private Lambda invoke + Logs + cleanup. Do not create API Gateway or public URL.

## Test yourself

1. What risks/components does Private Invoke eliminate?
2. Why is concurrency 1 not a limit on total costs?
3. How does `ExpiresAt` differ from automatic TTL?

## Result oriented

A small but complete inference lifecycle: artifact has checksum, contract runs correctly, clean log, residual
Scan cleanly and have a schedule to check Billing again.

## Signs that you understand

Can you explain why private invoke still needs contracts, logs, runtime limits and cleanup.

## Core vs stretch

- **Core:** private invoke valid/invalid then cleanup.
- **Stretch:** explains on paper how API Gateway adds attack surface and request cost; not deployed.

## Common errors

- Close the terminal after deploying and forget about cleanup.
- Think expired tags will automatically delete resources.
- Saw residual scan error but still concluded "zero residual".

## When you get stuck

If any command fails after deploy starts, stop and run cleanup dry-run immediately. Read exact names, run
execute, then residual scan. If the scan is not completed, check the Console or ask your account administrator; Don't guess.

## Are you ready to move weeks when

- Private Lambda returns the correct contract for both valid and invalid requests.
- Log has no credential or raw record.
- Stack, bucket, function, log group and role are no longer there after cleanup.

## AWS cost gate

Required lifecycle: `Pre-check -> Estimate -> Dry-run -> Deploy -> Verify -> Cleanup -> Residual scan -> Cost audit`.
Budget may be late; Planning envelope is not bill guarantee.

## Source

[Lambda pricing](https://aws.amazon.com/lambda/pricing/),
[S3 pricing](https://aws.amazon.com/s3/pricing/) and `docs/sources.yml`.
