import streamlit as st
from pollination_streamlit_io import get_hbjson

model = get_hbjson(key='my-model')
if model:
    st.json(model, expanded=False)