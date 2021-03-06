import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# disply the api
streamlit.text(fruityvice_response)

streamlit.title('My paraents new healthy dinner.')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

def get_fruityvice_data(this_fruit_choice):      
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit"+ fruit_choice)
    fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("PLEASE ENTER")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()


streamlit.header("The Fruit Load List Contains:")

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()      
        
#add a button
if streamlit.button("Visit Fruit Load List and your favrorites.!!"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

 # Inser

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("INSERT into fruit_load_list values('" + new_fruit + "')")
         return "Thanks for adding" + new_fruit  

