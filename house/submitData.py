# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:24:45 2022

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
def RunAlgo(location,marla,bed,dat):
    df=pd.read_csv('fbP_forecasted_data.csv')
    dfX=df[['ds','location','Area_Marla','bedrooms','bathrooms','yhat']]
    dfX=dfX.rename(columns={"yhat":"price"})
    dfX=dfX[dfX['price']>0]
    dfX=dfX[dfX['location']==location]
    dfX=dfX[dfX['Area_Marla']==marla]
    dfX=dfX[dfX['bedrooms']==bed]
    
    dfXN=dfX
    dfX=dfX[dfX['ds']==dat]
    lst_pr=list(dfX['price'])
    pr=0
   
   
    if(len(lst_pr)>0):
        
        pr=lst_pr[0]

    
    if(pr>0):
        print(f"<b>Results</b>")
        print("<table style='width: 80%;border-collapse: collapse;' align='center' border='1'>")
        print("<tr>")
        print("<th>Date</th>")
        print("<th>Location</th>")
        print("<th>Bedrooms</th>")
        print("<th>Bathrooms</th>")
        print("<th>Area in Marlas</th>")
        print("<th>Price</th>")
        
        print("</tr>")
        
        print("<tr>")
        
        print(f"<td>{dfX.iloc[0]['ds']}</td>")
        print(f"<td>{dfX.iloc[0]['location']}</td>")
        print(f"<td>{dfX.iloc[0]['bedrooms']}</td>")
        print(f"<td>{dfX.iloc[0]['bathrooms']}</td>")
        print(f"<td>{dfX.iloc[0]['Area_Marla']}</td>")
        print(f"<td>{dfX.iloc[0]['price']}</td>")
        
        print("</tr>")
        
        print("</table>")
    else:
        print(f"<b>No data available for the given date but here is some relevent info</b>")
        print("<table style='width: 80%;border-collapse: collapse;' align='center' border='1'>")
       
        print("<tr>")
        print("<th>Date</th>")
        print("<th>Location</th>")
        print("<th>Bedrooms</th>")
        print("<th>Bathrooms</th>")
        print("<th>Area in Marlas</th>")
        print("<th>Price</th>")
        
        print("</tr>")
        
        for i in range(len(dfXN['ds'])):
            
            print("<tr>")
            
            print(f"<td>{dfXN.iloc[i]['ds']}</td>")
            print(f"<td>{dfXN.iloc[i]['location']}</td>")
            print(f"<td>{dfXN.iloc[i]['bedrooms']}</td>")
            print(f"<td>{dfXN.iloc[i]['bathrooms']}</td>")
            print(f"<td>{dfXN.iloc[i]['Area_Marla']}</td>")
            print(f"<td>{dfXN.iloc[i]['price']}</td>")
            
            print("</tr>")
        
        
        print("</table>")
        
   

    

locat=str(sys.argv[1])
locat=locat.split("@")
locat1=locat[0].split(",")
locat1=locat1[0]+", "+locat1[1]

marla=float(locat[1])
bed=float(locat[2])
dat=str(locat[3])

RunAlgo(locat1,marla,bed,dat)