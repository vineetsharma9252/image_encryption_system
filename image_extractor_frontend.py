import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import numpy as np
from PIL import Image
from Components.encryptor import encrypt_image
from Components.decryptor import decrypt_image
from Components.about import About_page

page_selected = st.sidebar.selectbox("Select Page", ["Home", "Contact","About"])

def home():
    st.title("🔐 AES Image Encryptor & Decryptor")

    st.subheader("🛡 Encrypt an Image")
    uploaded_image = st.file_uploader("📤 Upload an Image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        encrypted_data, key, iv = encrypt_image(uploaded_image)
        st.success("✅ Image successfully encrypted!")

        st.text(f"🔑 Encryption Key: {key.hex()}")
        st.text(f"🆔 IV: {iv.hex()}")

        st.download_button("📥 Download Encrypted Image", encrypted_data, file_name="encrypted_image.bin")

    st.subheader("🔓 Decrypt an Image")
    uploaded_encrypted_file = st.file_uploader("📤 Upload Encrypted File (.bin)", type=["bin"])
    key_input = st.text_input("🔑 Enter the encryption key (hex format):")
    iv_input = st.text_input("🆔 Enter the IV (hex format):")

    if uploaded_encrypted_file and key_input and iv_input:
        encrypted_data = uploaded_encrypted_file.read()
        decrypted_img = decrypt_image(encrypted_data, key_input, iv_input)

        if decrypted_img:
            st.image(decrypted_img, caption="🖼 Decrypted Image")



if page_selected == "Home":
    home()
elif page_selected == "About":
    About_page()

