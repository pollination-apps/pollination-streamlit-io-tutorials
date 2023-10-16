import json
import pathlib
import streamlit as st
from pollination_streamlit_io import send_geometry

geo_txt = pathlib.Path('resources/geometry.json').read_text()
geo = json.loads(geo_txt)

col1, col2 = st.columns(2)

col1.link_button('Info about the schema', 
               url='https://www.ladybug.tools/ladybug-display-schema/geometry.html')
col2.link_button('Info about the schema', 
               url='https://www.ladybug.tools/ladybug-display-schema/display.html')

face = {
    "type": "Face3D",
    "boundary": [
        [4, 4, 0],
        [8, 4, 0],
        [8, 8, 0],
        [4, 8, 0]
    ],
    "plane": {
        "type": "Plane",
        "n": [0, 0, 1],
        "o": [0, 0, 0],
        "x": [1, 0, 0]
    }
}

# or display geometries 
display_face = {
    "type": "DisplayFace3D",
    "geometry": {
        "type": "Face3D",
        "boundary": [
            [0, 0, 0],
            [4, 0, 0],
            [4, 4, 0],
            [0, 4, 0]
        ],
        "plane": {
            "type": "Plane",
            "n": [0, 0, 1],
            "o": [0, 0, 0],
            "x": [1, 0, 0]
        },
        "holes": [
            [
                [1, 1, 0],
                [1.5, 1, 0],
                [1.5, 1.5, 0],
                [1, 1.5, 0]
            ],
            [
                [2, 2, 0],
                [3, 2, 0],
                [3, 3, 0],
                [2, 3, 0]
            ]
        ]
    },
    "color": {
        "type": "Color",
        "r": 255,
        "g": 0,
        "b": 0,
        "a": 255
    },
    "display_mode": "Surface"
}

st.info('it can send a list of Display Geometry and/or Geometry.')
cmd = send_geometry(key='my-geometry', geometry=[face, display_face])