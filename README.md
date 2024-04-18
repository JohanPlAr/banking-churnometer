![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## About Dataset

- The dataset is sourced from Kaggle. A fictitious user story was created where predictive analytics can be applied in a real project in the workplace.

- The bank customer churn dataset is a commonly used dataset for predicting customer churn in the banking industry. It contains information on bank customers who either left the bank or continue to be a customer. The dataset has 10 000 rows and includes the following attributes:

- Customer ID: A unique identifier for each customer
- Surname: The customer's surname or last name
- Credit Score: A numerical value representing the customer's credit score
- Geography: The country where the customer resides (France, Spain, or Germany)
- Gender: The customer's gender (Male or Female)
- Age: The customer's age
- Tenure: The number of years the customer has been with the bank
- Balance: The customer's account balance
- NumOfProducts: The number of bank products the customer uses (e.g., savings account, credit card)
- HasCrCard: Whether the customer has a credit card (1 = yes, 0 = no)
- IsActiveMember: Whether the customer is an active member (1 = yes, 0 = no)
- EstimatedSalary: The estimated salary of the customer
- Exited: Whether the customer has churned (1 = yes, 0 = no)


## Business Requirements
* Our bank is facing a significant challenge with customer churn, which is negatively impacting our revenue and growth. To address this issue, we require a robust predictive analysis solution that can accurately identify customers who are likely to churn.

## Hypothesis and how to validate?
* We suspect that active customers 

## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
- What are the business requirements?
The client interested in understanding first of all if but also why customers are likely to churn. Therefore, the client expects visualizations of the correlated variables against churned customers and an algoritm based churned predictor. The Client also wants to preidict the likely Tenure when a customer is predicted to churn. Also the client wish to conduct a Cluster analysis to better understand if there are any potential groupings of the customers that can improve marketing strategies.

- Is there any business requirement that can be answered with conventional data analysis?
Yes, we can use conventional data analysis to investigate the correlation between variables and churned customers.
- Does the client need a dashboard or an API endpoint?
The client needs a dashboard.
- What does the client consider as a successful project outcome?
A customer prospect churn prediction relying on a machine learning model. A predict Tenure Model implemented with the predict churn model to help the client identify high risk churning. A cluster Study with to identify groups of customers that might benefit marketing strategies. 
- Can you break down the project into Epics and User Stories?
Information gathering and data collection.
Data visualization, cleaning, and preparation.
Model training, optimization and validation.
Dashboard planning, designing, and development.
Dashboard deployment and release.
- Ethical or Privacy concerns?
No. The client found a public dataset.
- Does the data suggest a particular model?
The data suggests a classifier where the target is to classify either churned or not churned prospect customers. This also applies for the Cluster Study.
- What are the model's inputs and intended outputs?
The inputs are information aboutg the customer prospect and the output is the churn prediction.
What are the criteria for the performance goal of the predictions?
We agreed with the client on an Recall score of at least 0.80 on the train set as well as on the test set.
How will the client benefit?
- Reduce Customer Churn through identification of customers at risk of churning, enabling proactive retention strategies and reducing overall customer attrition.
- Improve Customer Lifetime Value the client can retain more customers and aim to increase the average customer lifetime value, leading to higher revenue and profitability.
- Enhance Targeted Marketing Campaigns: The predictive model will provide valuable insights to tailor our marketing efforts and personalize offers, leading to more effective customer engagement and retention.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
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
- Info text
* ML: Prospect Churn
- Pipeline Details and performance data
* ML: Predict Tenure
- Pipeline Details and performance data
* ML: Cluster Analysis
- Plots of Feature Importance, Cluster Silhoutte and Pipeline


## Unfixed Bugs
* No infixed Bugs

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
streamlit==0.85.0 # Streamlit app
plotly==4.12.0 # Data visualization library
altair<5 # Data visualization library
pandas==1.4.2 # Data manipulation and analysis library
ydata-profiling==4.4.0 # Data Exploration and Variable Distribution analysis
ipywidgets==8.0.2 # Data Exploration Widgets
scikit-learn==0.24.2 # Machine Learning library for tasks like OneHotEncoding, etc.
feature-engine==1.0.2 # Feature engineering library for correlation analysis
matplotlib==3.3.1 # Data visualization library for correlation analysis
seaborn==0.11.0 # Data visualization library
ppscore==1.2.0 # PPS (Predictive Power Score) package
imbalanced-learn==0.8.0 # Library for handling imbalanced datasets, including SMOTE
yellowbrick==1.3 # Visualization library for machine learning models

## Credits 

* Kaggle for offering the dataset
* Code Institute for educational material and especially for the walkthrough project
Churnometer which was the main inspiration for this project. The Streamlit banking-churnometer app was developed following this example.

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Code 

