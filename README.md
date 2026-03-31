### Fraud detection ###

### Task ###

* Binary classification of fraudulent transactions (3.5% fraud rate)
* 590k+ transactions, 400+ features (IEEE-CIS dataset)

### Model ###

* Meta-algorithm: LightGBM + XGBoost + CatBoost (stacking)
* SMOTE + class weights for imbalance handling
* Bayesian hyperparameter optimization

### Result ###

* Recall: 87% (87 of 100 frauds caught)
* False positives: 154 per 1000 transactions

### Dashboard ###

* FastAPI + Streamlit
* Card search by ID with transaction history
* Fraud probability visualization
* Risk factor explanation for each transaction
