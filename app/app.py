import pathlib

from enum import Enum

import streamlit as st
from streamlit_ace import st_ace, THEMES

from pollination_streamlit_io import ( 
    get_geometry, 
    send_geometry, 
    get_hbjson, 
    send_hbjson,
    auth_user,
    select_account, 
    select_project, 
    select_recipe, 
    select_run, 
    select_study, 
    select_cloud_artifact, 
    create_study,
    recipe_inputs_form,
    send_results )

# needed for get_and_show_model.py
import requests

# needed for get_and_show_model.py
import json
from honeybee.model import Model as HBModel
from honeybee_vtk.model import Model as VTKModel
from pollination_streamlit_viewer import viewer

st.set_page_config(
    page_title='Tutorial App',
    page_icon='https://app.pollination.cloud/favicon.ico',
    initial_sidebar_state='collapsed',
)

from pollination_streamlit.selectors import get_api_client

# needed for get_and_show_model.py
# set_page_config needs to be called prior to this import
from templates.get_show_model import create_vtkjs, show_model

st.sidebar.image(
    'https://uploads-ssl.webflow.com/6035339e9bb6445b8e5f77d7/616da00b76225ec0e4d975ba'
    '_pollination_brandmark-p-500.png',
    use_column_width=True
)

# get api_client from pollination
api_client = get_api_client()

TEMPLATES = './templates'

class Command(Enum):
    GET_MODEL = 'Get Model'
    SEND_MODEL = 'Send Model'
    SEND_MODEL_FROM_HB = 'Send Model From HB'
    GET_GEOMETRY = 'Get Geometry'
    SEND_GEOMETRY = 'Send Geometry'
    SEND_GEOMETRY_FROM_LB = 'Send Geometry From LB'
    SEND_GEOMETRY_FROM_DICT = 'Send Geometry From Dict'
    SEND_RESULTS = 'Send Results'
    AUTH_USER = 'Authenticated User'
    SEL_ACCOUNT = 'Select Account'
    SEL_PROJECT = 'Select Project'
    SEL_RECIPE = 'Select Recipe'
    SEL_STUDY = 'Select Study'
    SEL_RUN = 'Select Run'
    RUN_STUDY_BASIC = 'Create Study'
    RUN_STUDY_PROGRESS = 'Study Progress'
    RUN_STUDY_INTERMEDIATE = 'Create Study by Recipe Form'
    RUN_STUDY_ADVANCED = 'Create Study by Recipe Form (Advanced)'
    DOWNLOAD_ARTIFACT = 'Select and Download an Artifact'
    GET_SHOW_RESULTS = 'Get and Show a Study Result (VSF)'
    GET_SHOW_MODEL = 'Get and Show a Hbjson Model'

SCRIPTS = {
    Command.GET_MODEL.value: pathlib.Path(TEMPLATES)
        .joinpath('get_model.py').read_text(),
    Command.SEND_MODEL_FROM_HB.value: pathlib.Path(TEMPLATES)
        .joinpath('send_model_from_hb.py').read_text(),
    Command.SEND_MODEL.value: pathlib.Path(TEMPLATES)
        .joinpath('send_model.py').read_text(),
    Command.GET_GEOMETRY.value: pathlib.Path(TEMPLATES)
        .joinpath('get_geometry.py').read_text(),
    Command.SEND_GEOMETRY.value: pathlib.Path(TEMPLATES)
        .joinpath('send_geometry.py').read_text(),
    Command.SEND_GEOMETRY_FROM_LB.value: pathlib.Path(TEMPLATES)
        .joinpath('send_geometry_from_lb.py').read_text(),
    Command.SEND_GEOMETRY_FROM_DICT.value: pathlib.Path(TEMPLATES)
        .joinpath('send_geometry_from_dict.py').read_text(),
    Command.SEND_RESULTS.value: pathlib.Path(TEMPLATES)
        .joinpath('send_results.py').read_text(),
    Command.AUTH_USER.value: pathlib.Path(TEMPLATES)
        .joinpath('auth_user.py').read_text(),
    Command.SEL_ACCOUNT.value: pathlib.Path(TEMPLATES)
        .joinpath('sel_account.py').read_text(),
    Command.SEL_PROJECT.value: pathlib.Path(TEMPLATES)
        .joinpath('sel_project.py').read_text(),
    Command.SEL_RECIPE.value: pathlib.Path(TEMPLATES)
        .joinpath('sel_recipe.py').read_text(),
    Command.SEL_STUDY.value: pathlib.Path(TEMPLATES)
        .joinpath('sel_study.py').read_text(),
    Command.SEL_RUN.value: pathlib.Path(TEMPLATES)
        .joinpath('sel_run.py').read_text(),
    Command.RUN_STUDY_BASIC.value: pathlib.Path(TEMPLATES)
        .joinpath('run_study_basic.py').read_text(),
    Command.RUN_STUDY_PROGRESS.value: pathlib.Path(TEMPLATES)
        .joinpath('create_study_progress.py').read_text(),
    Command.RUN_STUDY_INTERMEDIATE.value: pathlib.Path(TEMPLATES)
        .joinpath('run_study_intermediate.py').read_text(),
    Command.RUN_STUDY_ADVANCED.value: pathlib.Path(TEMPLATES)
        .joinpath('run_study_advanced.py').read_text(),
    Command.DOWNLOAD_ARTIFACT.value: pathlib.Path(TEMPLATES)
        .joinpath('download_artifact.py').read_text(),
    Command.GET_SHOW_RESULTS.value: pathlib.Path(TEMPLATES)
        .joinpath('visualize_study_results.py').read_text(),
    Command.GET_SHOW_MODEL.value: pathlib.Path(TEMPLATES)
        .joinpath('get_show_model.py').read_text()
}

DOCS = {
    Command.GET_MODEL.value: get_hbjson.__doc__,
    Command.SEND_MODEL.value: send_hbjson.__doc__,
    Command.SEND_MODEL_FROM_HB.value: send_hbjson.__doc__,
    Command.GET_GEOMETRY.value: get_geometry.__doc__,
    Command.SEND_GEOMETRY.value: send_geometry.__doc__,
    Command.SEND_GEOMETRY_FROM_LB.value: get_geometry.__doc__,
    Command.SEND_GEOMETRY_FROM_DICT.value: send_geometry.__doc__,
    Command.SEND_RESULTS.value: send_results.__doc__,
    Command.AUTH_USER.value: auth_user.__doc__,
    Command.SEL_ACCOUNT.value: select_account.__doc__,
    Command.SEL_PROJECT.value: select_project.__doc__,
    Command.SEL_RECIPE.value: select_recipe.__doc__,
    Command.SEL_STUDY.value: select_study.__doc__,
    Command.RUN_STUDY_BASIC.value: create_study.__doc__,
    Command.RUN_STUDY_PROGRESS.value: create_study.__doc__,
    Command.RUN_STUDY_INTERMEDIATE.value: recipe_inputs_form.__doc__,
    Command.RUN_STUDY_ADVANCED.value: recipe_inputs_form.__doc__,
    Command.SEL_RUN.value: select_run.__doc__,
    Command.DOWNLOAD_ARTIFACT.value: select_cloud_artifact.__doc__,
    Command.GET_SHOW_RESULTS.value: viewer.__doc__,
    Command.GET_SHOW_MODEL.value: viewer.__doc__
}

def main():
    """Learning doing."""

    # title
    st.header('Select a tutorial!')

    # set tabs
    tab1, tab2, tab3 = st.tabs(["CAD Interactions", "Cloud Interactions", "Pollination Viewer"])

    # sidebar
    st.sidebar.markdown('## Editor Settings')
    st.sidebar.markdown('----------')
    auto_update = st.sidebar.checkbox(label='Auto update',
        value=True)
    font_size = st.sidebar.number_input(label='Font size',
        value=15, min_value=1, max_value=30)
    theme = st.sidebar.selectbox(
        label='Select a theme', options=THEMES, index=5)

    # tabs layout
    with tab1:
        mod_option = st.selectbox(
            'Select a script to test',
            (Command.SEND_MODEL.value, 
            Command.SEND_MODEL_FROM_HB.value, 
            Command.GET_MODEL.value,
            Command.SEND_GEOMETRY.value, 
            Command.SEND_GEOMETRY_FROM_LB.value, 
            Command.SEND_GEOMETRY_FROM_DICT.value, 
            Command.GET_GEOMETRY.value,
            Command.SEND_RESULTS.value))
        with st.expander(label='Docs', expanded=False):
            st.markdown(DOCS[mod_option])
        mod_script = st_ace(language="python", 
            value=SCRIPTS[mod_option], 
            auto_update=auto_update,
            font_size=font_size,
            theme=theme)
        exec(mod_script)

    with tab2:
        sel_option = st.selectbox(
            'Select a script to test',
            (Command.AUTH_USER.value,
            Command.SEL_ACCOUNT.value, 
            Command.SEL_PROJECT.value,
            Command.SEL_RECIPE.value,
            Command.SEL_STUDY.value,
            Command.SEL_RUN.value,
            Command.RUN_STUDY_BASIC.value,
            Command.RUN_STUDY_PROGRESS.value,
            Command.DOWNLOAD_ARTIFACT.value,
            Command.RUN_STUDY_INTERMEDIATE.value,
            Command.RUN_STUDY_ADVANCED.value))
        with st.expander(label='Docs', expanded=False):
            st.markdown(DOCS[sel_option])
        sel_script = st_ace(language="python", 
            value=SCRIPTS[sel_option], 
            auto_update=auto_update,
            font_size=font_size,
            theme=theme)
        exec(sel_script)
    
    with tab3:
        viewer_option = st.selectbox(
            'Select a script to test',
            ([Command.GET_SHOW_RESULTS.value, \
              Command.GET_SHOW_MODEL.value]))
        with st.expander(label='Docs', expanded=False):
            st.markdown(DOCS[viewer_option])
        viewer_script = st_ace(language="python", 
            value=SCRIPTS[viewer_option], 
            auto_update=auto_update,
            font_size=font_size,
            theme=theme)
        exec(viewer_script)
        
if __name__ == '__main__':
    main()
