#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import streamlit as st
import os
os.chdir("D:\CSE 4 PROJECT")


# In[5]:


import streamlit as st
import tensorflow as tf
from PIL import Image

# Load the model
model = tf.keras.models.load_model('my_model.h5')

# Define the class labels
classes = ['No DR', 'Mild', 'Moderate', 'Severe', 'Proliferative DR']

# Define the Streamlit app
def app():
    # Set the title and sidebar
    st.set_page_config(page_title='Diabetic Retinopathy Detection', page_icon=':eyes:')
    st.sidebar.title('Diabetic Retinopathy Detection')
    st.sidebar.info('Upload an image and the app will predict the damage level of diabetic retinopathy.')
    
    # Upload the image
    uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Preprocess the image
        img_array = tf.keras.preprocessing.image.img_to_array(image)
        img_array = tf.image.resize(img_array, [224, 224])
        img_array = tf.expand_dims(img_array, 0)
        img_array = img_array / 255.0
        
        # Make a prediction
        prediction = model.predict(img_array)
        predicted_class = classes[prediction.argmax()]
        st.success(f'The damage level of diabetic retinopathy is {predicted_class}.')


# In[6]:


app()


# In[ ]:




