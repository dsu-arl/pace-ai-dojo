Linear regression is a fundamental machine learning algorithm used for predicting continuous values. The goal is to find the linear relationship between input features (independent variables) and the target variable (dependent variable).

To define a linear regression model, we first need to import it from the sklearn module:

```python
from sklearn.linear_model import LinearRegression
```

Now to define our linear regression model, it's as simple as:
```python
model = LinearRegression()
```
NOTE: Our model variable can be named anything, it doesn't need to specifically be named `model`.

To be able to make predictions with our model, we need to train it. During training, the linear regression model attempts to learn the linear relationship between the features and the target by finding the best-fitting straight line that represents the relationship between these variables.

To train our linear regression model using our train datasets, we use the method `fit()`:
```python
model.fit(X_train, y_train)
```
The first parameter is your training data and the second parameter is the target values.

Once a model has been trained, you can now use it to make predictions on new data. Making predictions with a machine learning model is as easy as:
```python
y_pred = model.predict(X_test)
```
`model.predict(X_test)` will get an output for each row in `X_test` and return it to be stored in an output variable, in our case it'll be stored in the `y_pred` variable.

To determine how well your model is able to fit to the training data on a regression problem, we use mean squared error as our metric. Values closer to 0 indicate a better model. To calculate the mean squared error, we can use the function from the sklearn module:
```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
```
Since `y_test` contains the true values from `X_test` which is what we made our predictions for, we can use that to compare with our output `y_pred` to calculate the mean squared error.

In this level, we will train a linear regression model on the California housing dataset to predict the median house value based on factors such as location, median house age, population within a block, and median income within a block of houses. You will then evaluate the model by calculating its mean squared error.