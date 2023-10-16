import streamlit as st
from pollination_streamlit_io import send_hbjson
from honeybee.model import Model
from honeybee.room import Room

# create a HB model
room = Room.from_box('my-room')
model = Model('my-model', rooms=[room])

cmd = send_hbjson(key='my-model', hbjson=model.to_dict())