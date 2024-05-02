## Table of Content

- [About Dataset](#about-dataset)
- [Business Requirements](#business-requirements)
- [Project hypothesis and validation](#project-hypothesis-and-validation)
- [Rationale to map the business requirements to the Data Visualizations and ML tasks](#rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment to Heroku](#deployment-to-heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)

## About Dataset

- The dataset is sourced from Kaggle. A fictitious user story was created where predictive analytics can be applied in a real project in the workplace.

- The bank customer churn dataset is a commonly used dataset for predicting customer churn in the banking industry. It contains information on bank customers who either left the bank or continue to be a customer. The dataset has 10 000 rows and includes the following attributes:

| Variable | Meaning | Units |
|----------|---------|-------|
| RowNumber | A unique identifier for each row | 10000 |
| Customer ID | A unique identifier for each customer | 10000 |
| Surname | The customer's surname or last name | 2932 Surnames |
| Credit Score | A numerical value representing the customer's credit score | 352-827 |
| Geography | The country where the customer resides | France, Spain, or Germany |
| Gender | The customer's gender | Male or Female |
| Age | The customer's age | 22-92 Years |
| Tenure | The number of years the customer has been with the bank | 0-10 Years |
| Balance | The customer's account balance | 0-247198 Currency |
| NumOfProducts | The number of bank products the customer uses (e.g., savings account, credit card) | 1-4 Products |
| HasCrCard | Whether the customer has a credit card | 1 = yes, 0 = no |
| IsActiveMember | Whether the customer is an active member | 1 = yes, 0 = no |
| EstimatedSalary | The estimated salary of the customer | 193-195193 Currency |
| Exited | Whether the customer has churned| 1 = yes, 0 = no |

[Back to Table of content](#table-of-content)

## Business Requirements
* Our bank is facing a significant challenge with customer churn, which is negatively impacting our revenue and growth. To address this issue, we require a robust predictive analysis solution that can accurately identify customers who are likely to churn.

[Back to Table of content](#table-of-content)

## Project Hypothesis and Validation
* We suspect customers are churning with low engagement (Not Active Members)
    - Run Customer Base Churn Study and produce relevant plots
* We suspect that customers using fewer products(1-2) are churning
    - Run Customer Base Churn Study and produce relevant plots
* We suspect midage customers are more likely to Churn
    - Run Customer Base Churn Study and produce relevant plots

[Back to Table of content](#table-of-content)

## Rationale to map the business requirements to the Data Visualizations and ML tasks
* Business requirement 1: Correlation study and data visualization
- As a client I want to inspect the Customer data so that I can get an idea of which variables are important for the churning.
- As a client I want to display a heatmap of the spearman correlation coefficients so that I can order the variables by importance concerning churn.
- As a client I want to plot the important variables against the churn variable so that I can visualize how such a variable is correlated with churn.
Business requirement 2: Predict prospect churn risk and tenure 
As a client I want to select variable values I can easily produce a prospect customer.
As a client I want to use an ML model so that I can predict a prospects risk of churning.
As a client I want to use the ML model so that I can predict Tenure of the churning prospect.
Business Requirement 3: Cluster Analysis on prospect
As a client I want to use a ML Clustering model so that I can find patterns in the customer base that will help me take actions to reduce churn risk.

[Back to Table of content](#table-of-content)

## ML Business Case
1. What are the business requirements?
    - The client interested in understanding first of all if but also why customers are likely to churn. Therefore, the client expects visualizations of the correlated variables against churned customers and an algoritm based churned predictor. 
    - The Client also wants to preidict the likely Tenure when a customer is predicted to churn. 
    - The Client also wishes to conduct a Cluster analysis to better understand if there are any potential groupings of the customers that can improve marketing strategies.

2. Is there any business requirement that can be answered with conventional data analysis?
    - Yes, we can use conventional data analysis to investigate the correlation between variables and churned customers.
3. Does the client need a dashboard or an API endpoint?
    - The client needs a dashboard.
4. What does the client consider as a successful project outcome?
    - A customer prospect churn prediction relying on a machine learning model. A predict Tenure Model implemented with the predict churn model to help the client identify high risk churning. 
    - A cluster Study to identify groups of customers that might benefit of marketing strategies. 
5. Can you break down the project into Epics and User Stories?
    - Information gathering and data collection.
    - Data visualization, cleaning, and preparation.
    - Model training, optimization and validation.
    - Dashboard planning, designing, and development.
    - Dashboard deployment and release.
6. Ethical or Privacy concerns?
    - No, The client found a public dataset.
7. Does the data suggest a particular model?
    - The data suggests a classifier where the target is to classify either churned or not churned prospect customers. This also applies for the Cluster Study.
8. What are the model's inputs and intended outputs?
    - The inputs are information about the customer prospect and the output is the churn prediction.
9. What are the criteria for the performance goal of the predictions?
    - We agreed with the client on an Recall score of at least 0.80 on the train set as well as on the test set.
10. How will the client benefit?
    - Reduce Customer Churn through identification of customers at risk of churning, enabling proactive retention strategies and reducing overall customer attrition.
    - Improve Customer Lifetime Value the client can retain more customers and aim to increase the average customer lifetime value, leading to higher revenue and profitability.
    - Enhance Targeted Marketing Campaigns: The predictive model will provide valuable insights to tailor our marketing efforts and personalize offers, leading to more effective customer engagement and retention.

[Back to Table of content](#table-of-content)

## Dashboard Design
    
[More details with images on App Design here:](APPIMAGES.md)

* Quick Project Summary
    - Project Terms & Jargon, Business Requirements
* Customer Base Churn Study
    - Inspect Customer Base - displays sample of the Dataset
    - Churn Levels per Variable - displays the variables target value distribution  
    - Parallel plot - displays the most correlated variables against target values 
* Prospect Churnometer 
    - Prospect Churnometer Interface - streamlit widgets to add prospect variable values
    - Churn prediction and Cluster Analysis 
* Project Hypothesis and Validation
    - Hypothesis page
* ML: Prospect Churn
    - Pipeline Details and performance data
* ML: Predict Tenure
    - Pipeline Details and performance data
* ML: Cluster Analysis
    - Plots of Feature Importance, Cluster Silhoutte and Pipeline

[Back to Table of content](#table-of-content)

## Unfixed Bugs
* No unfixed Bugs

[Back to Table of content](#table-of-content)

## Deployment
### Heroku

* The App live link is: https://banking-churnometer-bf774a6cbd58.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

[Back to Table of content](#table-of-content)

## Main Data Analysis and Machine Learning Libraries

* streamlit==0.85.0 # Streamlit app
* plotly==4.12.0 # Data visualization library
* altair<5 # Data visualization library
* pandas==1.4.2 # Data manipulation and analysis library
* ydata-profiling==4.4.0 # Data Exploration and Variable Distribution analysis
* ipywidgets==8.0.2 # Data Exploration Widgets
* scikit-learn==0.24.2 # Machine Learning library for tasks like OneHotEncoding, etc.
* feature-engine==1.0.2 # Feature engineering library for correlation analysis
* matplotlib==3.3.1 # Data visualization library for correlation analysis
* seaborn==0.11.0 # Data visualization library
* ppscore==1.2.0 # PPS (Predictive Power Score) package
* imbalanced-learn==0.8.0 # Library for handling imbalanced datasets, including SMOTE
* yellowbrick==1.3 # Visualization library for machine learning models

[Back to Table of content](#table-of-content)

## Credits 
* Kaggle for offering the dataset and for Kaggle users that shared different approaches to dataset analysis. 
* Code Institute for educational material and especially for the walkthrough project
Churnometer which was the main inspiration for this project. The Streamlit banking-churnometer app was developed following this example and the code for this project were in some parts largely adaptions of this project.
* Perplexity.ai for the ability to quickly find the relevant Machine Learning segments and links.
* My Code Institute Mentor Preciuos Ijege for support and guidance throughout the project.

[Back to Table of content](#table-of-content)