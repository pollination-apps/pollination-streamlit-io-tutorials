import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_geometry

geo_txt = pathlib.Path('resources/geometry.json').read_text()
geo = json.loads(geo_txt)

cmd = send_geometry(key='my-geometry', geometry=geo)