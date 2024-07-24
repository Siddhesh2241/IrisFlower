# Iris Flower Classification App

This Streamlit app predicts the type of Iris flower based on user input features using a K-Nearest Neighbors (KNN) classifier. The app is built with Python and Streamlit and leverages the classic Iris dataset from scikit-learn.

## Features

- Interactive sliders for inputting Iris flower features (sepal length, sepal width, petal length, petal width).
- Displays the predicted Iris flower type based on user inputs.
- Shows the prediction probabilities for each Iris flower type.
- Visualizes the Iris dataset with a scatter matrix plot using Plotly.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Siddhesh2241/IrisFlower.git
   cd IrisFlower
2. **Install the dependencies**:
   Ensure you have Python installed, then run:
      pip install -r requirements.txt
3. **Run the app**:
      streamlit run app.py

## Usage 

. Open the app in your web browser at http://localhost:8501.
. Use the sliders in the sidebar to input the sepal length, sepal width, petal length, and petal width.
. The app will display the predicted Iris flower type and the prediction probabilities.

## Files
.app.py: The main Streamlit app file.
.requirements.txt: The file listing all required Python packages.
.README.md: This readme file.

## Iris Dataset
The Iris dataset consists of 150 samples from each of three species of Iris flowers (Iris setosa, Iris virginica, and Iris versicolor). 
Four features were measured from each sample: sepal length, sepal width, petal length, and petal width.

## Deployment
This app can be deployed on Streamlit Cloud. Simply connect your GitHub repository and follow the deployment instructions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The Iris dataset is a classic dataset in the field of machine learning and is publicly available through the UCI Machine Learning Repository.
The app uses the Streamlit library for creating interactive web applications with Python.

## Contact

Feel free to modify the content to better suit your needs or to include additional information specific to your project.
