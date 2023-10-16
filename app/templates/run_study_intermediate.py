import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit.api.recipes import RecipesAPI
from pollination_streamlit_io import (select_account, recipe_inputs_form,
                                      select_project, select_recipe)

st.info('This app submits studies by using recipe_inputs_form component.')

# get api_client from pollination
api_client = get_api_client()
# create a recipe api client
recipe_api = RecipesAPI(api_client)

account = select_account('select-account', api_client)

if account:
    # if it is an organization it uses account_name otherwise username
    project_owner = account.get('username') or account.get('account_name')
    st.subheader(f'Hi {project_owner}! Select a project:')

    pcol1, pcol2 = st.columns(2)

    with pcol1:
        project = select_project(
            'select-project',
            api_client,
            project_owner=project_owner
        )
    with pcol2:
        st.json(project or '{}', expanded=False)

    if project:
        # get the project name
        project_name = project.get('name')
        st.subheader(f'Selected {project_name}, select a recipe:')

        rcol1, rcol2 = st.columns(2)

        with rcol1:
            recipe = select_recipe(
                'select-recipe',
                api_client,
                project_name=project['name'],
                project_owner=project_owner
            )
        with rcol2:
            st.json(recipe or '{}', expanded=False)

        if recipe:
            study = recipe_inputs_form(key='st-study', 
                                       api_client=api_client, 
                                       recipe_filter=recipe,
                                       project_name=project_name,
                                       project_owner=project_owner,
                                       study_name='my study')