# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:44:30 2022

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
def RunAlgo(location):
    df=pd.read_csv('fbP_forecasted_data.csv')
    dfX=df[['ds','location','Area_Marla','bedrooms','bathrooms','yhat']]
    dfX=dfX.rename(columns={"yhat":"price"})
    dfX=dfX[dfX['price']>0]
    dfX=dfX[dfX['location']==location]
    marlas=list(dfX.Area_Marla.unique())
    
    print("<br></br>")
    print('<label for="sq">Area in Marlas:</label>')
    print("<select id='sq' onchange='selectMarla();'>")
    print("<option value=''>Select Marlas</option>")
    for marla in marlas:
        print(f"<option value='{marla}'>{marla}</option>")
        
    print("</select>")
    
    print('<div id="show3">')
    print("<br><br>")
    print('<label for="bed">Bedrooms:</label>')
    print("<select id='bed'>")
    print("<option value=''>Select No of Bedrooms</option>")
    print("</select>")
    print("</div>")
    

locat=str(sys.argv[1])
locat=locat.split(",")
locat=locat[0]+", "+locat[1]
#print(locat)   
RunAlgo(locat)