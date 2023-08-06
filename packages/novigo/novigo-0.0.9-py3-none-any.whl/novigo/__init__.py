# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:41:37 2018

@author: kmy07
"""
name = "novigo"
import os

print(os.getcwd())

def predictSalary():
    import pickle
    import numpy as np
    import os
    import pkg_resources
    resource_package = 'novigo'
    path = '/'.join(('models','trained_model.sav'))
    file = pkg_resources.resource_string(resource_package,path)
    loaded_model = pickle.load(open(file,'rb'))
    experience = int(input("Enter the Experience in years to predict the salary:\t"))
    print("The salary for the specified experience will be:%10d" % loaded_model.predict(np.array([[experience]])))
