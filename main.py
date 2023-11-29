import streamlit as st
from PIL import Image
import pickle as pkl
import numpy

import matplotlib.pyplot as plt
import seaborn as sns

class_list = {'0': 'Normal','1':'Pneumonia'}

input = open('', 'rb')
model = plk.load(input)


st.header('Upload a image')
image = st.file_uploader('', type= (['png','jpg','jpeg']))

if image is not None:
  image = Image.open(image)
  st.image(image, caption = 'Test image')

