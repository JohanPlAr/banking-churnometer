import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_bank_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_churned_customer_study_body():

    # load data
    df = load_bank_data()
    # hard copied from churned customer study notebook
    vars_to_study = [
                     'Age',
                     'Balance',
                     'Gender',
                     'Geography',
                     'IsActiveMember',
                     'NumOfProducts'
                     ]

    st.write("### Churned Customer Study")
    st.info(
        f"* Study conducted in order to understand the patterns from the customer base "
        f" and present the most relevant variables correlated to a churned customer.")

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['Exited'])
    # Change value names in studied variable for better ux.
    df_eda['Gender'] = df_eda['Gender'].replace({0: 'Male', 1:"Female"})
    # Change to object variable to plot categorical
    df_eda['NumOfProducts'] = df_eda['NumOfProducts'].astype(object)
    df_eda['IsActiveMember'] = df_eda['IsActiveMember'].replace({0: 'Not Active', 1:"Active"})
    # Individual plots per variable
    if st.checkbox("Churn Levels per Variable"):
        churn_level_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a churned customer"
            )
        parallel_plot_churn(df_eda)
            # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
    "Interpretation of correlation indications and plots above gives: \n"
    "It is indicated that:\n"
    "- A churned customer is typically in the range between 47 and 58 years old.\n"
    "- A churned customer typically has a mid-range or higher account Balance.\n"
    "- A churned customer is typically Female.\n"
    "- A churned customer is typically from Germany.\n"
    "- A churned customer typically has 1 or 3-4 Number of Products.\n"
    "- A churned customer is typically not an Active Member."
    )


# function created using "02 - Churned Customer Study" notebook code - "Variables Distribution by Churn" section
def churn_level_per_variable(df_eda):
    target_var = 'Exited'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# function created using "02 - Churned Customer Study" notebook code - Parallel Plot section
def parallel_plot_churn(df_eda):

    # hard coded from "disc.binner_dict_['Age','Balance']"" result,
    age_map = [-np.Inf, 35, 47, 58, np.Inf]
    balance_map = [-float('Inf'), 75000, 125000, float('Inf')]
    disc = ArbitraryDiscretiser(binning_dict={'Age':age_map, 'Balance': balance_map})
    # found at "02 - Churned Customer Study" notebook
    # under "Parallel Plot" section
    disc = ArbitraryDiscretiser(binning_dict={'Age':age_map, 
                                              'Balance': balance_map})
    df_parallel = disc.fit_transform(df_eda)
    def labels_map(col_data_map, col_data):
        n_classes = len(col_data_map) - 1
        classes_ranges = disc.binner_dict_[col_data][1:-1]
        labels_map = {}
        for n in range(0, n_classes):
            if n == 0:
                labels_map[n] = f"<{classes_ranges[0]}"
            elif n == n_classes-1:
                labels_map[n] = f"+{classes_ranges[-1]}"
            else:
                labels_map[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"
        labels_map
        return labels_map

    df_parallel['Age'] = df_parallel['Age'].replace(labels_map(age_map,'Age'))
    df_parallel['Balance'] = df_parallel['Balance'].replace(labels_map(balance_map,'Balance'))
    fig = px.parallel_categories(
        df_parallel, color="Exited", width=750, height=500)
    st.info('In Exited \n '
            '- 1 = "Churned"\n' 
            '- 0 = "Not Churned"')
    st.plotly_chart(fig)