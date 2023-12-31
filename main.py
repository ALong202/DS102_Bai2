import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np


#import matplotlib.pyplot as plt
#import seaborn as sns

class_list = {'0': 'Normal','1':'Pneumonia'}
st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

st.header('Upload an image')
image = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])


if image is not None:
  image = Image.open(image)
  st.image(image, caption='Test image')

  if st.button('Predict'):
    image = image.resize((227*227*3, 1))
    vector = np.array(image)
    lable = str(model.predict(model.predict(vector))[0])
    
    
    st.header('Result')
    st.text(class_list[label])



  
  
import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

class_list = {'0': 'Normal', '1': 'Pneumonia'}
st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

st.header('Upload an image')
image = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])

if image is not None:
    image = Image.open(image)
    st.image(image, caption='Test image')

    if st.button('Predict'):
        image = image.resize((227, 227))
        vector = np.array(image)
        vector = vector.reshape((1, 227, 227, 3))  # Reshape to match the model input shape

        # Make prediction
        prediction = model.predict(vector)

        # Get the predicted label
        label_index = np.argmax(prediction)
        label = class_list[str(label_index)]

        st.header('Result')
        st.text(f'Prediction: {label}')

  
  
  
  
  
  
  
  

