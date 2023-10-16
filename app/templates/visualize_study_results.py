import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import create_study
from pollination_streamlit_viewer import viewer

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

study = create_study(key='my-study-results', 
    api_client=api_client)
name, value, type = study.progress_report(refresh_interval=300, 
                      show_status_label=True,
                      color='#eb2126',
                      show_output=True)

if study and study.progress == 100:
    st.info('Click on visualization card.')
    if name and name.endswith('vtkjs'):
        viewer(key='my-vsf', content=value)
