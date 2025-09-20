import streamlit as st
import pickle
import pandas as pd


ridge_model = pickle.load(open('RidgeModel.pkl', 'rb'))
data = pickle.load(open('meta_data.pkl', 'rb'))


st.title('Banglore House Price Prediction')
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox('Please select the location',data['location'])
with col2:
    bhk = st.selectbox('Please select the bhk',data['bhk'])

col3, col4 = st.columns(2)

with col3:
    bath = st.selectbox('Please select the number of bath',sorted(set(int(x) for x in data['bath'])))
with col4:
    sqft = st.number_input('Please select the input', min_value = 100, step = 10)

if st.button('Predict the Price'):
    input_df = pd.DataFrame([{
        'location': location,
        'total_sqft': sqft,
        'bath': bath,
        'bhk': bhk
    }])
    prediction = ridge_model.predict(input_df)[0]
    st.success(f'Predicted Price is ₹ {prediction:,.2f} Lakhs')

