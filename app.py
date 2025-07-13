import streamlit as st  
import numpy as np
import os 
import tensorflow_hub as hub 
import tensorflow as tf 
from PIL import Image

# Style Transfer Logic   

def load_img(img_path) : 
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels = 3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

def style_transfer(content_img, style_img) : 
    model = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")
    stylize_img = model(tf.constant(content_img), tf.constant(style_img))
    stylize_img = stylize_img[0]
    return stylize_img

# UI   
st.set_page_config(layout="centered")
st.title("Neural Style Transfer")
st.subheader("Upload Image")
content_file = st.file_uploader("Upload Content Image")
style_file = st.file_uploader("Upload Style Image")
os.makedirs("./uploads", exist_ok = True)

if content_file and style_file : 
    content_path = os.path.join("uploads", content_file.name)
    style_path = os.path.join("uploads", style_file.name)

    with open(content_path, "wb") as f : 
        f.write(content_file.read())
    with open(style_path, "wb") as f : 
        f.write(style_file.read())
    col1, col2 = st.columns(2)

    with col1:
        content_image = Image.open(content_path)
        content_image = content_image.resize((256, 256))
        st.image(content_image, caption="Content Image", width = 300)

    with col2:
        style_image = Image.open(style_path)
        style_image = style_image.resize((256, 256))
        st.image(style_image, caption="Style Image", width = 300)

    if st.button("Generate Style Image") :
        with st.spinner("....") :
            content_img = load_img(content_path)
            style_img = load_img(style_path)
            stylize_img = style_transfer(content_img, style_img)
            stylize_img = np.squeeze(stylize_img)
            stylize_img = Image.fromarray((stylize_img*255).astype("uint8"))
            stylize_img = stylize_img.resize((256, 256))
            st.image(stylize_img, caption = "Stylize Image", width = 400)





