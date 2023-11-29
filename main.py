import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

#import matplotlib.pyplot as plt
#import seaborn as sns

class_list = {'0': 'Normal','1':'Pneumonia'}
st.title('Pneumonia Detection')


input = open('lrc_xray.pkl', 'rb')
model = plk.load(input)


st.header('Upload an image')
image = st.file_uploader('choose an image', type= (['png','jpg','jpeg']))

if image is not None:
  image = Image.open(image)
  st.image(image, caption = 'Test image')


