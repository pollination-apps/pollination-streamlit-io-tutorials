import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import auth_user, select_project

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

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
        st.subheader('Selected ' + project['name'] + ', select a recipe:')

        rcol1, rcol2 = st.columns(2)

        with rcol1:
            recipe = select_recipe(
                'select-recipe',
                api_client,
                project_name=project['name'],
                project_owner=user['username']
            )
        with rcol2:
            st.json(recipe or '{}', expanded=False)