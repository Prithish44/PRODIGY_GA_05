# PRODIGY_GA_05
#  Neural Style Transfer App

This project is part of **Prodigy InfoTech's Data Science Internship – Task 5**, where I built a Streamlit-based web app that applies **Neural Style Transfer** using a pre-trained TensorFlow Hub model.

##  Overview

This application allows you to upload a **content image** and a **style image**, and then it generates a new image that blends the content of the first with the artistic style of the second.

###  Features

- Upload any two images via a simple web interface.
- Perform Neural Style Transfer using a model from TensorFlow Hub.
- Real-time image generation and preview.
- Deployed locally using Streamlit.

##  Technologies Used

- Python 
- Streamlit 
- TensorFlow & TensorFlow Hub 
- NumPy 
- Pillow (PIL) 

##  Folder Structure
PRODIGY_GA_05/
├── app.py # Streamlit app file
├── uploads/ # Folder to store uploaded images
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🔧 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prithish44/PRODIGY_GA_05.git
   cd PRODIGY_GA_05
## Create a virtual environment 
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
# Install dependencies

pip install -r requirements.txt

# Run the Streamlit app

streamlit run app.py

# Open in browser

The app will automatically open in your default browser.
