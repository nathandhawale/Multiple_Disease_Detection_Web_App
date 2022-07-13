# Multiple_Disease_Detection_Web_App

This project contains the files for 3 of my other repositories that predict whether or not a patient
has Parkinsons, Heart disease or Diabetes.

The first is Parkinson's Disease:
The first thing I did was take a look at the data and then created a correlation heatmap to see where the data is correlated.
I then separated the train and test sets before scaling and transorming the data.
I then ran an SVM model to predict the accuracy and had a 90% on the train set and an 87% on the test set.
I then built a predictive system to determine if the code ran accurately.



I then made a diabetes prediction system:
I used a similar system as the Parkinson's with analyzing the data first the creating the training and testing sets.
I then standardized the datam then transformed it before running an SVM model to predict the accuracy.
The training set had a score 78.6% and the testing set had a score of 77.2%
I then again built a predictive system to determine the accuracy of the code.



The final model was a heart disease prediction system:
I followed similar steps as the previous 2 systems by analyzing the data and creating a correlation heatmap.
I then separated the training and testing set.
I used a logistic regression model on the data and had a training score of 85% and a testing score of 82%.
I built a predictive system to determine the accuracy of the code.



Following these 3 models. I compiled them into a python file and created a web app using streamlit to allow individuals to enter in information to determine if they or a patient is positive for Parkinsons, Diabetes, or Heart Disease.
