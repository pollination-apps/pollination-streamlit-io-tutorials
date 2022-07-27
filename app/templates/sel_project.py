import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user, select_account

api_client = get_api_client()

st.header("Authenticated User")

acol1, acol2 = st.columns(2)

with acol1:
    user = auth_user('auth-user', api_client)
    if user is not None:
        st.json(user)

with acol2:
    account = select_account('select-account', api_client) or ''

if account and 'name' in account:
    st.subheader('Hi ' + account['name'] + ', select a project:')
    owner = None
    if 'username' in account:
        owner = account['username']
    elif 'account_name' in account:
        owner = account['account_name']

    pcol1, pcol2 = st.columns(2)

    with pcol1:
        project = select_project(
            'select-project',
            api_client,
            project_owner=owner
        )
    with pcol2:
        st.json(project or '{}', expanded=False)