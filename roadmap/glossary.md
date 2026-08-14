# Machine Learning Glossary

Beginner-friendly definitions, examples, misconceptions, and review questions, grouped by the lab where each term first appears.

---

**Introduced in Lab 00**

## `dataset`

**Meaning:** A dataset is a collection of samples used for analysis or model training. It usually has rows of samples and columns of features.

**Why it matters:** It defines the evidence available to every later ML decision.

**Example:** A churn file has 300 customers, with columns describing each customer.

**Common confusion:** A dataset is the whole collection; a sample is one item inside it.

**Self-check:** Which rows and columns belong in the churn dataset?

**Introduced in:** Lab 00

## `reproducibility`

**Meaning:** Reproducibility is the ability to rerun the same data, code, and settings and get comparable results. It requires recording data, code, dependencies, configuration, and random controls.

**Why it matters:** It lets another person verify that a result came from the same procedure.

**Example:** Two terminals use the same seed and produce the same row count and metric within tolerance.

**Common confusion:** The same seed helps reproducibility, but changed code or packages can still change results.

**Self-check:** What would another learner need to rerun your churn experiment?

**Introduced in:** Lab 00

## `sample`

**Meaning:** A sample is one observation in a dataset, usually one row or one image. Every sample has the same expected structure but different observed values.

**Why it matters:** It is the unit that splits, metrics, and predictions count.

**Example:** One customer is a sample in the churn table.

**Common confusion:** A sample is one observation, while a feature is one input value or column describing it.

**Self-check:** In the churn table, what does one sample represent?

**Introduced in:** Lab 00

## `schema`

**Meaning:** A schema describes input names, data types, and validity rules. It also states constraints such as required columns, allowed categories, and numeric ranges.

**Why it matters:** It prevents silent input changes from reaching training or inference.

**Example:** The tenure column must be non-negative; churn accepts only 0 or 1.

**Common confusion:** A schema describes allowed structure; data validation checks actual data against it.

**Self-check:** Which schema rule would reject a negative tenure value?

**Introduced in:** Lab 00

## `seed`

**Meaning:** A seed is a starting number for pseudorandom generation, allowing splits or initialization to be repeated. Reusing it starts the same pseudorandom sequence in supported operations.

**Why it matters:** It makes random experiments comparable when the rest of the setup is unchanged.

**Example:** Set seed 42 before creating demo data.

**Common confusion:** A seed controls a random sequence, not every source of nondeterminism.

**Self-check:** What must stay unchanged, besides seed 42, to reproduce a split?

**Introduced in:** Lab 00

---

**Introduced in Lab 01**

## `feature`

**Meaning:** A feature is input information that a model uses to make a prediction. A feature must be available both during training and when a new prediction is requested.

**Why it matters:** It determines which information the model can use at prediction time.

**Example:** Tenure and monthly_charges are two features in the churn problem.

**Common confusion:** A feature is an input; the label or target is the answer to predict.

**Self-check:** Why can tenure be a churn feature at inference time?

**Introduced in:** Lab 01

## `label / target`

**Meaning:** A label, or target, is the outcome that a supervised model learns to predict. During supervised learning, each training sample pairs its features with this known answer.

**Why it matters:** It states the outcome the model is expected to learn.

**Example:** Churn=1 is the label for a customer who left.

**Common confusion:** A label is observed truth; a prediction is the model's estimated answer.

**Self-check:** For a customer who left, what value should the churn target contain?

**Introduced in:** Lab 01

## `parameter`

**Meaning:** A parameter is a value that a model learns from data during training. Parameters include weights and biases that change as training reduces loss.

**Why it matters:** It captures what the model learned and is updated by the optimizer.

**Example:** The weights in the linear-regression vector w are parameters.

**Common confusion:** A parameter is learned during fit; a hyperparameter is chosen before or around fit.

**Self-check:** Who learns the linear model's weights: the optimizer or the practitioner?

**Introduced in:** Lab 01

## `vectorization`

**Meaning:** Vectorization performs a calculation on a whole array instead of looping through elements in Python. Array operations let optimized numerical libraries process many values together.

**Why it matters:** It makes numerical code faster, shorter, and less error-prone.

**Example:** Use X @ w to calculate scores for every sample.

**Common confusion:** Vectorization changes how computation is expressed, not the mathematical objective.

**Self-check:** How does `X @ w` replace a loop over customer rows?

**Introduced in:** Lab 01

---

**Introduced in Lab 02**

## `data validation`

**Meaning:** Data validation checks that data follows its schema and quality rules before use. Checks can reject or report invalid rows before those rows enter the workflow.

**Why it matters:** It catches bad inputs before they distort analysis or break a service.

**Example:** Find duplicate IDs, negative ages, or a missing target.

**Common confusion:** Data validation enforces known rules; EDA searches for patterns and new questions.

**Self-check:** Which validation checks would catch a missing target and a duplicate customer ID?

**Introduced in:** Lab 02

## `EDA`

**Meaning:** Exploratory data analysis (EDA) uses statistics and plots to study data quality, distributions, and useful questions. It begins with questions, then uses summaries and plots to investigate them.

**Why it matters:** It reveals data problems and useful patterns before modeling begins.

**Example:** Compare the overall churn rate with the rate for each contract group.

**Common confusion:** EDA explores and forms hypotheses; model validation evaluates model choices.

**Self-check:** Which EDA comparison could show whether contract type relates to churn?

**Introduced in:** Lab 02

## `missing value`

**Meaning:** A missing value is absent or was not recorded in the dataset. It may be represented by null, NaN, or another agreed marker, depending on the schema.

**Why it matters:** It affects what the model can learn and must be handled consistently.

**Example:** Some samples have no monthly_charges value.

**Common confusion:** A missing value is absent; zero can be a valid recorded value.

**Self-check:** How should a missing `monthly_charges` value differ from a real zero?

**Introduced in:** Lab 02

## `outlier`

**Meaning:** An outlier is an observation far from most other values in the data. Its cause should be checked with domain knowledge before it is removed or capped.

**Why it matters:** It may reveal a data error, a rare case, or an important business event.

**Example:** An unusually high bill may be an error or a real business customer.

**Common confusion:** An outlier is unusual, not automatically incorrect.

**Self-check:** What evidence would tell you whether an unusually high bill is valid?

**Introduced in:** Lab 02

---

**Introduced in Lab 03**

## `gradient`

**Meaning:** A gradient shows the direction and rate at which loss changes when a parameter changes. Its sign gives direction, and its magnitude shows how strongly the loss responds.

**Why it matters:** It tells the optimizer how each parameter should move to reduce loss.

**Example:** A positive gradient suggests lowering the parameter by the learning rate.

**Common confusion:** A gradient is a direction of change; the learning rate scales the update size.

**Self-check:** If a parameter has a positive gradient, which direction should gradient descent move it?

**Introduced in:** Lab 03

## `learning rate`

**Meaning:** The learning rate controls the size of each parameter update. The optimizer multiplies this value by the gradient when forming an update.

**Why it matters:** It controls whether training moves steadily, too slowly, or unstably.

**Example:** A learning rate that is too large makes loss oscillate or grow.

**Common confusion:** The learning rate is an update setting, not the loss being minimized.

**Self-check:** What training pattern suggests that the learning rate is too large?

**Introduced in:** Lab 03

## `loss`

**Meaning:** Loss is the error value that a model tries to reduce during training. Different tasks use different loss functions, such as MSE for regression or cross-entropy for classification.

**Why it matters:** It gives training a single objective to minimize.

**Example:** MSE penalizes the squared distance between prediction and target.

**Common confusion:** Loss guides training; a metric reports the quality people care about.

**Self-check:** Why does a large prediction error contribute strongly to MSE?

**Introduced in:** Lab 03

## `prediction`

**Meaning:** A prediction is the value that a model produces for one sample. For regression it may be a number; for classification it may be a class or probability.

**Why it matters:** It is the model output that downstream users or systems act on.

**Example:** The model predicts monthly_charges of 42.5.

**Common confusion:** A prediction is an output value; a label is the observed answer.

**Self-check:** Is a churn probability of 0.72 a prediction, a target, or both?

**Introduced in:** Lab 03

---

**Introduced in Lab 04**

## `baseline`

**Meaning:** A baseline is a simple benchmark used to judge whether a more complex model provides a real improvement. It can be a simple rule, a dummy model, or the smallest reasonable learned model.

**Why it matters:** It provides a minimum result that a more complex model must beat.

**Example:** A dummy classifier always predicts the most common class.

**Common confusion:** A baseline is a comparison point, not necessarily the final model.

**Self-check:** What must logistic regression demonstrate beyond a majority-class baseline?

**Introduced in:** Lab 04

## `confusion matrix`

**Meaning:** A confusion matrix is a table that counts each combination of true class and predicted class. Its cells separate true positives, false positives, true negatives, and false negatives.

**Why it matters:** It shows the exact types of classification mistakes hidden by one score.

**Example:** The churn=1 row shows how many actual churners were predicted as 0.

**Common confusion:** A confusion matrix contains counts; precision, recall, and F1 summarize those counts.

**Self-check:** Which confusion-matrix cell counts churners predicted as non-churners?

**Introduced in:** Lab 04

## `data split`

**Meaning:** A data split divides a dataset into non-overlapping subsets with different roles. Typical roles are training, validation, and testing, with no sample shared across them.

**Why it matters:** It protects evaluation by giving each subset one clear role.

**Example:** Use 70% for training, 15% for validation, and 15% for testing.

**Common confusion:** A data split creates subsets; cross-validation rotates several folds through roles.

**Self-check:** Why must one customer not appear in both training and test sets?

**Introduced in:** Lab 04

## `fit`

**Meaning:** To fit a model or transform is to learn its state from training data. For a scaler, fit learns statistics; for a model, fit learns predictive parameters.

**Why it matters:** It is where learned state enters a model or preprocessing step.

**Example:** Call pipeline.fit(X_train, y_train).

**Common confusion:** fit learns state; transform applies a learned or fixed transformation.

**Self-check:** What does `pipeline.fit(X_train, y_train)` learn from the training data?

**Introduced in:** Lab 04

## `metric`

**Meaning:** A metric is a number that measures one aspect of model quality and should match the goal and cost of errors. No single metric describes every kind of quality, so its meaning must be stated.

**Why it matters:** It connects model evaluation to the business cost of errors.

**Example:** Recall measures the proportion of churners that the model finds.

**Common confusion:** A metric is a measurement; loss is the objective optimized during training.

**Self-check:** Which metric best reflects the goal of finding most churners?

**Introduced in:** Lab 04

## `model validation`

**Meaning:** Model validation evaluates model choices on data that was not used to fit them. It includes comparing candidates and thresholds on validation data before the final test.

**Why it matters:** It lets you compare choices while keeping the final test estimate independent.

**Example:** Compare F1 on the validation set before opening the test set.

**Common confusion:** Validation guides choices; testing estimates the final chosen system once.

**Self-check:** Why should model validation happen before the test set is opened?

**Introduced in:** Lab 04

## `precision / recall / F1`

**Meaning:** Precision measures correct positive predictions, recall measures found positive samples, and F1 balances the two. All three come from confusion-matrix counts but answer different questions.

**Why it matters:** It explains the trade-off between false alarms and missed churners.

**Example:** The churn project prioritizes recall while still tracking precision.

**Common confusion:** Precision asks whether positive predictions are right; recall asks whether positives were found.

**Self-check:** If missing a churner is costly, why might recall matter more than precision?

**Introduced in:** Lab 04

## `test set`

**Meaning:** A test set is a held-back data subset opened only after model and threshold choices are fixed. It must remain untouched by preprocessing fit, model selection, and threshold tuning.

**Why it matters:** It gives one final, less-biased estimate after all choices are fixed.

**Example:** Run the test once after selecting logistic regression.

**Common confusion:** The test set is not another validation set for repeated tuning.

**Self-check:** When is it acceptable to evaluate the churn model on the test set?

**Introduced in:** Lab 04

## `training set`

**Meaning:** A training set is the data subset used to learn model parameters and preprocessing state. Validation and test samples must not influence anything learned from this subset.

**Why it matters:** Keeping all learned state within this split protects validation and test results from leakage.

**Example:** Fit logistic regression only on the training set.

**Common confusion:** The training set teaches the model; the validation set only guides choices.

**Self-check:** Which data should a scaler use when it learns its mean and standard deviation?

**Introduced in:** Lab 04

## `validation set`

**Meaning:** A validation set is the data subset used to choose a model, threshold, or hyperparameter without fitting on it. It may be examined many times for decisions, but its labels must not enter fit.

**Why it matters:** It supports model choices without teaching the model or replacing the test set.

**Example:** Choose a threshold with satisfactory recall on the validation set.

**Common confusion:** The validation set guides choices; the test set checks the locked result.

**Self-check:** Can you tune a churn threshold on validation data without fitting the model on it?

**Introduced in:** Lab 04

---

**Introduced in Lab 05**

## `data leakage`

**Meaning:** Data leakage happens when training uses information from validation, testing, or the future. Leakage can come from future data, target-derived features, duplicate customers, or preprocessing before a split.

**Why it matters:** It can make evaluation look excellent even when the model will fail in use.

**Example:** Fitting a scaler on the entire dataset before splitting leaks test information.

**Common confusion:** Leakage can occur without duplicate rows, such as fitting a scaler before splitting.

**Self-check:** Why does fitting a scaler on the full dataset leak test information?

**Introduced in:** Lab 05

## `pipeline`

**Meaning:** A pipeline runs preprocessing and modeling steps in a fixed order. When the pipeline is fitted, each learned preprocessing step sees only training data.

**Why it matters:** It keeps preprocessing and prediction steps consistent across splits and inference.

**Example:** A Pipeline connects a ColumnTransformer to logistic regression.

**Common confusion:** A pipeline is the ordered container; preprocessing is only the data-preparation part.

**Self-check:** How does a pipeline help keep scaling consistent during inference?

**Introduced in:** Lab 05

## `preprocessing`

**Meaning:** Preprocessing prepares raw data for a model by filling missing values, scaling numbers, or encoding categories. Some steps are fixed, while others learn values such as medians, category lists, or scaling statistics.

**Why it matters:** It turns raw data into model-ready inputs while preserving split boundaries.

**Example:** Fill missing values with the median, then one-hot encode the contract column.

**Common confusion:** Preprocessing may learn state, so it is not always a harmless fixed cleanup.

**Self-check:** Which preprocessing values must be learned only from the training split?

**Introduced in:** Lab 05

## `transform`

**Meaning:** A transform applies a fixed rule or state learned from the training set to input data. The same fitted transform should then be reused for validation, test, and inference data.

**Why it matters:** It applies a learned or fixed rule consistently to new inputs.

**Example:** StandardScaler learns the mean and standard deviation from training data, then applies them to validation data.

**Common confusion:** transform applies a rule; fit learns any state required by that rule.

**Self-check:** What is different between `fit_transform` on training data and `transform` on validation data?

**Introduced in:** Lab 05

---

**Introduced in Lab 06**

## `class imbalance`

**Meaning:** Class imbalance occurs when the numbers of samples in different classes vary greatly. The minority class can have too little influence on accuracy or model training.

**Why it matters:** It makes accuracy unreliable and shifts attention to class-sensitive metrics.

**Example:** Only 8% of customers churn so accuracy is easily misleading.

**Common confusion:** Class imbalance describes label counts, not unequal business costs by itself.

**Self-check:** Why can 92% accuracy be weak when only 8% of customers churn?

**Introduced in:** Lab 06

## `threshold`

**Meaning:** A threshold converts a score or probability into a decision label. Lowering it usually finds more positive cases but also creates more false alarms.

**Why it matters:** It converts model scores into an operational decision rule.

**Example:** Probabilities of 0.35 or higher are labeled churn.

**Common confusion:** A threshold changes decisions, not the underlying predicted probability.

**Self-check:** What happens to churn recall when the decision threshold is lowered?

**Introduced in:** Lab 06

---

**Introduced in Lab 07**

## `bias / variance`

**Meaning:** High bias often means a model is too simple, while high variance means it is too sensitive to its training data. Bias causes systematic underfitting, while variance causes unstable behavior across datasets.

**Why it matters:** It helps diagnose whether to add model capacity, data, or regularization.

**Example:** Low training and validation scores on a learning curve suggest high bias.

**Common confusion:** Bias and variance are error tendencies, not the protected attributes called demographic bias.

**Self-check:** What learning-curve pattern suggests high bias rather than high variance?

**Introduced in:** Lab 07

## `cross-validation`

**Meaning:** Cross-validation repeatedly evaluates a model on different folds to estimate its stability. Each sample is used for validation in one fold and for training in the others.

**Why it matters:** It estimates performance variation instead of trusting one lucky split.

**Example:** 3-fold CV generates three validation scores.

**Common confusion:** Cross-validation estimates variability; it does not create more independent data.

**Self-check:** Why are several CV scores more informative than one validation score?

**Introduced in:** Lab 07

## `fold`

**Meaning:** A fold is one subset that takes a turn as validation data during cross-validation. Folds should preserve important structure, such as class balance or customer grouping.

**Why it matters:** It defines each temporary training and validation role in CV.

**Example:** In fold 2, the second group is kept for evaluation.

**Common confusion:** A fold is one subset inside cross-validation, not the final test set.

**Self-check:** In three-fold CV, how many times does each fold serve as validation data?

**Introduced in:** Lab 07

## `overfitting`

**Meaning:** Overfitting happens when a model learns the training data too closely and performs poorly on new data. It appears as a gap between training performance and performance on unseen data.

**Why it matters:** It warns that strong training results may not generalize.

**Example:** Train score increases and validation score decreases.

**Common confusion:** Overfitting is a generalization gap, not simply a model with many parameters.

**Self-check:** What does rising training score with falling validation score suggest?

**Introduced in:** Lab 07

---

**Introduced in Lab 08**

## `bagging / boosting`

**Meaning:** Bagging trains several models mostly independently, while boosting trains them in sequence to correct earlier errors. Bagging mainly reduces instability; boosting focuses later models on earlier mistakes.

**Why it matters:** It explains how tree ensembles gain stability or correct earlier errors.

**Example:** Random forest uses bagging, gradient boosting uses boosting.

**Common confusion:** Bagging and boosting are different ensemble strategies, not interchangeable names.

**Self-check:** Which strategy describes random forest, and which describes gradient boosting?

**Introduced in:** Lab 08

## `ensemble`

**Meaning:** An ensemble combines predictions from several member models. The member predictions are combined by voting, averaging, or another aggregation rule.

**Why it matters:** It often improves robustness by combining different prediction errors.

**Example:** Random forest takes results from many decision trees.

**Common confusion:** An ensemble is the combined model; bagging and boosting are ways to build one.

**Self-check:** How does random forest turn many tree outputs into one prediction?

**Introduced in:** Lab 08

## `hyperparameter`

**Meaning:** A hyperparameter is a setting chosen by the practitioner rather than learned directly during fit. Examples include tree depth, regularization strength, and the number of trees.

**Why it matters:** It controls model behavior and must be chosen with validation evidence.

**Example:** The number of trees and maximum tree depth are random-forest hyperparameters.

**Common confusion:** A hyperparameter is selected; a parameter is learned from training data.

**Self-check:** Why must maximum tree depth be chosen with validation rather than test data?

**Introduced in:** Lab 08

---

**Introduced in Lab 09**

## `ablation`

**Meaning:** An ablation adds or removes exactly one ingredient so its impact can be measured. All other data, code, and settings should stay fixed so the comparison is fair.

**Why it matters:** It isolates whether one feature group or technique truly caused an improvement.

**Example:** Remove the behavioral feature group, then compare validation AUC.

**Common confusion:** An ablation changes one ingredient; ordinary tuning may change many settings.

**Self-check:** What can you conclude if validation AUC falls after removing one feature group?

**Introduced in:** Lab 09

## `feature engineering`

**Meaning:** Feature engineering creates or transforms inputs using problem knowledge and only information available at prediction time. Useful engineered features encode relevant structure without using future or target information.

**Why it matters:** It can expose useful signal, but only when the feature exists at inference time.

**Example:** Create tenure_bucket from tenure if used during inference.

**Common confusion:** Feature engineering creates inputs; feature selection keeps or removes existing inputs.

**Self-check:** Would `tenure_bucket` still be available when predicting a new customer?

**Introduced in:** Lab 09

---

**Introduced in Lab 10**

## `error analysis`

**Meaning:** Error analysis studies incorrect predictions systematically to form hypotheses and plan further tests. The analyst inspects false positives and false negatives across examples and groups.

**Why it matters:** It turns failures into specific, testable improvement ideas.

**Example:** Review false negatives by contract type.

**Common confusion:** Error analysis studies observed failures; a metric only summarizes them.

**Self-check:** Which false-negative pattern would you investigate first in the churn model?

**Introduced in:** Lab 10

## `failure taxonomy`

**Meaning:** A failure taxonomy groups errors by observable cause instead of treating every mistake as the same. Useful categories are specific enough to count and connect to a possible remedy.

**Why it matters:** It makes recurring failure patterns measurable instead of anecdotal.

**Example:** Group errors as data problems, boundary cases, missing signals, or label noise.

**Common confusion:** A failure taxonomy names error groups; a confusion matrix groups errors only by class labels.

**Self-check:** Would "missing signal" and "label noise" belong in the same failure category?

**Introduced in:** Lab 10

## `slice`

**Meaning:** A slice is a group of samples with a shared characteristic that is evaluated separately. Slice results should be compared with overall results and reported with support.

**Why it matters:** It reveals whether overall performance hides harm to an important group.

**Example:** The new-customer slice contains customers with tenure below three months.

**Common confusion:** A slice is a meaningful subgroup; a data split assigns training or evaluation roles.

**Self-check:** Which metric would you inspect for customers with tenure below three months?

**Introduced in:** Lab 10

## `support`

**Meaning:** Support is the number of actual samples in a class or slice. Small support makes an apparently perfect metric uncertain.

**Why it matters:** It shows whether a strong-looking slice metric has enough evidence.

**Example:** 100% recall on support=2 is not enough for a strong conclusion.

**Common confusion:** Support is a count, not a quality score.

**Self-check:** Why is recall of 100% on only two churners weak evidence?

**Introduced in:** Lab 10

---

**Introduced in Lab 11**

## `artifact`

**Meaning:** An artifact is the set of model, configuration, metric, and metadata files needed to reproduce or serve predictions. It should be versioned and accompanied by enough provenance to verify how it was produced.

**Why it matters:** It packages the exact files needed to reproduce or serve a model.

**Example:** The artifact contains model.joblib and manifest.json.

**Common confusion:** An artifact is the saved deliverable; a checkpoint is a training state used to resume.

**Self-check:** Which files and metadata must travel with `model.joblib`?

**Introduced in:** Lab 11

## `inference`

**Meaning:** Inference uses a trained model to produce predictions for new input. It must apply exactly the preprocessing and feature order learned during training.

**Why it matters:** It is the point where a trained model produces value on unseen inputs.

**Example:** Load the artifact, then predict churn for an unseen customer.

**Common confusion:** Inference uses a trained model; training updates its parameters.

**Self-check:** What should happen when the saved churn model receives one unseen customer?

**Introduced in:** Lab 11

## `manifest`

**Meaning:** A manifest lists an artifact's contents, versions, checksums, and origin. Checksums help detect changed files, while metadata explains how those files were created.

**Why it matters:** It makes an artifact auditable and protects against loading the wrong files.

**Example:** Manifest records seed, feature order and SHA-256.

**Common confusion:** A manifest describes files and provenance; the artifact contains the actual files.

**Self-check:** Which manifest field would reveal that a model file changed unexpectedly?

**Introduced in:** Lab 11

---

**Introduced in Lab 12**

## `configuration`

**Meaning:** Configuration is the set of values that controls a run and is saved for reruns and comparisons. It belongs outside reusable code so one setting can change without editing program logic.

**Why it matters:** It records run choices so experiments can be repeated and compared fairly.

**Example:** A YAML configuration records the seed, feature list, and threshold.

**Common confusion:** Configuration controls a run; learned parameters are model state.

**Self-check:** Which churn run choices should be stored in configuration rather than source code?

**Introduced in:** Lab 12

## `package`

**Meaning:** A package organizes Python code into modules that tests, CLIs, notebooks, and services can import. An installable package avoids copying important logic between notebooks.

**Why it matters:** It makes ML logic reusable by tests, CLIs, notebooks, and services.

**Example:** Put the training logic in src/ml_roadmap instead of copying it between notebooks.

**Common confusion:** A package organizes code; a container bundles the runtime environment.

**Self-check:** Why should training logic live in `src/ml_roadmap` instead of several notebooks?

**Introduced in:** Lab 12

---

**Introduced in Lab 13**

## `data contract`

**Meaning:** A data contract is a machine-readable agreement about data schema, allowed values, and validation errors. Both producers and consumers can validate the same contract at their boundary.

**Why it matters:** It turns assumptions about input data into enforceable checks.

**Example:** Reject input that lacks the tenure column before it reaches the model.

**Common confusion:** A data contract governs data; an API contract governs service requests and responses.

**Self-check:** What should the data contract do when the `tenure` column is absent?

**Introduced in:** Lab 13

## `parity`

**Meaning:** Parity means two paths produce sufficiently consistent results for the same input. The acceptable tolerance depends on whether outputs are labels, probabilities, or floating-point arrays.

**Why it matters:** It detects behavior changes introduced by serialization or a new serving path.

**Example:** Prediction before and after save/load must match within tolerance.

**Common confusion:** Parity means sufficiently matching behavior, not necessarily byte-identical files.

**Self-check:** How would you test prediction parity before and after saving the model?

**Introduced in:** Lab 13

---

**Introduced in Lab 14**

## `API contract`

**Meaning:** An API contract defines an inference service's inputs, outputs, status codes, and errors. Both client and server rely on the same contract to exchange valid data.

**Why it matters:** It gives clients a stable interface and predictable failure behavior.

**Example:** Payload missing tenure returns 422 instead of 500.

**Common confusion:** An API contract describes behavior; a data contract focuses on input data rules.

**Self-check:** Which status code should the API return when required churn input is missing?

**Introduced in:** Lab 14

## `latency`

**Meaning:** Latency is the elapsed time between receiving a request and returning its response. It should be measured under stated conditions such as warm-up state and batch size.

**Why it matters:** It determines whether an inference service feels responsive enough for its use case.

**Example:** Measure warm latency for a mini-batch of 16 samples.

**Common confusion:** Latency measures elapsed time; throughput measures how much work finishes per unit time.

**Self-check:** Why must a warm latency result include the batch size?

**Introduced in:** Lab 14

---

**Introduced in Lab 15**

## `CI`

**Meaning:** Continuous integration (CI) automatically runs checks and tests when code changes. Typical CI checks include tests, linting, and type checking, but not an automatic production deployment.

**Why it matters:** It catches regressions automatically before changed code is merged.

**Example:** The CI pipeline runs pytest, Ruff, and mypy without deploying to AWS.

**Common confusion:** CI validates changes; deployment releases them to an environment.

**Self-check:** Which checks should run in CI before the churn package is merged?

**Introduced in:** Lab 15

## `container`

**Meaning:** A container bundles an application with its dependencies and runtime configuration in an isolated environment. Its image should contain only what the service needs and should run as a non-root user.

**Why it matters:** It makes an application portable without assuming the host has matching dependencies.

**Example:** Docker images run APIs using non-root users.

**Common confusion:** A container is a runnable package, not a full virtual machine.

**Self-check:** What makes a containerized inference API more portable than a host-only setup?

**Introduced in:** Lab 15

---

**Introduced in Lab 16**

## `batch`

**Meaning:** A batch is a group of samples processed together before a parameter update. Training normally performs one forward and backward pass for each batch.

**Why it matters:** It balances compute efficiency, memory use, and gradient noise.

**Example:** Batch size 32 means the model reads 32 images in each step.

**Common confusion:** A batch groups samples; an epoch covers the entire training set.

**Self-check:** How many images contribute to one step when batch size is 32?

**Introduced in:** Lab 16

## `device`

**Meaning:** A device is the hardware, such as a CPU or GPU, where tensors and models perform computations. The model and every tensor used in one operation must be on compatible devices.

**Why it matters:** It prevents runtime errors caused by tensors living on different hardware.

**Example:** Place the model and its input on the same CPU or CUDA device.

**Common confusion:** A device is compute hardware; a tensor is the data placed on it.

**Self-check:** Why does a CUDA model fail when its input tensor remains on the CPU?

**Introduced in:** Lab 16

## `epoch`

**Meaning:** An epoch is one complete pass through the training set. The number of optimizer steps per epoch depends on dataset size and batch size.

**Why it matters:** It provides the basic unit for measuring progress through training data.

**Example:** Three epochs use each training sample about three times.

**Common confusion:** An epoch is one pass; an optimizer step may happen many times within that pass.

**Self-check:** If the training set has 320 images and batch size 32, how many batches form one epoch?

**Introduced in:** Lab 16

## `optimizer`

**Meaning:** An optimizer is an algorithm that uses gradients to update model parameters. It may also keep moving averages or other state used to form later updates.

**Why it matters:** It determines how gradients become parameter updates.

**Example:** Adam updates the classifier head after loss.backward().

**Common confusion:** The optimizer applies updates; the learning rate is one setting that controls them.

**Self-check:** What information does Adam use after `loss.backward()`?

**Introduced in:** Lab 16

## `tensor`

**Meaning:** A tensor is a multidimensional array used to represent data and computations in a neural network. Its shape, data type, and device determine how operations can use it.

**Why it matters:** It carries neural-network inputs, activations, and outputs with explicit shapes.

**Example:** A batch of images has shape [32, 3, 160, 160].

**Common confusion:** A tensor is an array with shape and dtype, not the neural network itself.

**Self-check:** What does each dimension in `[32, 3, 160, 160]` represent?

**Introduced in:** Lab 16

---

**Introduced in Lab 17**

## `augmentation`

**Meaning:** Augmentation applies valid random changes to training samples to add diversity without changing their labels. The transformation must preserve the task label and is normally random only for training.

**Why it matters:** It reduces overfitting by showing the model valid variations of training images.

**Example:** Flip training images horizontally; resize validation images deterministically.

**Common confusion:** Augmentation changes training examples; preprocessing also prepares validation and inference inputs.

**Self-check:** Why should validation images be resized deterministically instead of randomly augmented?

**Introduced in:** Lab 17

## `backbone`

**Meaning:** A backbone is the main network section that extracts features before the task-specific classifier head. A small classifier head converts those features into scores for the new classes.

**Why it matters:** It supplies reusable visual features before the task-specific classifier.

**Example:** Use a pretrained ResNet18 as the backbone.

**Common confusion:** The backbone extracts features; the classifier head maps them to task labels.

**Self-check:** Which part of pretrained ResNet18 is replaced for a new image-classification task?

**Introduced in:** Lab 17

## `checkpoint`

**Meaning:** A checkpoint saves training state so a run can continue after interruption. It often contains model parameters, optimizer state, epoch number, and training history.

**Why it matters:** It preserves progress and enables a stopped training run to resume.

**Example:** The latest checkpoint contains the model, optimizer, epoch, and history.

**Common confusion:** A checkpoint may resume training; a final artifact is prepared for evaluation or serving.

**Self-check:** Which checkpoint fields are needed to resume an interrupted run faithfully?

**Introduced in:** Lab 17

## `freeze`

**Meaning:** To freeze a model section means temporarily preventing its parameters from being updated during training. Frozen parameters still take part in the forward pass but receive no optimizer updates.

**Why it matters:** It reduces compute and protects pretrained features during early training.

**Example:** Set requires_grad=False for backbone.

**Common confusion:** Freeze stops parameter updates but still allows data to pass through the layer.

**Self-check:** What does `requires_grad=False` change for the backbone during training?

**Introduced in:** Lab 17

## `transfer learning`

**Meaning:** Transfer learning reuses knowledge from a pretrained model for a new problem. The classifier head can be trained first while the pretrained backbone remains frozen.

**Why it matters:** It lowers data and compute needs by starting from useful pretrained features.

**Example:** Keep the ResNet18 backbone and replace the classifier head.

**Common confusion:** Transfer learning is the overall reuse strategy; fine-tuning is one later training stage.

**Self-check:** Why can transfer learning work with fewer labeled images than training from scratch?

**Introduced in:** Lab 17

---

**Introduced in Lab 18**

## `early stopping`

**Meaning:** Early stopping ends training after validation performance has not improved for a chosen number of epochs. A patience setting defines how many non-improving epochs are tolerated.

**Why it matters:** It avoids wasting epochs after validation performance stops improving.

**Example:** Stop after validation loss fails to improve for two epochs.

**Common confusion:** Early stopping is a training rule, not a guarantee against all overfitting.

**Self-check:** After how many non-improving epochs should a patience-two run stop?

**Introduced in:** Lab 18

## `fine-tuning`

**Meaning:** Fine-tuning continues training some pretrained layers with a small learning rate for the new problem. It commonly follows frozen-head training and uses a lower learning rate for unfrozen layers.

**Why it matters:** It adapts pretrained features to the new task after a stable baseline exists.

**Example:** Unfreeze layer4 after frozen-head baseline.

**Common confusion:** Fine-tuning updates pretrained layers; frozen-head training leaves them unchanged.

**Self-check:** Why should the pretrained backbone use a small learning rate during fine-tuning?

**Introduced in:** Lab 18

---

**Introduced in Lab 19**

## `macro average`

**Meaning:** A macro average calculates a metric for each class and gives every class equal weight. The per-class scores are added and divided by the number of classes.

**Why it matters:** It gives rare and common classes equal influence on the reported score.

**Example:** Macro F1 averages the F1 scores for churn and non-churn as equally weighted classes.

**Common confusion:** Macro average weights classes equally; weighted average weights them by support.

**Self-check:** How does macro F1 treat churn and non-churn when their supports differ greatly?

**Introduced in:** Lab 19

## `weighted average`

**Meaning:** A weighted average gives each class a weight based on its support. Large classes therefore influence the result more than small classes.

**Why it matters:** It reflects dataset frequency but can hide poor performance on rare classes.

**Example:** Weighted F1 can look high when common classes do well but rare classes do poorly.

**Common confusion:** Weighted average follows support; macro average treats every class equally.

**Self-check:** How can weighted F1 look strong while the rare class performs poorly?

**Introduced in:** Lab 19

---

**Introduced in Lab 20**

## `budget alert`

**Meaning:** A budget alert sends a notification when actual or forecast AWS cost reaches a threshold. It can watch actual and forecast spending, but AWS resources continue running until something stops them.

**Why it matters:** It gives early cost visibility before an experiment creates a surprise bill.

**Example:** Send email alerts for both Actual and Forecasted AWS Budgets.

**Common confusion:** A budget alert sends a warning; it does not automatically stop AWS spending.

**Self-check:** What action is still required after a budget alert reports unexpected AWS cost?

**Introduced in:** Lab 20

## `CloudWatch Logs`

**Meaning:** CloudWatch Logs stores runtime logs on AWS, where sensitive data and retention require deliberate controls. Log groups need explicit retention, access control, and rules that prevent sensitive values from being written.

**Why it matters:** It provides evidence for debugging while retention and privacy controls limit risk.

**Example:** Retain the Lambda log group for one day.

**Common confusion:** CloudWatch Logs stores runtime logs; CloudWatch metrics store numeric measurements.

**Self-check:** Which Lambda evidence belongs in CloudWatch Logs, and which customer data should stay out?

**Introduced in:** Lab 20

## `IAM`

**Meaning:** AWS Identity and Access Management (IAM) controls identities and permissions using least privilege. Policies attach allowed actions and resources to users, roles, or services.

**Why it matters:** It limits what each AWS identity or service is allowed to do.

**Example:** The Lambda role can read only the required model object in S3.

**Common confusion:** IAM controls access; security groups control network traffic.

**Self-check:** What is the least S3 permission the inference Lambda role needs?

**Introduced in:** Lab 20

## `idempotent cleanup`

**Meaning:** Idempotent cleanup can run repeatedly and still move toward the same clean state. It treats already-absent resources as a successful state rather than a fatal error.

**Why it matters:** It lets cleanup be retried safely after a partial failure.

**Example:** Clean up resources for the exact project ID, then scan again.

**Common confusion:** Idempotent cleanup is safe to repeat; a one-shot delete may fail when partly completed.

**Self-check:** Why should running the same cleanup command twice remain safe?

**Introduced in:** Lab 20

## `Lambda`

**Meaning:** AWS Lambda runs functions on request without requiring users to manage servers. AWS provisions the execution environment and charges for the resources used by each invocation.

**Why it matters:** It runs inference on demand without maintaining a continuously running server.

**Example:** Invoke the private Lambda function to run tabular inference.

**Common confusion:** Lambda is compute; S3 is object storage.

**Self-check:** Which part of the tabular inference workflow runs inside Lambda?

**Introduced in:** Lab 20

## `residual scan`

**Meaning:** A residual scan checks for project resources that remain after cleanup. It should check every relevant service and identify anything that still needs removal.

**Why it matters:** It verifies that cleanup actually removed the project resources.

**Example:** Scan CloudFormation, S3, Lambda, CloudWatch Logs, and IAM.

**Common confusion:** A residual scan verifies absence; cleanup performs the deletion actions.

**Self-check:** Which AWS services should the residual scan inspect after this project?

**Introduced in:** Lab 20

## `S3`

**Meaning:** Amazon S3 is an object storage service used here for small model artifacts. Each object has a key inside a bucket and can be protected with IAM and encryption.

**Why it matters:** It stores model artifacts durably without placing them in the application image.

**Example:** Upload portable_model.json to a private bucket.

**Common confusion:** S3 stores objects in buckets; a file system exposes directories and file operations.

**Self-check:** Which model file should be uploaded to the private S3 bucket?

**Introduced in:** Lab 20
