# Import the necessary libraries
import openai
import urllib.request
from PIL import Image
import streamlit as st

# Set the OpenAI API key
openai.api_key = "-----"

# Function to generate the image based on the given description
def generate_image(image_description):

  # Call the OpenAI API to generate the image
  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  
  # Get the URL of the generated image
  img_url = img_response['data'][0]['url']

  # Download the generated image and save it as a PNG file
  urllib.request.urlretrieve(img_url, 'img.png')

  # Open the PNG image file using PIL
  img = Image.open("img.png")
  
  # Return the PIL image object
  return img

# Set the title of the Streamlit page
st.title('AI-Art - Image Generation')

# Add a text input box for the image description
img_description = st.text_input('Enter a textual description of the image you want to generate')

# Add a button to generate the image based on the given description
if st.button('Generate Image'):
    
    # Call the generate_image function and store the resulting PIL image object
    generated_img = generate_image(img_description)
    
    # Display the generated image in the Streamlit page
    st.image(generated_img)
