With the models so far, we haven't changed anything about them. Each machine learning model has its own values called hyperparameters which are like the settings of the model that the user can modify to improve performance. One hyperparameter for a random forest model is `n_estimators` which defines the number of decision trees in the forest. Each model has its own default hyperparameter values which is why we've been able to train our models without providing any specific values when initializing our models. For example, the default value for the `n_estimators` hyperparameter is `100` so a random forest model can be defined as
```python
model = RandomForestClassifier(n_estimators=100)
```
which is the same as how we defined it before since it's using the default `n_estimators` value.

For a full list of hyperparameters and their default values for the random forest model, you can view them in the documentation located [here](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

While not needed for the challenge, you might notice that we call `model.predict_proba()` for use with the `log_loss()` function. This is because we need the probability values for each class to accurately calculate the loss. `predict()` simply outputs the class with the highest probability.

Now it's your turn! Using the provided notebook, modify the `n_estimators` hyperparameter so that your model's loss on the test dataset is `0.0252`. HINT: The correct number of `n_estimators` will be in the range from 10 to 200 and will be an increment of 10 (no need to try 54 or 123).