from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import numpy as np
from PIL import Image
import streamlit as st

def decrypt_image(encrypted_data, key_hex, iv_hex):
    """Decrypts an AES-CBC encrypted image and returns the decrypted image."""
    try:
        key = bytes.fromhex(key_hex)
        iv = bytes.fromhex(iv_hex)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        # Remove padding and reshape to original image dimensions
        decrypted_data = unpad(decrypted_data, AES.block_size)
        img_array = np.frombuffer(decrypted_data, dtype=np.uint8).reshape(st.session_state["img_shape"])
        return Image.fromarray(img_array)

    except ValueError:
        st.error("🚨 Decryption failed! Incorrect key or IV.")
        return None