from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import plotly.express as px

def Iris_data():
    df = user_input()
    st.subheader("User Input Parameters")
    st.write(df)

    iris = load_iris()
    feature_names = iris.feature_names
    x = pd.DataFrame(iris.data, columns=feature_names)
    y = iris.target

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x, y)

    df.columns = feature_names  # Ensure the user input has the same feature names

    prediction = model.predict(df)
    prediction_prob = model.predict_proba(df)

    st.subheader('Class Labels and their Corresponding Index Number')
    st.write(iris.target_names)

    st.subheader('Prediction')
    st.write(iris.target_names[prediction][0])

    st.subheader('Prediction Probability')
    prob_df = pd.DataFrame(prediction_prob, columns=iris.target_names)
    st.write(prob_df)

    # Plotting prediction probabilities
    fig_prob = px.bar(prob_df, title="Prediction Probability")
    st.plotly_chart(fig_prob)

    # Scatter plot of the dataset
    df_full = pd.DataFrame(iris.data, columns=iris.feature_names)
    df_full['target'] = iris.target
    df_full['target'] = df_full['target'].apply(lambda x: iris.target_names[x])
    
    fig_scatter = px.scatter_matrix(df_full, dimensions=iris.feature_names, color='target', title="Iris Dataset Scatter Matrix")
    st.plotly_chart(fig_scatter)

def user_input():
    sepal_length = st.sidebar.slider('sepal length (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('sepal width (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal length (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal width (cm)', 0.1, 2.5, 0.2)
    
    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

def main():
    st.write("""
        # Simple Iris Flower Case Study
        This app predicts the Iris flower type
    """)
    
    st.sidebar.header("User Input Parameters")
    Iris_data()

if __name__ == "__main__":
    main()
