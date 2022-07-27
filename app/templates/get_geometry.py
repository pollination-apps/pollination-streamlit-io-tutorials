import streamlit as st
from pollination_streamlit_io import get_geometry

geo = get_geometry(key='my-geometry')
if geo:
    st.json(geo, expanded=False)