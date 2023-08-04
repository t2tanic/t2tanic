import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

width = 700

msg = 'A ship that does not leave the harbor will not sink'
st.text(msg)

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    ).properties(width=width, height=300)
st.write(c)

image = Image.open('images/logo.webp')
st.image(image, width=width, caption=msg)

code = f'''import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

width = 700

msg = 'A ship that does not leave the harbor will not sink'
st.text(msg)

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    ).properties(width=width, height=300)
st.write(c)

image = Image.open('images/logo.webp')
st.image(image, width=width, caption=msg)'''
st.code(code, language='python', line_numbers=True)
