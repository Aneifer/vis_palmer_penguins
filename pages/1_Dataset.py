import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.header("Penguins dataset", divider="blue")
    st.markdown(
        """
        The Palmer Penguins dataset contains data on three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The dataset includes measurements such as bill length, flipper length, body mass, and more.

        More information about the dataset can be found on the [Palmer Penguins dataset GitHub page](https://github.com/allisonhorst/palmerpenguins).
        """
    )
    # Load and display the dataset
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
    df.rename(
        columns={
            "bill_length_mm": "bill length (mm)",
            "bill_depth_mm": "bill depth (mm)",
            "flipper_length_mm": "flipper length (mm)",
            "body_mass_g": "body mass (g)",
        },
        inplace=True,
    )
    st.subheader("Peak into the dataset:")
    st.write(df.head())

    # Visualizations
    sns.color_palette("mako")
    st.subheader("Scatter Plot with Seaborn")
    plt.figure(figsize=(10, 6))
    facet = sns.FacetGrid(df, hue="species", height=6, palette="mako")
    facet.map(plt.scatter, "bill length (mm)", "bill depth (mm)").add_legend()
    st.pyplot(plt)

    image_path = "/home/an/git/Aneifer/vis_palmer_penguins/media/24_Palmer Penguins_Bill length and depth_Anna Neifer.png"
    st.image(image_path, caption="Illustration of the bill of penguins. Source: Allison Horst.", use_column_width=True)

    st.subheader("Violin Plot of Flipper Length by Species")
    sns.color_palette("mako")
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="species", y="flipper length (mm)", data=df, palette="mako")
    st.pyplot(plt)

    st.subheader("Correlation between body mass and flipper length")
    plt.figure(figsize=(10, 6))
    sns.color_palette("mako")
    facet = sns.FacetGrid(df, hue="species", height=6, palette="mako")
    facet.map(plt.scatter, "body mass (g)", "flipper length (mm)").add_legend()
    st.pyplot(plt)
    st.markdown(
        """Flipper length and body mass have the strongest correlation. Penguins with longer flippers tend to be heavier, suggesting that flipper length is a good predictor of body mass."""
    )

if __name__ == "__main__":
    main()

