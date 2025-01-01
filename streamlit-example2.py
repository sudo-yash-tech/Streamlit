import streamlit as st
import pandas as pd
import numpy as np

##Title of the Application
st.title('Hello, Streamlit!')

##Display a Simple Text
st.write("This is a Simple Text")

##Create a simple dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

##Display the dataframe
st.write("Here is a simple dataframe")
st.write(df)

##Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.line_chart(chart_data)