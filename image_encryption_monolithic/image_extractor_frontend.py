import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import numpy as np
from PIL import Image
from Components.encryptor import encrypt_image
from Components.decryptor import decrypt_image
from Components.about import About_page


import streamlit as st 
from PIL import Image



from Components.generate_key import generate_keys
import streamlit as st 
from PIL import Image 
from Crypto.Util.Padding import pad, unpad
import numpy as np 
from Crypto.Cipher import AES

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import numpy as np
from PIL import Image
import streamlit as st





page_selected = st.sidebar.selectbox("Select Page", ["Home","About"])

def decrypt_image(encrypted_data, key_hex, iv_hex):
    """Decrypts an AES-CBC encrypted image and returns the decrypted image."""
    try:
        key = bytes.fromhex(key_hex)
        iv = bytes.fromhex(iv_hex)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        decrypted_data = unpad(decrypted_data, AES.block_size)
        img_array = np.frombuffer(decrypted_data, dtype=np.uint8).reshape(st.session_state["img_shape"])
        return Image.fromarray(img_array)

    except ValueError:
        st.error("🚨 Decryption failed! Incorrect key or IV.")
        return None


def encrypt_image(image):
    """Encrypts an image using AES-CBC and returns encrypted data."""
    generate_keys() 
    key, iv = st.session_state["key"], st.session_state["iv"]

    img = Image.open(image).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)
    img_shape = img_array.shape 

    img_bytes = img_array.tobytes()
    padded_data = pad(img_bytes, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)

    st.session_state["img_shape"] = img_shape

    return encrypted_data, key, iv


def About_page():
    st.title("About")
    st.write("This is a simple web app to encrypt and decrypt images")
    with st.expander("See more details"):
        st.write("Here are more details...")
    st.write("This app allows users to upload images and encrypt them using various encryption algorithms such as AES, DES, and RSA. The encrypted images can then be decrypted back to their original form.")

    st.subheader("Developers")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Developer 1**")
        st.image("Assets/My_photo.jpg", width=150, caption="Vineet Sharma")
        st.write("Main Developer")

    with col2:
        st.write("**Developer 2**")
        st.write("Details about Developer 2")

    with col3:
        st.write("**Developer 3**")
        image = Image.open("Assets/nitin.png")

# Resize the image (new width, new height)
        new_height = 1060  # Adjust this as needed
        image = image.resize((image.width, new_height))

        st.image(image, width=150, caption="Nitin Sharma")
        st.write("Assistant Developer")
    with col4:
        st.write("**Developer 4**")
        # st.image()
        st.write("Details about Developer 4")

    
    with st.expander("More about the algorithms"):
        st.write("""1️⃣ AES (Advanced Encryption Standard)
✅ Type: Symmetric-key block cipher
✅ Key Sizes: 128-bit, 192-bit, 256-bit
✅ Use Case: Secure data encryption (e.g., banking, WiFi security, file encryption)

How AES Works:
AES encrypts data in blocks of 128 bits using a single key (symmetric encryption).

Key Expansion: The key is expanded into multiple round keys.
Substitution (S-Box): Each byte is replaced using a fixed lookup table.
Shift Rows: Rows of the data block are shifted to mix up the bytes.
Mix Columns: Mathematical transformation is applied to mix byte columns.
Add Round Key: XOR operation with the round key.
Repeat for 10, 12, or 14 rounds depending on key size.
🔒 Why AES?

Faster than RSA
More secure than DES
Used in modern encryption (HTTPS, VPNs, disk encryption)""")
        st.write("""2️⃣ DES (Data Encryption Standard)
✅ Type: Symmetric-key block cipher
✅ Key Size: 56-bit
✅ Use Case: Older encryption standard (replaced by AES due to security flaws)

How DES Works:
Splits plaintext into 64-bit blocks.
Uses a 56-bit key for encryption.
Performs 16 rounds of substitution and permutation using Feistel structure.
Uses XOR operations, S-box substitutions, and bit shifting to encrypt data.
❌ Why DES is Insecure?

56-bit key is too small (can be cracked in hours).
Vulnerable to brute-force attacks.
3DES (Triple DES) was introduced as a more secure version but is still slower than AES.""")
        st.write('''3️⃣ RSA (Rivest-Shamir-Adleman)
✅ Type: Asymmetric-key encryption
✅ Key Size: 1024-bit, 2048-bit, 4096-bit
✅ Use Case: Secure key exchange (e.g., SSL/TLS, digital signatures)

How RSA Works:
RSA uses two keys:

Public Key (for encryption)
Private Key (for decryption)
Steps:
Generate two large prime numbers (p, q) and compute n = p × q.
Compute Euler’s totient function: ϕ(n) = (p-1) × (q-1).
Choose an encryption key e, such that 1 < e < ϕ(n) and gcd(e, ϕ(n)) = 1.
Compute the decryption key d, where (e × d) mod ϕ(n) = 1.
Encryption: Ciphertext = (Plaintext^e) mod n
Decryption: Plaintext = (Ciphertext^d) mod n
🔑 Why RSA?

Provides secure communication (e.g., used in HTTPS and digital signatures).
Slower than AES because of large key size.
Often combined with AES for hybrid encryption (e.g., RSA encrypts the AES key).
''')

# if __name__ == "__main__":
#     About_page()


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

