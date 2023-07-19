# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 14:57:42 2022

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


def RunAlgo():
    df=pd.read_csv('fbP_forecasted_data.csv')
    dfX=df[['ds','location','Area_Marla','bedrooms','bathrooms','yhat']]
    dfX=dfX.rename(columns={"yhat":"price"})
    dfX=dfX[dfX['price']>0]
    locs=list(dfX.location.unique())
 
    print("<label for='loc'>Property Location:</label>")
    print("<select id='loc' onchange='selectLocation();'> ")
    print("<option value=''>Select a location</option>")
    for lc in locs:

        print(f"<option value='{lc}'>{lc}</option>")
    print("</select>")
    
    print('<div id="show2">')
    print("<br></br>")
    print('<label for="sq">Area in Marlas:</label>')
    print("<select id='sq'>")
    print("<option value=''>Select Marlas</option>")
    print("</select>")
    
    print('<div id="show3">')
    print("<br><br>")
    print('<label for="bed">Bedrooms:</label>')
    print("<select id='bed'>")
    print("<option value=''>Select No of Bedrooms</option>")
    print("</select>")
    print("</div>")
    
    print("</div>")
    
    print('<br><br><label for="ye">Date:</label><input type="date" name="ye" id="ye" placeholder="2021-2023" required >')



RunAlgo()
    

    
    
    
    
    
    


