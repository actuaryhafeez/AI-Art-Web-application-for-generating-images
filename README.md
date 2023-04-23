# AI-Art-Web-application-for-generating-images-
Web application for generating images using OpenAI's DALL-E model


# Descrition

 AI-Art is a Streamlit-based web application that generates images based on textual descriptions using OpenAI's DALL-E model. The application allows users to enter a description of the image they would like to generate and produces an image that best represents that description.
 
 
#  Steps to use the AI-Art app

1. Go to the AI-Art web page hosted on a server, or if you have cloned the repository locally, run the app.py file using Streamlit. You should see a page with the title "AI-Art - Image Generation using DALL-E".
2. In the text input box labeled "Enter a textual description of the image you want to generate", type a description of the image you want to generate. For example, "a cat playing with a ball of yarn" or "a mountain landscape with a sunset sky".
4. Click the "Generate Image" button to generate an image based on the description you entered.
5. Wait a few seconds while the DALL-E model generates the image. The generated image will be displayed on the page once it is ready.
6. You can generate more images by entering different descriptions and clicking the "Generate Image" button again.

Note that the quality of the generated image may vary depending on the complexity and specificity of the description. You may need to experiment with different descriptions to get the desired results.

### How to Use
#### To run the app, first clone the repository:
    git clone https://github.com/actuaryhafeez/AI-Art-Web-application-for-generating-images.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
#### Next, install the required packages using pip:
    pip install -r requirements.txt
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
#### Then, run the app:
    streamlit run app.py


## Project Structure 

    movie-recommender-system-streamlit/
        ├── data/
        │   
        ├── model/
        │   └── xgb_model.pkl
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).


# References

### Acknowledgements
This project was built using the following tools and resources:

* Python
* Streamlit
* Openai
