# AI-Art-Web-application-for-generating-images
Web application for generating images using OpenAI's DALL-E model


# Descrition

 AI-Art is a Streamlit-based web application that generates images based on textual descriptions using OpenAI's DALL-E model. The application allows users to enter a description of the image they would like to generate and produces an image that best represents that description.
 
 
In the text input box labeled "Enter a textual description of the image you want to generate", type a description of the image you want to generate. For example, "a cat playing with a ball of yarn" or "a mountain landscape with a sunset sky".
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
### Examples of text you can use to generate images with the AI-Art app:

    A red sports car racing down a winding road
    
    A cozy living room with a fireplace and a bookshelf
    
    A tropical beach with palm trees and crystal-clear water
    
    An abstract painting with vibrant colors and dynamic shapes
    
    A futuristic cityscape with towering skyscrapers and flying cars
    
    A magical forest with glowing mushrooms and a unicorn
    
    A spooky haunted house with bats and ghosts
    
    A delicious sushi platter with various types of rolls and sashimi
    
    A cute puppy playing with a ball in a grassy field
    
    A majestic eagle soaring through a mountain range at sunset
    
![img1](https://user-images.githubusercontent.com/55107467/233864431-3138d5fb-132e-4d6c-b4f0-5338c18cc45c.png)
![img2](https://user-images.githubusercontent.com/55107467/233864420-55f822e3-79b8-48a3-b815-7e42537d5bc8.png)
![img3](https://user-images.githubusercontent.com/55107467/233864425-7a7ca841-c2f1-4299-b2c0-d80bb178169d.png)
![img4](https://user-images.githubusercontent.com/55107467/233864429-33dd97bc-207d-4440-8e33-e410c9ddc8a3.png)


## Project Structure 

    AI-Art-Web-application-for-generating-images/
        ├── data/
        │   
        ├── model/
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
