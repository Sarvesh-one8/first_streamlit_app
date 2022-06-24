import streamlit
import pandas

streamlit.title('My paraents new healthy dinner.')

streamlit.header('Breatfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Kale')
streamlit.text('Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
