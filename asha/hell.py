import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

number = st.slider("Pick a number", 0, 100)
st.header("this is a header!")
st.title("this is a title")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

def sqr(num):
    return num ** 2

num = st.number_input("Enter a number")
if(st.button("Calculate square of number")):
    result = sqr(num)
    st.text(f"The square of {num} is {result}")