import collections
import joblib
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer

def SVMLoad(inputList):
    SVMClassifier = joblib.load("SVM_Classifier.joblib")
    predicted_number = np.array_str(SVMClassifier.predict(preprocessing.normalize(inputList)))
#change the predicted number into human readable grade classification
    if predicted_number == '[1]':
        predicted_grade = "Your predicted CGPA next sem is 2.0 and below.\n Please pay more effort as you will fail the upcoming semester"
    elif predicted_number == '[2]':
        predicted_grade = "Your predicted CGPA next sem is 2.00 - 2.75.\n Your CGPA can be better, GAMBATEH "
    elif predicted_number == '[3]':
        predicted_grade = "Your predicted CGPA next sem is 2.75 - 3.75.\n Well done, let's aim for a higher CGPA"       
    elif predicted_number == '[4]':
        predicted_grade = "Your predicted CGPA next sem is 3.75 and above.\n Excellent! please keep it up"       
    else: 
        predicted_grade = "something wrong"
        
    return predicted_grade
    
def RFLoad(inputList):
    RFClassifier = joblib.load("RF_Classifier.joblib")
    predicted_number = np.array_str(RFClassifier.predict(preprocessing.normalize(inputList)))
    
#change the predicted number into human readable grade classification
    if predicted_number == '[1]':
        predicted_grade = "Your predicted CGPA next sem is 2.0 and below.\n Please pay more effort as you will fail the upcoming semester"
    elif predicted_number == '[2]':
        predicted_grade = "Your predicted CGPA next sem is 2.00 - 2.75.\n Your CGPA can be better, GAMBATEH "
    elif predicted_number == '[3]':
        predicted_grade = "Your predicted CGPA next sem is 2.75 - 3.75.\n Well done, let's aim for a higher CGPA"       
    elif predicted_number == '[4]':
        predicted_grade = "Your predicted CGPA next sem is 3.75 and above.\n Excellent! please keep it up"       
    else: 
        predicted_grade = "something wrong"
        
    return predicted_grade


