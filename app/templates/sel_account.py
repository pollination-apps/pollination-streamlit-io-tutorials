import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import select_account

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

st.header("Select Account")

account = select_account('select-account', api_client)
if account:
    st.json(account, expanded=False)