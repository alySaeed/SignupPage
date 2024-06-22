import streamlit as st

original_title = '<h1 style="font-family: serif; color:white; font-size: 40px;">MeAI is Launching Soon✨ </h1>'
st.markdown(original_title, unsafe_allow_html=True)

# Access the secret email
email = st.secrets["email"]


# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
for i in range(8):
    st.markdown('##')

st.markdown('<h1 style="font-family: serif; color:black; font-size: 20px;">Sign up to be the first to know about our soft launch events. 📩</h1>', unsafe_allow_html=True)
contact_form = f"""
<form action="https://formsubmit.co/{email}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)




input_style = """
<style>
# input[type="text"], input[type="email"] {
#     background-color: transparent;
#     color: #a19eae;  // This changes the text color inside the input box
# }
input[type=text], input[type=email], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;

}
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

