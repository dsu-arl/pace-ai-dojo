In this challenge, you'll learn how to use a logistic regression model to classify flowers based on the length and width of sepals and petals. A logistic regression model is a type of machine learning algorithm used for classification that predicts the probability of a data point belonging to a specific class.

The difference between this level and the previous one is that now instead of outputting a numeric value, our model will still output a number, but that number will correspond with a specific class. For example, if our classes were either 'no' or 'yes', our model could output 0 to indicate 'no' or 1 to indicate 'yes'. The dataset we'll be using, called the Iris dataset, has 3 possible classes: Iris Setosa, Iris Versicolor, or Iris Virginica.

The only change we have to make now is when defining our model. To define our logistic regression model, we can import it from the same `sklearn` library and initialize it how we did with the linear regression model:
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
```

You can train and get predictions from this logistic regression model the same way as the linear regression model, by using `fit()` and `predict()`

To determine how good a classification model is, we can use the `accuracy_score()` function from `sklearn.metrics`. This will compute the accuracy of our model by getting the percentage of correctly guessed labels out of the total number of labels. For example if your dataset had 100 rows and the model predicted the correct label for 92 of them, `accuracy_score()` would return 0.92 (100% is outputted as 1.0).

We'll give `accuracy_score()` two parameters, `y_test` our correct labels for the test dataset and `y_pred` our model's predictions.
```python
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
```
To get this flag, create a logistic regression model, train it using the iris dataset, make predictions on the test dataset and retrieve its test dataset accuracy!