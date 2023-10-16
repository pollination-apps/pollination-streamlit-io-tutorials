import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import (select_account, select_account,
                                      select_project, select_study, 
                                      select_run)
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
            st.subheader(f'Select a run for study {study_id}:')

            runcol1, runcol2 = st.columns(2)

            with runcol1:
                run = select_run(
                    'select-run',
                    api_client,
                    project_name=project_name,
                    project_owner=project_owner,
                    job_id=study_id
                )

            with runcol2:
                st.json(run or '{}', expanded=False)