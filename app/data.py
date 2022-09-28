import streamlit as st
import pandas as pd

def main():
    """
    This function shows the raw dataset behind the dashboard
    :return: Table with data
    """
    # set title
    st.title("Data")
    st.write("Data retrieved from: https://www.kaggle.com/code/lennarthaupts/airbnb-prices-in-berlin/data")
    # dataframe
    data = pd.read_csv("listings_berlin.csv")

    # give the user the opportunity to have a look at the data
    if st.checkbox("Show data..."):
        st.subheader("Raw data")
        # show data
        st.write(data)
        st.subheader("Locations of Airbnb's")
        st.map(data)