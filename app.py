import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body

# load pages scripts

app = MultiPage(app_name= "Banking-Churnometer") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)

app.run() # Run the  app