import requests
import streamlit as st
import pandas as pd

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    div[data-testid="stToolbar"] {display: none;}
    div[data-testid="stDecoration"] {display: none;}
    div[data-testid="stStatusWidget"] {display: none;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🌙" if st.get_option("theme.base") == "light" else "☀️", use_container_width=True):
        if st.get_option("theme.base") == "light":
            st._config.set_option("theme.base", "dark")
        else:
            st._config.set_option("theme.base", "light")
        st.rerun()

st.title("Antifraud service")
with st.form("check fraud transactions"):
    card_numb = st.text_input(
    "Your card number",
    placeholder="Write your card number"
    )
    
#    date_trans = st.date_input("Date of transaction")
    submit = st.form_submit_button("Check probability")

if card_numb and card_numb.isdigit():
    card_numb = int(card_numb)
    if submit:
        response = requests.post('http://127.0.0.1:8000/score', json={"card_num": card_numb})
    #    st.write(response.json())
        data = response.json()
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame([data])
        
        column_mapping = {
            'TransactionID': 'TransactionID',
            'TransactionAmt': 'TransactionAmt',
            'isFraud': 'isFraud',
            'TransactionDate': 'TransactionDate',
            'TranscationTime': 'TransactionTime',
            'TransactionTime': 'TransactionTime'
        }
        
        df = df.rename(columns=column_mapping)
        if df.empty:
            st.error("Wrong card number")
        else:
            st.dataframe(df, use_container_width=True)
else:
    st.error("Wrong card number")

