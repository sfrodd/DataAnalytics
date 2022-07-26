import pandas as pd
import numpy as np

def addNewFeature(msg):
    a,b=7,9
    if(a>b):
        print('A Bigger'+msg)
    else:
        print('B Gigger'+msg)


if __name__ == '__main__':
   dict_A={
       'Name':['Ajay',np.nan,'Kiran','Vijay','Sharada'],
       'Age':[19,np.nan,21,22,np.nan],
       'Sem':[3,5,np.nan,4,3]
   }
   addNewFeature("Hello")
   df=pd.DataFrame(dict_A)
   print(df.isnull().sum())
   values={'Name':'Bishnoi','Age':20,'Sem':4}
   df.fillna(values,inplace=True)
   df.replace(to_replace=np.nan,value=20,inplace=True)
   df.interpolate(method='linear',limit_direction='forward',inplace=True)
   print("Hello World")
   print(df)
