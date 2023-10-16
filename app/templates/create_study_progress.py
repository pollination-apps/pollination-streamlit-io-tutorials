import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import create_study

# in this tutorial, the api_client is taken from app.py
# typically you would create the api_client as shown below
# api_client = get_api_client()

study = create_study(key='my-study-progress', 
    api_client=api_client)
study.progress_report(refresh_interval=300, 
                      show_status_label=True,
                      color='#eb2126',
                      show_output=True)