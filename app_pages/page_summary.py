import streamlit as st
import plotly.express as px

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is a person who consumes your service or product.\n"
        f"* A **prospect** is a potential customer.\n"
        f"* A **churned** customer is a user who has stopped using your product or service.\n "
        f"* This customer has a **tenure** level, the number of years this person " 
        f"has used our product/service.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents a **customer base from a Banking company** "
        f"containing individual customer data on the products and services "
        f"(like, Has Credit Card, Number Of Products, Is Active Member, Tenure), "
        f"account information (like Credit Score, Balance, Estimated Salary) "
        f"and profile (like Gender, Age, Geography).")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/JohanPlAr/banking-churnometer/blob/main/README.md).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 3 business requirements:\n"
        f"* 1 - Understand the patterns from the customer base "
        f"so that the client can learn the most relevant variables that are correlated to a "
        f"churned customer.\n"
        f"* 2 - Determine whether or not a given prospect will churn.\n"
        f"If so, the client is interested to know when.\n" 
        f"* 3 - Cluster Analysis of Churned Prospect\n"
        f"Present learnings from which cluster the prospect will belong in the customer base. "
        f"Based on that, present potential factors that could maintain and/or bring  "
        f"the prospect to a non-churnable cluster."
        )