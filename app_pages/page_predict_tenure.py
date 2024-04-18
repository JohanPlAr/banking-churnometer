import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_bank_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_predict_tenure_body():

    # load tenure pipeline files
    version = 'v1'
    tenure_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    label_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    tenure_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Prospect Tenure")
    # display pipeline training summary conclusions
    st.info(
        f"A Classifier was picked as ML-model as neither Regression \
            or Regression with PCA was able to reach Business Requirements \
        of R2 Score of 70% on Train and test sets or 80% Recall on Train and \
        Test set for the shortest Tenure period possible. In order to reach \
        criteria the Tenure variable was binned in two categories. '0 to 5 \
        years' or 'more than 5 years'.")
    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict tenure when prospect is expected to churn.")
    st.write(tenure_pipe)
    st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(tenure_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=tenure_pipe,
                    label_map=label_map)