import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"* We suspect customers are churning with low engagement (Not Active Members): Correct. "
        f"The correlation study at Churned Customer Study supports that. \n\n"
        f"* We suspect that customers using fewer products(1-2) are churning: False.\n"
        f"The correlation study at Churned Customer Study identifies higher Churn ratio in\n"
        f"1 used product rather than 2 but especially high level of churn in 3-4 which is\n"
        f"worth investigating further\n"
        f"* We suspect midage customers are more likely to Churn: Correct\n"
        f"The correlation study at Churned Customer Study supports that."
    )   