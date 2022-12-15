import numpy as np
import sklearn as sk
from sklearn.metrics import confusion_matrix
from numpy import genfromtxt

df = np.genfromtxt("C:/Koulu (Tietotekniikka)/arduinodata", delimiter=',')

y_true = df[:,1]
y_pred = df[:,0]


print(confusion_matrix(y_true, y_pred))