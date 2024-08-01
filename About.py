import streamlit as st

def main():
    st.header("About the Penguin App", divider="blue")
    image_path = "/home/an/git/Aneifer/vis_palmer_penguins_app/media/24_Palmer Penguins Species_Anna Neifer.png"
    st.image(
        image_path,
        caption="Illustration of the three species of penguins featured in the Palmer Penguins dataset. Source: Allison Horst.",
        use_column_width=True,
    )

    st.subheader("Penguins? What is it all about?")
    st.markdown(
        """
        This app demonstrates the capabilities of the Palmer Penguins dataset, a popular resource for data analysis and visualization. Developed as part of a project at the Data Science Retreat in Berlin, the app showcases how Streamlit, an open-source framework, can be used for creating interactive and insightful data visualizations.

        Users can upload datasets, specifically the Palmer Penguins dataset, to explore various visualizations and gain insights into the data. This dataset was chosen for its simplicity and diversity, making it ideal for exploratory data analysis and machine learning demonstrations.
        """
    )

if __name__ == "__main__":
    main()

