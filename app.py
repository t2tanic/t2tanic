import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="t2tatic",
    page_icon="🛳",
)

width = 400

msg = 'A ship that does not leave the harbor will not sink'
st.text(msg)

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    ).properties(width=width, height=300)
st.write(c)

image = Image.open('logo.webp')
st.image(image, width=width, caption=msg)


train = pd.read_parquet('data/train.parquet')
test = pd.read_parquet('data/test.parquet')
submission = pd.read_parquet('data/gender_submission.parquet')

st.write(train.head(5))
st.write(test.head(5))
st.write(submission.head(5))
