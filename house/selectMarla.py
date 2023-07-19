# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:26:56 2022

@author: Amjid_Khan_Mohmand
"""
# import numpy as np
import matplotlib.pyplot as plt
# from scipy import signal
import pandas as pd
# from sklearn.decomposition import FastICA, PCA
# from biosppy import storage
# from biosppy.signals import ecg
# import os.path
import sys
from datetime import date
def RunAlgo(location,marla):
    df=pd.read_csv('fbP_forecasted_data.csv')
    dfX=df[['ds','location','Area_Marla','bedrooms','bathrooms','yhat']]
    dfX=dfX.rename(columns={"yhat":"price"})
    dfX=dfX[dfX['price']>0]
    dfX=dfX[dfX['location']==location]
    dfX=dfX[dfX['Area_Marla']==marla]
    
     
    
    bedrooms=list(dfX.bedrooms.unique())
    
    print("<br><br>")
    print('<label for="bed">Bedrooms:</label>')
    print("<select id='bed'>")
    print("<option value=''>Select No of Bedrooms</option>")
    for bedroom in bedrooms:
        print(f"<option value='{bedroom}'>{bedroom}</option>")
  
    print("</select>")

    

locat=str(sys.argv[1])
locat=locat.split("@")
locat1=locat[0].split(",")
locat1=locat1[0]+", "+locat1[1]
  
RunAlgo(locat1,float(locat[1]))