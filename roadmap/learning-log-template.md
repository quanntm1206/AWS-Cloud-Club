# Study diary - NN Week

This journal is for you, not a submission. Write short but specific: a command or a real observation
more useful than saying “I understood the lesson”.

## Blank template

- **Weekly goal:** What do I want to explain or do on my own?
- **What was run:** What command, notebook, config and environment?
- **Evidence:** What metrics, tests, graphs, or tests support the conclusion?
- **A memorable error:** Symptoms, causes, how I checked and fixed.
- **Uncertainties:** Which questions still need to come back?
- **Technical decision:** Which practice do I keep or type? Why?
- **Next small step:** First thing next week, specific enough to do in 30 minutes.

## Short example - Week 07

- **Weekly goal:** Choose the threshold according to the cost of missing churn, do not choose the highest F1 mechanically.
- **What ran:** `python scripts/run_lab.py --lab 6`, seed 42, local CPU.
- **Evidence:** Threshold 0.35 increases recall from 0.68 to 0.81; precision decreased from 0.74 to 0.61.
- **One memorable mistake:** I initially chose threshold on test. I found that the test metric changes after each test;
  Fix it by selecting on validation and then only evaluate the test once.
- **Uncertainty:** When false positive costs vary by customer group, is a common threshold still reasonable?
- **Technical decision:** Keep threshold 0.35 for current cost assumptions; Clearly state assumptions in the report.
- **Next small step:** Draw the confusion matrix according to the two tenure groups in the next run.