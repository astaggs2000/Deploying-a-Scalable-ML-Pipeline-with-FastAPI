# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model is a Random Forest Classifier developed using the Scikit-learn library. The model performs binary classification to predict whether an individual's annual income is $50,000 or less, or greater than $50,000 based on census data. Default hyperparameters were used, with a random state of 42 to support reproducibility.

## Intended Use
This model is intended to predict whether an individual's annual income is greater than $50,000 based on demographic and employment-related census data. The model was developed for educational purposes to demonstrate the implementation and deployment of a machine learning classification pipeline using FastAPI. It is not intended to be used for employment, lending, or other consequential financial decisions.

## Training Data
The model was trained using the census dataset provided in the project. The dataset contains demographic and employment-related information, including age, education, occupation, marital status, race, sex, and hours worked per week. A total of 80% of the dataset was allocated for training. Categorical features were transformed using one-hot encoding, and the salary target variable was transformed using label binarization.

## Evaluation Data
The remaining 20% of the census dataset was used to evaluate the model's performance on unseen data. The evaluation data was processed using the same encoder and label binarizer fitted during training to maintain consistency. Model performance was evaluated across the entire testing dataset and individual subsets of all eight categorical features.

## Metrics
The model was evaluated using precision, recall, and F1 score. The model achieved a precision of 73.91%, a recall of 63.84%, and an F1 score of 68.51%. These results indicate that the model is more effective at correctly identifying positive income predictions than identifying all individuals earning more than $50,000. Performance metrics were also calculated for each categorical slice to evaluate differences in model performance across demographic and employment-related groups.

## Ethical Considerations
The census dataset contains sensitive demographic information, including race, sex, age, and native country. Historical income disparities and biases within the training data may influence the model's predictions and result in unequal performance across demographic groups. Categorical slice analysis was performed to help identify potential differences in model performance. However, this analysis does not guarantee that the model is free from bias. The model should not be used to make decisions that could result in discrimination or unfair treatment of individuals.

## Caveats and Recommendations
The model's performance is limited by the quality and representativeness of the census dataset. Certain categorical groups contain fewer records than others, which may result in unreliable performance metrics for smaller groups. The model's recall of 63.84% indicates that some individuals earning more than $50,000 are incorrectly classified. Future improvements could include hyperparameter tuning, additional training data, and further evaluation of potential demographic biases. The model should be evaluated regularly before being considered for any practical application.
