import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import load
import streamlit as st
from sklearn.metrics import r2_score,accuracy_score

model = load('LR.joblib')
s1 = load('item_weight.joblib')
s2 = load('price.joblib')
rf = load('RF.joblib')

st.title("Sales Prediction")

types = {
    "Baking Goods":0,
    "Breads":1,
    "Breakfast":2,
    "Canned goods":3,
    "Dairy":4,
    "Frozen Food":5,
    "Fruits & Vegetables":6,
    "Hard Drinks":7,
    "Soft Drinks":14,
    "Health & Hygiene":8,
    "Household":9,
    "Meat":10,
    "Seafood":12,
    "Snack Food":13,
    "Starchy Food":15,
    "Others":11
}

i1 = st.text_input("Item Weight", "7")


ITEM_TYPE = st.selectbox("Item Type", ["Baking Goods", "Breads","Breakfast","Canned goods","Dairy","Frozen Food","Fruits & Vegetables","Hard Drinks","Soft Drinks","Health & Hygiene","Household","Meat","Seafood","Snack Food","Starchy Food","Others"])

i2 = st.text_input("Item MRP", "7")

ITEM_CATEGORY = st.selectbox("Item category",['Food','Drinks','Non-Consumable'])
#ITEM_CATEGORY = 'Non-Consumable'


if ITEM_CATEGORY == 'Food' or ITEM_CATEGORY == 'Drinks':
    ITEM_FAT_CONTENT = st.selectbox("Item Fat Content",["Regular","Low Fat"])
else :
    ITEM_FAT_CONTENT = 'Low Fat'

OUTLET_SIZE = st.selectbox("Outlet Size",["High","Medium","Small"])

OUTLET_LOCATION_TYPE = st.selectbox("Outlet Location Type",["Tier 1","Tier 2","Tier 3"])

OUTLET_TYPE = st.selectbox("Outlet Type",["Supermarket type 1","Supermarket type 2","Supermarket type 3","Grocery Store"])


#encoding input
ITEM_WEIGHT = float(i1)
ITEM_WEIGHT = s1.transform([[ITEM_WEIGHT]])
ITEM_TYPE = types[ITEM_TYPE]
ITEM_MRP = float(i2)
ITEM_MRP = s2.transform([[ITEM_MRP]])
ITEM_FAT_CONTENT = 0 if ITEM_FAT_CONTENT=="Low Fat" else 1

if OUTLET_SIZE=="High":
    OUTLET_SIZE=0
elif OUTLET_SIZE=="Medium":
    OUTLET_SIZE=1
elif OUTLET_SIZE=="Small":
    OUTLET_SIZE=2
    

if OUTLET_LOCATION_TYPE=="Tier 1":
    OUTLET_LOCATION_TYPE=0
elif OUTLET_LOCATION_TYPE=="Tier 2":
    OUTLET_LOCATION_TYPE=1
elif OUTLET_LOCATION_TYPE=="Tier 3":
    OUTLET_LOCATION_TYPE=2
    
if OUTLET_TYPE=="Supermarket type 1":
    OUTLET_TYPE=1
elif OUTLET_TYPE=="Supermarket type 2":
    OUTLET_TYPE=2
elif OUTLET_TYPE=="Supermarket type 3":
    OUTLET_TYPE=3
elif OUTLET_TYPE=="Grocery Store":
    OUTLET_TYPE=0

if ITEM_CATEGORY == "Food":
    ITEM_CATEGORY = 1
elif ITEM_CATEGORY == 'Drinks':
    ITEM_CATEGORY = 0
else:
    ITEM_CATEGORY = 2
    
ITEM_CATEGORY_0 = 0
ITEM_CATEGORY_1 = 0
ITEM_CATEGORY_2 = 0
if ITEM_CATEGORY == 0:
    ITEM_CATEGORY_0 = 1
    ITEM_CATEGORY_1 = 0
    ITEM_CATEGORY_2 = 0
elif ITEM_CATEGORY_1 == 1:
    ITEM_CATEGORY_0 = 0
    ITEM_CATEGORY_1 = 1
    ITEM_CATEGORY_2 = 0
else:
    ITEM_CATEGORY_0 = 0
    ITEM_CATEGORY_1 = 0
    ITEM_CATEGORY_2 = 1


ITEM_FAT_CONTENT_0=0
ITEM_FAT_CONTENT_1=0
if ITEM_FAT_CONTENT==0:
    ITEM_FAT_CONTENT_0=1
    ITEM_FAT_CONTENT_1=0
else:
    ITEM_FAT_CONTENT_0=0
    ITEM_FAT_CONTENT_1=1
    

OUTLET_SIZE_0=0
OUTLET_SIZE_1=0
OUTLET_SIZE_2=0
if OUTLET_SIZE==0:
    OUTLET_SIZE_0=1
    OUTLET_SIZE_1=0
    OUTLET_SIZE_2=0
elif OUTLET_SIZE==1:
    OUTLET_SIZE_0=0
    OUTLET_SIZE_1=1
    OUTLET_SIZE_2=0
else:
    OUTLET_SIZE_0=0
    OUTLET_SIZE_1=0
    OUTLET_SIZE_2=1
    
    
OUTLET_LOCATION_TYPE_0=0
OUTLET_LOCATION_TYPE_1=0
OUTLET_LOCATION_TYPE_2=0

if OUTLET_LOCATION_TYPE==0:
    OUTLET_LOCATION_TYPE_0=1
    OUTLET_LOCATION_TYPE_1=0
    OUTLET_LOCATION_TYPE_2=0
elif OUTLET_LOCATION_TYPE==1:
    OUTLET_LOCATION_TYPE_0=0
    OUTLET_LOCATION_TYPE_1=1
    OUTLET_LOCATION_TYPE_2=0
else:
    OUTLET_LOCATION_TYPE_0=0
    OUTLET_LOCATION_TYPE_1=0
    OUTLET_LOCATION_TYPE_2=1
    
    
OUTLET_TYPE_0=0
OUTLET_TYPE_1=0
OUTLET_TYPE_2=0
OUTLET_TYPE_3=0

if OUTLET_TYPE==0:
    OUTLET_TYPE_0=1
    OUTLET_TYPE_1=0
    OUTLET_TYPE_2=0
    OUTLET_TYPE_3=0
elif OUTLET_TYPE==1:
    OUTLET_TYPE_0=0
    OUTLET_TYPE_1=1
    OUTLET_TYPE_2=0
    OUTLET_TYPE_3=0   
elif OUTLET_TYPE==2:
    OUTLET_TYPE_0=0
    OUTLET_TYPE_1=0
    OUTLET_TYPE_2=1
    OUTLET_TYPE_3=0
else:
    OUTLET_TYPE_0=0
    OUTLET_TYPE_1=0
    OUTLET_TYPE_2=0
    OUTLET_TYPE_3=1

    



input_features = [ITEM_WEIGHT[0][0],ITEM_TYPE,ITEM_MRP[0][0],
                  ITEM_FAT_CONTENT_0,ITEM_FAT_CONTENT_1,
                  OUTLET_SIZE_0,OUTLET_SIZE_1,OUTLET_SIZE_2,
                  OUTLET_LOCATION_TYPE_0,OUTLET_LOCATION_TYPE_1,OUTLET_LOCATION_TYPE_2,
                  OUTLET_TYPE_0,OUTLET_TYPE_1,OUTLET_TYPE_2,OUTLET_TYPE_3,
                  ITEM_CATEGORY_0,ITEM_CATEGORY_1,ITEM_CATEGORY_2]



#st.write(input_features)

def get_range_with_gap_of_500(number):
    lower_bound = (number // 500) * 500
    upper_bound = lower_bound + 500
    return (lower_bound, upper_bound)





if st.button("Predict"):
    # Make a prediction using the trained model
    output = model.predict([input_features])
    output2 = rf.predict([input_features])
    # Display the prediction result
    st.subheader("Prediction Result by Linear Regression :")
    result = get_range_with_gap_of_500(output[0])
    st.write(output[0])
   
    st.subheader("Prediction Result by Random Forest Regression :")
    st.write(output2[0])
    
    st.write(f"Range : {result[0]} to {result[1]}")
    