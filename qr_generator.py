import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator")
st.title("QR Code Generator")
st.divider()

url = st.text_input("Enter a URL to generate QR Code :smile:", placeholder="https://example.com")

# click = st.button("Generate QR Code", type="primary", width=150)

col1, col2, col3 = st.columns(3)
with col2:
    click = st.button("Generate QR Code", type="primary", width=250)


    if click:
        if url:
            # qr = qrcode.QRCode()
            # qr.add_data(url)
            # qr.make()
            # img = qr.make_image()
            img = qrcode.make(url)
            
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            
            left, mid, right = st.columns(3)
            st.image(buffer, caption="QR Code Generated Successfully!")
            
            st.download_button("Download QR Code", data=buffer, file_name="qr_code.png", mime="image/png", type="secondary", icon=":material/download:", width="stretch")
        else:
            st.warning("⚠ Please enter a valid URL")   
