import streamlit as st
import home
import data
import dashboard
import testdata

st.set_page_config(
    page_icon="✅",
    layout="wide",
)

PAGES = {
    "Home": home,
    "Dashboard": dashboard,
    "Data": data,
    "Test": testdata,
}

def main():
    """
    This function sets up the basic layout of the dashboard, including the sidebar Elements.
    :return:Sidebar layout
    """
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is developed by Milena Lang (last updated 10.10.2022).
        """
    )

if __name__ == "__main__":
    main()