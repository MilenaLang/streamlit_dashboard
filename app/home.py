import streamlit as st
from PIL import Image

def main():
    """
    This function creates the home section
    :return: Home section
    """

    # add title
    st.title("Airbnb-Dashboard Berlin, July 2021")
    # information about the project
    st.write("This app is designed to analyze and visualize airbnb housing and pricing in Berlin, july 2021.")

    #add image
    image = Image.open('airbnb.png.webp')
    st.image(image, caption="Airbnb-Logo, derived from https://www.finanzgefluester.de/besteuerung-airbnb/")
    # information on data
    st.markdown("## Ressources")
    st.markdown("* EXAMPLE SOURCE")