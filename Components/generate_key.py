import streamlit as st 
import os 

def generate_keys():
    """Generate a random AES key and IV, store in session state."""
    if "key" not in st.session_state:
        st.session_state["key"] = os.urandom(16)  # 16-byte key
    if "iv" not in st.session_state:
        st.session_state["iv"] = os.urandom(16)

