import streamlit as st
from streamlit_ace import st_ace

SCRIPTS = {
    'Get Model': """
import streamlit as st
from pollination_streamlit_io import get_hbjson

model = get_hbjson(key='my-model')
if model:
    st.json(model, expanded=False)
""",
    'Send Model': """
import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_hbjson

model_txt = pathlib.Path('resources/sample.hbjson').read_text()
model = json.loads(model_txt)

cmd = send_hbjson(key='my-model', hbjson=model)
""",
    'Get Geometry': """
import streamlit as st
from pollination_streamlit_io import get_geometry

geo = get_geometry(key='my-geometry')
if geo:
    st.json(geo, expanded=False)
""",
    'Send Geometry': """
import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_geometry

geo_txt = pathlib.Path('resources/geometry.json').read_text()
geo = json.loads(geo_txt)

cmd = send_geometry(key='my-geometry', geometry=geo)
"""
}

st.header('Select Script')
option = st.selectbox(
        'Select a script to test',
        ('Send Model', 'Get Model',
        'Send Geometry', 'Get Geometry'))
content = st_ace(language="python", 
    value=SCRIPTS[option], auto_update=True)

exec(content)