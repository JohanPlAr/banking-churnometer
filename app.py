import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_churned_customer_study import page_churned_customer_study_body

# load pages scripts

app = MultiPage(app_name= "Banking-Churnometer") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Customer Base Churn Study", page_churned_customer_study_body)
app.add_page("Prospect Churnometer", page_summary_body)
app.add_page("ML: Prospect Churn", page_summary_body)
app.add_page("ML: Prospect Tenure", page_summary_body)
app.add_page("ML: Cluster Analysis", page_summary_body)

app.run() # Run the  app