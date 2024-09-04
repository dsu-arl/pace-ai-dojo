In this challenge, you'll learn how to use a decision tree to classify flowers based on the length and width of sepals and petals. Decision trees are a supervised learning algorithm used for both classification and regression tasks, where they split data into branches based on feature values to make predictions. Each internal node represents a decision based on a feature, each branch represents an outcome of that decision, and each leaf node represents a final prediction or outcome.

As with the machine learning models that we have covered, we first need to import it from `sklearn` and then define it.
```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
```

We can train and make predictions from our decision tree the same way as the previous models.

To get this flag, create a decision tree classifier model, train it using the iris dataset, make predictions on the test dataset and retrieve its test dataset accuracy!