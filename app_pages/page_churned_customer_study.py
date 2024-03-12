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
    vars_to_study = ['Age','Balance','CreditScore','EstimatedSalary', 'Gender', 'Geography', 'IsActiveMember', 'NumOfProducts','Tenure']

    st.write("### Churned Customer Study")
    st.info(
        f"* The client is interested in understanding the patterns from the customer base "
        f"so that the client can learn the most relevant variables correlated "
        f"to a churned customer.")

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

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"A churned customer typically is older than 40. \n"
        f"A churned customer typically has a mid-range or higher account Balance. \n"
        f"A churned customer typically is Female. \n"
        f"A churned customer typically is German. \n"
        f"A churned customer typically has 0 Number of Products. \n"
        f"A churned customer typically is not an Active Member. \n"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['Exited'])

    # Individual plots per variable
    if st.checkbox("Churn Levels per Variable"):
        churn_level_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a churned customer"
            )
        parallel_plot_churn(df_eda)


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

    # hard coded from "disc.binner_dict_['tenure']"" result,
    tenure_map = [-np.Inf, 2, 7, np.Inf]
    age_map = [-np.Inf, 35, 40, np.Inf]
    num_of_prods_map = [-np.Inf, 1, np.Inf]
    balance_map = [-float('Inf'), 25000, 125000, float('Inf')]
    # credit_score_map = [-float('Inf'), 600, 700, float('Inf')]
    estimated_salary_map = [-float('Inf'), 50000, 100000, 150000, 200000, float('Inf')]
    # found at "02 - Churned Customer Study" notebook
    # under "Parallel Plot" section
    disc = ArbitraryDiscretiser(binning_dict={'Age':age_map, 
                                              'Balance': balance_map,
                                            #   'CreditScore':credit_score_map, 
                                            #   'EstimatedSalary': estimated_salary_map, 
                                              'Tenure':tenure_map,
                                              'NumOfProducts':num_of_prods_map})
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
    # df_parallel['EstimatedSalary'] = df_parallel['EstimatedSalary'].replace(labels_map(estimated_salary_map,'EstimatedSalary'))
    # df_parallel['CreditScore'] = df_parallel['CreditScore'].replace(labels_map(credit_score_map,'CreditScore'))
    df_parallel['Tenure'] = df_parallel['Tenure'].replace(labels_map(tenure_map,'Tenure'))
    fig = px.parallel_categories(
        df_parallel, color="Exited", width=750, height=500)
    # we use st.plotly_chart() to render, in notebook is fig.show()
    st.plotly_chart(fig)