
import streamlit as st 



def home_page():
    st.title("Image Encryptor and Decryptor")
    st.write("This is a simple web app to encrypt and decrypt images")
    with st.expander("See more details"):
        st.write("Here are more details...")

    # File uploader
    image = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

    st.subheader("Select the encryption algorithm")
    st.sidebar.title("Encryption Options")
    selected_algo = st.sidebar.selectbox("Select the encryption algorithm", ["AES", "DES", "RSA"] , key="algo")
    st.write(f"Selected encryption algorithm: {selected_algo}")
    if image is not None:
        st.image(image, caption="Uploaded Image", use_column_width=True)
        # Add your encryption logic here
        if st.button("Click to Encrypt Image"):
            st.write("Image encryption logic goes here")
    else:
        st.write("Please upload an image.")
        

if __name__ == "main":
    home_page()