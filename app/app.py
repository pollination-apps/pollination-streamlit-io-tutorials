import pathlib
from enum import Enum
import streamlit as st
from streamlit_ace import st_ace, THEMES
from pollination_streamlit_io import ( get_geometry,
    send_geometry, get_hbjson, send_hbjson )

st.set_page_config(
    page_title='Direct Sun Hours',
    page_icon='https://app.pollination.cloud/favicon.ico',
    initial_sidebar_state='collapsed',
)  # type: ignore
st.sidebar.image(
    'https://uploads-ssl.webflow.com/6035339e9bb6445b8e5f77d7/616da00b76225ec0e4d975ba'
    '_pollination_brandmark-p-500.png',
    use_column_width=True
)

TEMPLATES = './templates'

class Command(Enum):
    GET_MODEL = 'Get Model'
    SEND_MODEL = 'Send Model'
    GET_GEOMETRY = 'Get Geometry'
    SEND_GEOMETRY = 'Send Geometry'

SCRIPTS = {
    Command.GET_MODEL.value: pathlib.Path(TEMPLATES)
        .joinpath('get_model.py').read_text(),
    Command.SEND_MODEL.value: pathlib.Path(TEMPLATES)
        .joinpath('send_model.py').read_text(),
    Command.GET_GEOMETRY.value: pathlib.Path(TEMPLATES)
        .joinpath('get_geometry.py').read_text(),
    Command.SEND_GEOMETRY.value: pathlib.Path(TEMPLATES)
        .joinpath('send_geometry.py').read_text(),
}

DOCS = {
    Command.GET_MODEL.value: get_hbjson.__doc__,
    Command.SEND_MODEL.value: send_hbjson.__doc__,
    Command.GET_GEOMETRY.value: get_geometry.__doc__,
    Command.SEND_GEOMETRY.value: get_geometry.__doc__
}


def main():
    """Learning doing."""

    # title
    st.header('Select a script!')

    # set tabs
    tab1, tab2 = st.tabs(["CAD interactions", "Cloud interactions"])

    # sidebar
    st.sidebar.markdown('## Editor Settings')
    st.sidebar.markdown('----------')
    auto_update = st.sidebar.checkbox(label='Auto update',
        value=True)
    font_size = st.sidebar.number_input(label='Font size',
        value=15, min_value=1, max_value=30)
    theme = st.sidebar.selectbox(
        label='Select a theme', options=THEMES, index=5)

    # tabs layout
    with tab1:
        option = st.selectbox(
            'Select a script to test',
            (Command.SEND_MODEL.value, 
            Command.GET_MODEL.value,
            Command.SEND_GEOMETRY.value, 
            Command.GET_GEOMETRY.value))
        with st.expander(label='Docs', expanded=False):
            st.markdown(DOCS[option])
        content = st_ace(language="python", 
            value=SCRIPTS[option], 
            auto_update=auto_update,
            font_size=font_size,
            theme=theme)
        exec(content)

    with tab2:
        pass

if __name__ == '__main__':
    main()

