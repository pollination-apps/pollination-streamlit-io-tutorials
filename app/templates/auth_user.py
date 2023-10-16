import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user

# get api_client from pollination
api_client = get_api_client()

st.header("Authenticated User")

user = auth_user('auth-user', api_client)
if user is not None:
    st.json(user, expanded=False)