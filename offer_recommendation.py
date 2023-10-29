import numpy as np
import pandas as pd
from joblib import load
import streamlit as st
import random

model = load('KMEANS.joblib')

offer0 = pd.read_csv('offer.csv')
offer1 = pd.read_csv('offer1.csv')
offer2 = pd.read_csv('offer2.csv')
offer3 = pd.read_csv('offer3.csv')
offer4 = pd.read_csv('offer4.csv')

def convert_inr_to_usd(amount_inr):
    exchange_rate = 0.012  
    amount_usd = amount_inr * exchange_rate * 0.001
    return amount_usd

segment_detail = {
    1 : "Average in terms of earning and spending ",
    2 : "Earning high and also spending high [TARGET SET]",
    3 : "Earning high but spending less",
    4 : "Earning less , spending less",
    5 : "Earning less but spending more"
}

def get_seg_detail(segment):
    seg_det = segment_detail[segment]
    return seg_det

st.title('Offer Recommender App')

gross_income = st.text_input("Gross income of customer(Rs.) ",'1200000')

income = float(gross_income)

income = convert_inr_to_usd(income)

st.write("income : ",income)

score = st.text_input("Spending score(0-100)",'32')

spending_score = float(score)

input_features = [[income,spending_score]]




def get_random_rows(df, num_rows=10):

    random_rows = df.sample(n=num_rows)
    return random_rows



def get_seg(input_features):
    segment = model.predict(input_features)
    segment = segment[0]
    return segment

segment= int(get_seg(input_features))

if st.button("Predict Segment"):
    seg_det = get_seg_detail(segment)
    st.write("Segment : ",segment)
    st.write("Customer is likely to be  ", seg_det)
    
    
# Button to trigger offer recommendation
if st.sidebar.button('Recommend Offers'):
    df = offer0
    if segment == 0:
        df = offer0
    elif segment == 1:
        df = offer1
    elif segment == 2:
        df = offer2
    elif segment == 3:
        df = offer3
    elif segment == 4:
        df = offer4
    
    recommended_offers = get_random_rows(df,10)
    st.subheader(f'Recommended offers for Segment {segment}:')
    st.write(recommended_offers)