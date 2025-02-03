import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
st.set_page_config(initial_sidebar_state='collapsed')
page = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact"])
# Title

from Components.home import home_page
from Components.about import About_page
from Components.contact import contact

if page == "Home":
    home_page()
elif page == "About":
    About_page()