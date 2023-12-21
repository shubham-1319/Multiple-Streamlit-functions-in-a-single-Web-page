#made by Shubh
import streamlit as st

st.title('My First Streamlit Web App')
st.write('This is a simple web app built using Streamlit')

# Header
st.header('About')
st.write('This web app is a demonstration of what you can build using Streamlit')

# Text Input
st.subheader('Text Input')
user_input = st.text_input('Enter some text')
st.write('You entered:', user_input)

# Checkbox
st.subheader('Checkbox')
checked = st.checkbox('Check me out')
st.write('Checked:', checked)

# Radio Buttons
st.subheader('Radio Buttons')
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.radio('Select an option', options)
st.write('You selected:', selected_option)

# Selectbox
st.subheader('Selectbox')
select_options = ['Select Option 1', 'Select Option 2', 'Select Option 3']
selected_value = st.selectbox('Choose a value', select_options)
st.write('You selected:', selected_value)

# Multiselect
st.subheader('Multiselect')
multiselect_options = ['Option 1', 'Option 2', 'Option 3']
selected_values = st.multiselect('Select multiple values', multiselect_options)
st.write('You selected:', selected_values)

# File Upload
st.subheader('File Upload')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    st.write('You uploaded:', uploaded_file.name)

# Slider
st.subheader('Slider')
slider_value = st.slider('Slide to select a value', 0, 100, 50)
st.write('You selected:', slider_value)

# Date Input Important 
st.subheader('Date Input')
date_value = st.date_input('Select a date')
st.write('You selected:', date_value)
