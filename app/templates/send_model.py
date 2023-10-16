import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_hbjson

model_txt = pathlib.Path('resources/model.hbjson').read_text()
model = json.loads(model_txt)

cmd = send_hbjson(key='my-model', hbjson=model)