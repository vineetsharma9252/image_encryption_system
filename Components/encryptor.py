
from Components.generate_key import generate_keys
import streamlit as st 
from PIL import Image 
from Crypto.Util.Padding import pad, unpad
import numpy as np 
from Crypto.Cipher import AES

def encrypt_image(image):
    """Encrypts an image using AES-CBC and returns encrypted data."""
    generate_keys()  # Ensure keys are generated
    key, iv = st.session_state["key"], st.session_state["iv"]

    img = Image.open(image).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)
    img_shape = img_array.shape  # Store original shape

    img_bytes = img_array.tobytes()
    padded_data = pad(img_bytes, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)

    # Store shape for decryption
    st.session_state["img_shape"] = img_shape

    return encrypted_data, key, iv