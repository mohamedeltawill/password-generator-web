import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Secure Password Generator")
st.write("Generate a strong, custom password in seconds!")

length = st.slider("Password Length", 6, 50, 12)
use_upper = st.checkbox("Include Uppercase Letters", value=True)
use_lower = st.checkbox("Include Lowercase Letters", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

def generate_password(length, upper, lower, numbers, symbols):
    chars = ''
    if lower:
        chars += string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    if not chars:
        return "❌ Please select at least one character set."

    return ''.join(random.choice(chars) for _ in range(length))

if st.button("Generate Password"):
    password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)
    st.code(password, language='text')