"""Download files from Pollination jobs aka studies."""
import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import (select_account, 
                                      select_cloud_artifact, 
                                      select_project, 
                                      select_study)

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

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
        # get project name
        project_name = project.get('name')
        st.subheader('Select a study:')

        scol1, scol2 = st.columns(2)

        with scol1:
            study = select_study(
                'select-study',
                api_client,
                project_name=project_name,
                project_owner=project_owner
            )
        with scol2:
            st.json(study or '{}', expanded=False)

        if study:
            study_id = study.get('id')
            st.subheader('Select an artifact:')
            st.info('It returns the name of the file \
                    and the binary data to save.')

            acol1, acol2 = st.columns(2)

            with acol1:
                artifact = select_cloud_artifact(
                    'sel-artifact',
                    api_client,
                    project_name=project_name,
                    project_owner=project_owner,
                    study_id=study_id,
                    file_name_match=".*"
                )
            with acol2:
                st.json(artifact or {}, expanded=False)