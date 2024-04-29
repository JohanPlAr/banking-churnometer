import streamlit as st
import pandas as pd
from src.data_management import load_bank_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_churn,
    predict_tenure,
    predict_cluster)


def page_prospect_body():

    # load predict churn files
    version = 'v1'
    churn_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    churn_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_model.pkl")
    churn_features = (pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    # load predict tenure files
    version = 'v1'
    tenure_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    tenure_features = (pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    # load cluster analysis files
    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.write("### Prospect Churnometer Interface")
    st.info(
        f"* Choosing variable values will determine whether or not a given prospect will churn. "
        f"If prospect is predicted to churn a predicted prospect tenure is presented, in addition,"
        f"a cluster analysis is displayed, enabling learning from which cluster "
        f"this prospect will belong in the customer base."
        f"Based on that, the potential factors that could maintain and/or bring  "
        f"the prospect to a non-churnable cluster is presented."
    )
    st.write("---")

    # Generate Live Data
    # check_variables_for_UI(tenure_features, churn_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        churn_prediction = predict_churn(
            X_live, churn_features, churn_pipe_dc_fe, churn_pipe_model)

        if churn_prediction == 1:
            predict_tenure(X_live, tenure_features,
                           tenure_pipe, tenure_labels_map)

        predict_cluster(X_live, cluster_features,
                        cluster_pipe, cluster_profile)


def check_variables_for_UI(tenure_features, churn_features, cluster_features):
    import itertools

    # The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
    # Combined features with unique values only
    combined_features = set(
        list(
            itertools.chain(tenure_features, churn_features, cluster_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")

def DrawInputsWidgets():

    # load dataset
    df = load_bank_data()
# we create input widgets only for 8 features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)
    col7, col8, = st.beta_columns(2)

    # Features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])
    # Widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "NumOfProducts"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "Balance"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()),
            max_value=int(df[feature].max()),
            value=int(df[feature].median()),
            step=5000
            )
    X_live[feature] = st_widget

    with col3:
        feature = "Age"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()),
            max_value=int(df[feature].max()),
            value=int(df[feature].median()),
            step=5
        )
    X_live[feature] = st_widget

    with col4:
        feature = "CreditScore"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()),
            max_value=int(df[feature].max()),
            value=int(df[feature].median()),
            step=25
        )
    X_live[feature] = st_widget

    with col5:
        feature = "EstimatedSalary"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()),
            max_value=int(df[feature].max()),
            value=int(df[feature].median()),
            step=5000
        )
    X_live[feature] = st_widget

    with col6:
        feature = "Tenure"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()),
            max_value=int(df[feature].max()),
            value=int(df[feature].median()),
            step=1  # Set the step size to 0.1 for float values
        )
    X_live['TenureByAge'] = st_widget/X_live['Age']

    with col7:
        feature = "Gender"
        st_widget = st.selectbox(
        label=feature,
        options=["Male", "Female"],
        )
    if st_widget == "Male":
        X_live[feature] = 0
    else:
        X_live[feature] = 1

    with col8:
        feature = "Geography"
        st_widget = st.selectbox(
        label=feature,
        options=df[feature].unique()
        )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live