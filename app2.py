import streamlit as st

# Set the title of the application
st.title("Da hora emu APP")

# Display a header
st.header("Welcome to Streamlit!")

# Display some plain text
st.text("This is a basic example demonstrating Streamlit's simplicity.")

# Add a text input widget
user_name = st.text_input("What's your name?")

# Display a greeting if a name is entered
if user_name:
    st.write(f"Hello, {user_name}!")

# Add a slider widget
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You selected: {age} years old.")

# Add a button
if st.button("Click me!"):
    st.success("Button clicked!")
