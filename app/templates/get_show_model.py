import os, json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from honeybee.model import Model as HBModel
from honeybee_vtk.model import Model as VTKModel

from pollination_streamlit_viewer import viewer
from pollination_streamlit_io import get_hbjson

st.header("Get Model")

if 'temp' not in st.session_state:
    st.session_state.temp = Path('/tmp')
    st.session_state.temp.mkdir(parents=True, exist_ok=True)

def create_vtkjs(hbjson_path: Path):
    if not hbjson_path:
        return
    
    model = VTKModel.from_hbjson(hbjson_path.as_posix())
    
    vtkjs_dir = st.session_state.temp.joinpath('vtkjs')
    if not vtkjs_dir.exists():
        vtkjs_dir.mkdir(parents=True, exist_ok=True)

    vtkjs_file = vtkjs_dir.joinpath(f'{hbjson_path.stem}.vtkjs')
    
    if not vtkjs_file.is_file():
        model.to_vtkjs(
            folder=vtkjs_dir.as_posix(),
            name=hbjson_path.stem
        )

    return vtkjs_file


def show_model(hbjson_path: Path):
    """Render HBJSON."""

    vtkjs_name = f'{hbjson_path.stem}_vtkjs'
    vtkjs = create_vtkjs(hbjson_path)
    st.session_state.content = vtkjs.read_bytes()
    st.session_state[vtkjs_name] = vtkjs

def callback_once():
    if 'hbjson' in st.session_state.get_hbjson:
        hb_model = HBModel.from_dict(st.session_state.get_hbjson['hbjson'])
        if hb_model:
            hbjson_path = st.session_state.temp.joinpath(f'{hb_model.identifier}.hbjson')
            hbjson_path.write_text(json.dumps(hb_model.to_dict()))
            show_model(hbjson_path)

hbjson = get_hbjson('get_hbjson', on_change=callback_once)

if st.session_state.get_hbjson is not None:

    st.subheader('Hbjson Visualized')
    if 'content' in st.session_state:
        viewer(
            content=st.session_state.content,
            key='vtkjs-viewer',
            subscribe=False,
            style={
                'height' : '640px'
            }
        )

    st.subheader('Hbjson Content')
    if st.session_state.get_hbjson is not None:
        st.json(st.session_state.get_hbjson, expanded=False)
        
else:
    st.info('Load a model!')