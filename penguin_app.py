import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

# Custom CSS to style the sidebar radio buttons as a menu
st.sidebar.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "About this App"

# Function to set the page state
def set_page(page_name):
    st.session_state.page = page_name

# Sidebar buttons for navigation
st.sidebar.header("Menu")
if st.sidebar.button("About this app"):
    set_page("About this app")

if st.sidebar.button("Dataset"):
    set_page("Dataset")

if st.sidebar.button("Data Visualisation"):
    set_page("Data Visualisation")

# Content for "About this App"
if st.session_state.page == "About this App":
    st.header("About the Penguin App", divider="blue")
    

    image_path = "/home/an/git/Aneifer/vis_palmer_penguins/media/24_Palmer Penguins Species_Anna Neifer.png"  
    st.image(image_path, caption="Illustration of the three species of penguins featured in the Palmer Penguins dataset. Source: Allison Horst.", use_column_width=True)

    st.subheader("Penguins? What is it all about?")
    st.markdown(
    """
    This app demonstrates the capabilities of the Palmer Penguins dataset, a popular resource for data analysis and visualization. Developed as part of a project at the Data Science Retreat in Berlin, the app showcases how Streamlit, an open-source framework, can be used for creating interactive and insightful data visualizations.

    Users can upload datasets, specifically the Palmer Penguins dataset, to explore various visualizations and gain insights into the data. This dataset was chosen for its simplicity and diversity, making it ideal for exploratory data analysis and machine learning demonstrations.

    """
    )


# Content for "Dataset"
elif st.session_state.page == "Dataset":
    st.header("Penguins dataset", divider="blue")
    st.markdown(
        """
        The Palmer Penguins dataset contains data on three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The dataset includes measurements such as bill length, flipper length, body mass, and more. 

        
        More information about the dataset can be found on the [Palmer Penguins dataset GitHub page](https://github.com/allisonhorst/palmerpenguins).
    """
    )

    # Load the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

    # Rename columns
    df.rename(columns={
    'bill_length_mm': 'bill length (mm)',
    'bill_depth_mm': 'bill depth (mm)',
    'flipper_length_mm': 'flipper length (mm)',
    'body_mass_g': 'body mass (g)'
}, inplace=True)

    st.subheader("Peak into the dataset:")
    st.write(df.head())

    # Plot with Seaborn
    sns.set_palette("pastel")

    # Create a FacetGrid scatter plot
    st.subheader("Scatter Plot with Seaborn")
    plt.figure(figsize=(10, 6))
    facet = sns.FacetGrid(df, hue="species", height=6, palette="pastel")
    facet.map(plt.scatter, "bill length (mm)", "bill depth (mm)").add_legend()
    st.pyplot(plt)

    image_path = "/home/an/git/Aneifer/vis_palmer_penguins/media/24_Palmer Penguins_Bill length and depth_Anna Neifer.png"  
    st.image(image_path, caption="Illustration of the bill of penguins. Source: Allison Horst.", use_column_width=True)

    # Create a violin plot with colors for each species
    st.subheader("Violin Plot of Flipper Length by Species")
    plt.figure(figsize=(10, 6))
    ax = sns.violinplot(x="species", y="flipper length (mm)", data=df, palette="pastel")
    st.pyplot(plt)

    # Create a FacetGrid scatter plot 
    st.subheader("Correlation between body mass and flipper length")
    facet = sns.FacetGrid(df, hue="species", height=6, palette="pastel")
    facet.map(plt.scatter, "body mass (g)", "flipper length (mm)").add_legend()
    st.pyplot(plt)
    st.markdown(
        """Flipper length and body mass have the strongest correlation. Penguins with longer flippers tend to be heavier, suggesting that flipper length is a good predictor of body mass.
        """
    )

# Content for "Data Visualisation"
elif st.session_state.page == "Data Visualisation":
    st.header("Data Visualisation", divider="blue")
    st.write("Please upload the penguin CSV file. You can find the dataset ")
    st.markdown(
        "[here](https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv).",
        unsafe_allow_html=True,
    )

    # File uploader
    uploaded_file = st.file_uploader("", type="csv")

    if uploaded_file is not None:
        try:
            # Attempt to read the uploaded CSV file
            df = pd.read_csv(uploaded_file)

            # Check for required columns
            required_columns = ["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]
            if all(column in df.columns for column in required_columns):
                st.write(df)

                st.subheader("Interactive Scatter Plot with Altair")
                x_axis = st.selectbox(
                    "Choose X axis",
                    options=df.columns,
                    index=df.columns.get_loc("flipper_length_mm"),
                )
                y_axis = st.selectbox(
                    "Choose Y axis",
                    options=df.columns,
                    index=df.columns.get_loc("body_mass_g"),
                )
                color_var = st.selectbox(
                    "Choose Color Variable",
                    options=df.columns,
                    index=df.columns.get_loc("species"),
                )

                scatter_chart = (
                    alt.Chart(df)
                    .mark_circle(size=60)
                    .encode(
                        x=x_axis, y=y_axis, color=color_var, tooltip=list(df.columns)
                    )
                    .interactive()
                )

                st.altair_chart(scatter_chart, use_container_width=True)
            else:
                st.error(
                    "Sorry, but this seems to be the wrong CSV file. Please check if you uploaded the Palmer Penguins data."
                )
        except Exception as e:
            st.error(
                f"An error occurred while processing the file: {e}. Please ensure you upload a valid CSV file."
            )

else:
    st.header("About the Penguin App", divider="blue")
    st.subheader("Penguins? What is it all about?")
    st.markdown(
        """
        This app serves as a demonstration of the Palmer Penguins dataset. 
         can be analysed with Streamlit is a part of a project designed during a class for the Data Science Retreat in Berlin. It . Streamlit is an open-source app framework for Machine Learning and Data Science projects. It can be effectively used for data visualization and interactive data exploration.

        The app allows users to upload datasets, specifically tailored for the Palmer Penguins dataset, and explore various visualizations to uncover insights about the data.

        The Palmer Penguins dataset was chosen for this project due to its simplicity and variety of data points, making it ideal for exploratory data analysis and visualization. It is a popular dataset in the data science community, often used for demonstrating data analysis techniques and building machine learning models. By using this dataset, we aim to showcase the capabilities of Streamlit in creating interactive and insightful data visualizations.       
    """
    )
