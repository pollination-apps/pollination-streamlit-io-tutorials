import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_results

res_txt = pathlib.Path('resources/model_daylight_factor.vsf').read_text()
res = json.loads(res_txt)

cmd = send_results(key='my-results', results=res)