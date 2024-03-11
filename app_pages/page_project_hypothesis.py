import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"* We suspect customers are churning with low tenure levels: Correct. "
        f"The correlation study at Churned Customer Study supports that. \n\n"
    )