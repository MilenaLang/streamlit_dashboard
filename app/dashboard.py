import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("listings_berlin.csv")

def main():
    """
    This function provides a dashboard for Airbnb data from july 2021 in Berlin.
    :return: Dashboard
    """
    # set title
    st.title("Airbnb-Dashboard Berlin, July 2021")
    data = pd.read_csv("listings_berlin.csv")
    st.map(data )

    #select districts
    st.markdown('## Select district of interest')
    #district names
    selected = data.neighbourhood_group.unique()
    #multiselection of districts
    districts = st.multiselect('Select districts', selected)



    def plot_district(district):
        """
        Get stats and plots for each district
        :param district: name of the selected district
        :return: muötiple plots and stats
        """
        import numpy as np
        import matplotlib.pyplot as plt
        ""
        for district in districts:
            prices = data.loc[data['neighborhood_group'] == district]
            fig = plt.hist(prices, density= True, bins=30)
            plt.ylabel('Hello')
            st.pyplot(fig)





