import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user, select_account

api_client = get_api_client()

st.header("Authenticated User")

acol1, acol2 = st.columns(2)

with acol1:
    user = auth_user('auth-user', api_client)
    if user is not None:
        st.json(user, expanded=False)

with acol2:
    account = select_account('select-account', api_client) or ''
    if account is not None and 'username' in account:
        st.json(account, expanded=False)