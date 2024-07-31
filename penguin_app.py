import streamlit as st
import pandas as pd
import altair as alt

# Custom CSS to style the sidebar radio buttons as a menu
st.sidebar.markdown("""
    <style>
    .reportview-container .sidebar-content {
        padding-top: 0rem;
    }
    .sidebar .sidebar-content {
        padding: 1rem;
    }
    .widget-container .stRadio > div {
        display: flex;
        flex-direction: column;
    }
    .css-1b4g6e5 {
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
    }
    .css-1b4g6e5:hover {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'About this App'

# Function to set the page state
def set_page(page_name):
    st.session_state.page = page_name

# Sidebar buttons for navigation
st.sidebar.header("Menu")
if st.sidebar.button("About this app"):
    set_page('About this app')

if st.sidebar.button("Dataset"):
    set_page('Dataset')

if st.sidebar.button("Data Visualisation"):
    set_page('Data Visualisation')

# Content for "About this App"
if st.session_state.page == 'About this App':
    st.title("About the Penguin App")
    st.markdown("""
        This app is a part of a project designed during a class for the Data Science Retreat in Berlin. It serves as a demonstration of the Palmer Penguins dataset can be analysed with Streamlit. Streamlit is an open-source app framework for Machine Learning and Data Science projects. It can be effectively used for data visualization and interactive data exploration.

        The app allows users to upload datasets, specifically tailored for the Palmer Penguins dataset, and explore various visualizations to uncover insights about the data.

        The Palmer Penguins dataset was chosen for this project due to its simplicity and variety of data points, making it ideal for exploratory data analysis and visualization. It is a popular dataset in the data science community, often used for demonstrating data analysis techniques and building machine learning models. By using this dataset, we aim to showcase the capabilities of Streamlit in creating interactive and insightful data visualizations.       
    """)

# Content for "Dataset"
elif st.session_state.page == 'Dataset':
    st.title("Penguins dataset")
    st.markdown("""
        The Palmer Penguins dataset contains data on three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The dataset includes measurements such as bill length, bill depth, flipper length, body mass, and more, along with the species and islands.

        This dataset is popular in the data science community for exploratory data analysis, data visualization, and machine learning tasks due to its simplicity and variety of data points.

        More information about the dataset can be found on the [Palmer Penguins dataset GitHub page](https://github.com/allisonhorst/palmerpenguins).
    """)
    
# Content for "Data Visualisation"
elif st.session_state.page == 'Data Visualisation':
    st.title("Data Visualisation")
    st.write("Please upload the penguin CSV file. You can find the dataset ")
    st.markdown("[here](https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv).", unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.file_uploader("", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        st.subheader("Interactive Scatter Plot with Altair")
        x_axis = st.selectbox("Choose X axis", options=df.columns, index=df.columns.get_loc("flipper_length_mm"))
        y_axis = st.selectbox("Choose Y axis", options=df.columns, index=df.columns.get_loc("body_mass_g"))
        color_var = st.selectbox("Choose Color Variable", options=df.columns, index=df.columns.get_loc("species"))

        scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
            x=x_axis,
            y=y_axis,
            color=color_var,
            tooltip=list(df.columns)
        ).interactive()

        st.altair_chart(scatter_chart, use_container_width=True)

else:
    st.info("Please upload the penguin CSV file.")
    st.markdown("[here](https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv).", unsafe_allow_html=True)
