import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def main():
    st.header("Penguins dataset", divider="blue")
    st.markdown(
        """
        The Palmer Penguins dataset contains data on three penguin species observed on three islands in the Palmer Archipelago, Antarctica. The dataset includes measurements such as bill length, flipper length, body mass, and more.

        More information about the dataset can be found on [this GitHub page](https://github.com/allisonhorst/palmerpenguins).
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
    st.subheader("Bill Length vs. Bill Depth")
    st.markdown(
    """
    This scatter plot visualizes the relationship between the bill length and bill depth for each species of penguin.
    By coloring the data points according to species, we can observe how these measurements differ between species.
    
    **Key Insights:**
    - **Adelie Penguins** tend to have shorter bill lengths and smaller bill depths compared to other species.
    - **Gentoo Penguins** generally exhibit longer bill lengths.
    - **Chinstrap Penguins** often show similar bill depths to Adelie but have longer bills.
    
    The scatter plot helps us to visually distinguish species based on their bill characteristics, which is important for identification and understanding species differences.
    """
    )
    plt.figure(figsize=(10, 6))
    facet = sns.FacetGrid(df, hue="species", height=6, palette="mako")
    facet.map(plt.scatter, "bill length (mm)", "bill depth (mm)").add_legend()
    st.pyplot(plt)

    st.subheader("Bill of a penguin")
    image_path = os.path.join("media", "24_Palmer Penguins_Bill length and depth_Anna Neifer.png")
    st.image(image_path, caption="Illustration explains bill length and depth of penguins. Source: Allison Horst.", use_column_width=True)

    st.subheader("Flipper Length by Species")
    st.markdown(
    """
    This violin plot shows the distribution of flipper lengths across the different penguin species. The width of each violin represents the density of penguins with a particular flipper length within a species.
    
    **Key Insights:**
    - **Gentoo Penguins** generally have longer flippers compared to Adelie and Chinstrap penguins, indicating a possible adaptation for efficient swimming.
    - **Adelie Penguins** show a wider range of flipper lengths compared to Chinstrap penguins, suggesting more variation within the species.
    
    The plot highlights the physical adaptations of different penguin species that may relate to their habitat and lifestyle.
    """
    )
    sns.color_palette("mako")
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="species", y="flipper length (mm)", data=df, palette="mako")
    st.pyplot(plt)

    st.subheader("Correlation between Body Mass and Flipper Length")
    
    correlation_value = df["body mass (g)"].corr(df["flipper length (mm)"])

    # Shows DataFrame with correlation matrixbetween body mass and flipper length.
    st.write("Correlation Matrix")
    st.write(df[["body mass (g)", "flipper length (mm)"]].corr())
    st.markdown(f"""
    **Interpretation of the Correlation**

    The correlation matrix shows a strong positive correlation between body mass and flipper length among penguin species. A correlation coefficient of **{correlation_value:.2f}** indicates that penguins with longer flippers tend to have a higher body mass.

    **Scatter Plot Analysis**

    Based on the strong correlation, I created a scatter plot to examine this relationship between body mass and flipper length more closely:

    **Key Insights:**
    - **Positive Correlation**: The scatter plot confirms a noticeable positive correlation between flipper length and body mass across all species.
    - **Gentoo Penguins**: These penguins are generally heavier and have longer flippers compared to other species, which might indicate differences in diet. 
    """
    )

    plt.figure(figsize=(10, 6))
    sns.color_palette("mako")
    facet = sns.FacetGrid(df, hue="species", height=6, palette="mako")
    facet.map(plt.scatter, "body mass (g)", "flipper length (mm)").add_legend()
    st.pyplot(plt)

    st.markdown("""
    **Ecological Significance**

    Understanding this correlation is important for ecological studies, as it may reflect penguins' ability to forage efficiently and adapt to their environment. These physical traits could be crucial for survival in their natural habitats, influencing their ability to dive deeper or swim longer distances to find food.
    """)
    
if __name__ == "__main__":
    main()

