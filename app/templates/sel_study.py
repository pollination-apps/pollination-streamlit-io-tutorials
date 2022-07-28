import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user, select_account

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
    
    if project and 'name' in project:
        st.subheader('Select a study:')

        scol1, scol2 = st.columns(2)

        with scol1:
            study = select_study(
                'select-study',
                api_client,
                project_name=project['name'],
                project_owner=user['username']
            )
        with scol2:
            st.json(study or '{}', expanded=False)