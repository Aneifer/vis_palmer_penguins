import streamlit as st
import pandas as pd
import altair as alt

def main():
    st.header("Visual Interaction", divider="blue")
    st.write("Please upload the penguin CSV file. You can find the dataset ")
    st.markdown(
        "[here](https://github.com/tylerjrichards/Streamlit-for-Data-Science/blob/main/penguin_app/penguins.csv).",
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader("", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            required_columns = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "flipper_length_mm",
                "body_mass_g",
                "sex",
            ]
            if all(column in df.columns for column in required_columns):
                st.write(df)

                st.subheader("Interactive Scatter Plot with Altair")
                numeric_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
                x_axis = st.selectbox(
                    "Choose X axis",
                    options=numeric_columns,
                    index=numeric_columns.index("flipper_length_mm"),
                )
                y_axis = st.selectbox(
                    "Choose Y axis",
                    options=numeric_columns,
                    index=numeric_columns.index("body_mass_g"),
                )
                color_var = st.selectbox(
                    "Choose Color Variable",
                    options=["species", "sex"],
                    index=0,
                )

                scatter_chart = (
                    alt.Chart(df)
                    .mark_circle(size=60)
                    .encode(x=x_axis, y=y_axis, color=color_var, tooltip=list(df.columns))
                    .interactive()
                )

                st.altair_chart(scatter_chart, use_container_width=True)
            else:
                st.error(
                    "Sorry, but this seems to be the wrong CSV file. Please check if you uploaded the Palmer Penguins data."
                )
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}. Please ensure you upload a valid CSV file.")

if __name__ == "__main__":
    main()

