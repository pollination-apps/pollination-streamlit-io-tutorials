import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

st.header("Authenticated User")

user = auth_user('auth-user', api_client)
if user is not None:
    st.json(user, expanded=False)