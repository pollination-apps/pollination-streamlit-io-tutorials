import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit.api.recipes import RecipesAPI
from pollination_streamlit_io import (select_account, recipe_inputs_form,
                                      select_project)

st.info('This app submits cumulative radiation studies and shows \
        the progress of the study and its results.')

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
        project_name = project.get('name')

        # set recipe name and recipe filter
        recipe_name = 'cumulative-radiation'
        recipe_filter = {'owner': 'ladybug-tools', 
                         'name': f'{recipe_name}-*', 
                         'tag': '*'}

        # add the recipe you want to a project
        recipe_api.add_to_project(owner=recipe_filter.get('owner'), 
                                name=recipe_name, 
                                project_slug=f'{project_owner}/{project_name}')

        st.info('A user input is an input which is passed \
                directly to recipe form. It can come from \
                the app itself.')
        enable_controlled = st.checkbox('User input?')
        show_form = st.checkbox('Show form?', value=True)

        if enable_controlled:
            controlled_values = {
            'wea': ['resources/ITA_Campobasso.162520_IGDG.wea', 
                    'my_wea.wea'],
            'model': ['resources/model.hbjson', 
                    'my_model.wea']
            }
        else:
            controlled_values = None

        study = recipe_inputs_form(key='st-study', 
                                api_client=api_client, 
                                project_name=project_name,
                                project_owner=project_owner,
                                recipe_filter=recipe_filter,
                                user_inputs=controlled_values,
                                study_name='my study',
                                is_local=True,
                                show_form=show_form)

        study.progress_report(refresh_interval=300, 
                              show_output=True)