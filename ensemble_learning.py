# -*- coding: utf-8 -*-
"""ensemble_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_fRks5B_Of4m35scnD7Wl35cVMz22tiB
"""

# Name : Sujeeth Sundarajan Rajkumar
# UTA ID : 1002153693

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris


def ensemble_learning(X, y, task='classification'):
    """
    Implement ensemble learning methods: Decision Trees, Bagging, Random Forest, and Boosting.

    Parameters:
    - X: Input features (numpy array or pandas DataFrame)
    - y: Target variable (numpy array or pandas Series)
    - task: Type of task, either 'classification' or 'regression' (default: 'classification')

    Returns:
    - results: Dictionary containing evaluation results for each ensemble method
    """
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize results dictionary
    results = {}

    # Decision Tree
    dt_classifier = DecisionTreeClassifier()
    # Train the Decision Tree classifier on the training data
    # Your code here
    dt_classifier.fit(X_train, y_train)  # Train
    # Predict the labels for the testing data
    # Your code here
    dt_predictions = dt_classifier.predict(X_test)  # Predict

    # Calculate the accuracy of the Decision Tree classifier
    # Your code here
    dt_accuracy = accuracy_score(y_test, dt_predictions)  # Calculate accuracy

    # Store the accuracy in the results dictionary
    # Your code here
    results['Decision Tree'] = dt_accuracy  # Store accuracy

    # Bagging
    bagging_classifier = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=2, random_state=42)
    # Train the Bagging classifier on the training data
    # Your code here
    bagging_classifier.fit(X_train, y_train)  # Train

    # Predict the labels for the testing data
    # Your code here
    bagging_predictions = bagging_classifier.predict(X_test)  # Predict

    # Calculate the accuracy of the Bagging classifier
    # Your code here
    bagging_accuracy = accuracy_score(y_test, bagging_predictions)  # Calculate accuracy

    # Store the accuracy in the results dictionary
    # Your code here
    results['Bagging'] = bagging_accuracy  # Store accuracy

    # Random Forest
    rf_classifier = RandomForestClassifier(n_estimators=2, random_state=42)
    # Train the Random Forest classifier on the training data
    # Your code here
    rf_classifier.fit(X_train, y_train)  # Train

    # Predict the labels for the testing data
    # Your code here
    rf_predictions = rf_classifier.predict(X_test)  # Predict

    # Calculate the accuracy of the Random Forest classifier
    # Your code here
    rf_accuracy = accuracy_score(y_test, rf_predictions)  # Calculate accuracy

    # Store the accuracy in the results dictionary
    # Your code here
    results['Random Forest'] = rf_accuracy  # Store accuracy

    # Boosting
    if task == 'classification':
        boosting_classifier = AdaBoostClassifier(estimator=DecisionTreeClassifier(), n_estimators=2, random_state=42)
    else:
        # For regression tasks, you can use GradientBoostingRegressor instead
        pass
    # Train the Boosting classifier on the training data
    # Your code here
        boosting_classifier.fit(X_train, y_train)

    # Predict the labels for the testing data
    # Your code here
        boosting_predictions = boosting_classifier.predict(X_test)

    # Calculate the accuracy of the Boosting classifier
    # Your code here
        boosting_accuracy = accuracy_score(y_test, boosting_predictions)

    # Store the accuracy in the results dictionary
    # Your code here
        results['Boosting'] = boosting_accuracy

    return results

# Example usage:
iris = load_iris()
X = iris.data
y = iris.target
results = ensemble_learning(X, y, task='classification')
print(results)