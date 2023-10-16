import streamlit as st
from pollination_streamlit_io import send_geometry
from ladybug_display.geometry3d.face import Face3D, DisplayFace3D
from ladybug_display.geometry3d.point import Point3D
from ladybug_display.geometry3d.vector import Vector3D
from ladybug.color import Color

face = Face3D(boundary=[
    Point3D(0, 0, 0),
    Point3D(4, 0, 0),
    Point3D(4, 4, 0),
    Point3D(0, 4, 0)])
face_copy = face.move(Vector3D(4, 0, 0))
display_face = DisplayFace3D(geometry=face_copy, color=Color(255, 0, 0))

geo = list(map(lambda g: g.to_dict(), [face, display_face]))

st.info('it can send a list of Display Geometry and/or Geometry.')
cmd = send_geometry(key='my-geometry', geometry=geo)