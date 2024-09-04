The last machine learning model we'll cover is random forests. You already know more about this model than you think since a random forest is just a collection of decision trees! Random forests work by building multiple decision trees during training and then merging their results to output a single value which helps improve its accuracy.

Like our previous models, we'll import it from `sklearn` and then define it.
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
```

As with our previous challenges, to get the flag you'll need to define a random forest model, train it on the iris dataset, make predictions on the test dataset, and then compare your model against the test dataset by getting the accuracy of the model.