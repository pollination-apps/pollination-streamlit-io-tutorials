import streamlit as st
from pollination_streamlit.selectors import get_api_client
from pollination_streamlit_io import create_study

api_client = get_api_client()

study = create_study(key='my-pollination-study', 
    api_client=api_client)