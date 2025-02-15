import streamlit as st
import os

def main():
    st.header("About the Penguin App", divider="blue")
    image_path = os.path.join("media", "24_Palmer Penguins Species_Anna Neifer.png")
    st.image(
        image_path,
        caption="Illustration of the three species of penguins featured in the Palmer Penguins dataset. Source: Allison Horst.",
        use_container_width=True,
    )

    st.subheader("Penguins? What is it all about?")
    st.markdown(
    """
    **Palmer Penguins:**
    
    These three adorable penguins—Chinstrap, Gentoo and Adelie—are the stars of the Palmer Penguins dataset, a popular resource for data analysis and visualization. 
    This dataset provides insights into the physical characteristics of these species, collected from the Palmer Archipelago in Antarctica.

    **Hey, I'm Anna:**

    I'm a data scientist and journalist and passionate about creating visualizations that make data accessible and engaging. Find my [Github Profile here](https://github.com/Aneifer).

    **Project at Data Science Retreat:**

    I developed this app as part of a project at the Data Science Retreat in Berlin, and I've been enhancing it since summer 2024. 
    The Penguin App is built with Streamlit, an open-source framework that enables the creation of prototypes and data visualisations.
    """
    )

if __name__ == "__main__":
    main()

