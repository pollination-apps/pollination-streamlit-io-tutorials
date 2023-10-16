import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import select_account

# get api_client from pollination
api_client = get_api_client()

st.header("Select Account")

account = select_account('select-account', api_client) or ''
if account is not None:
    st.json(account, expanded=False)