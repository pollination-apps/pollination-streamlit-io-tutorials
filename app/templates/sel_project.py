import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user

api_client = get_api_client()

user = auth_user('auth-user', api_client)

if user and 'username' in user:
    st.subheader('Hi ' + user['username'] + ', select a project:')

    pcol1, pcol2 = st.columns(2)

    with pcol1:
        project = select_project(
            'select-project',
            api_client,
            project_owner=user['username']
        )
    with pcol2:
        st.json(project or '{}', expanded=False)