# <i>Implémentez un modèle de scoring</i>
### OpenClassrooms - Data Scientist diploma (Master's level diploma) - Project # 7

## Goal(s)

- conceiving, raining and testing a model, which predicts, wheter a given loan applicant will be able to repay (on time) all loan installments or not;
- deploying a <a href="https://bankscoring.streamlit.app/">web application</a> (<a href="https://bankscoring.streamlit.app/">Default risk calculator</a>), which implements such model;

## Main output(s)

- a Jupyter <a href="https://github.com/biancof/oc_bank_scoring/blob/main/notebook_modelization.ipynb">Notebook</a> of data cleaning, exploration and modelization;
- an HTML <a href="https://github.com/biancof/oc_bank_scoring/blob/main/data_drift_report.html">data drift report</a>;
- an <a href="https://biancof.pythonanywhere.com/">Application Programming Interface</a> (API);
- a <a href="https://github.com/biancof/oc_bank_scoring/blob/main/test_api.py">unit test script</a>;
- an <a href="https://bankscoring.streamlit.app/">interactive dashboard</a>;

## Repository branches

- <a href="https://github.com/biancof/oc_bank_scoring/tree/main/">main</a>: dashboard and API in cloud version;
- <a href="https://github.com/biancof/oc_bank_scoring/tree/local/">local</a>: dashboard and API in local version.

## Languages and frameworks

The used scripting language is <i>Python</i>.
Main frameworks:
- <a href="https://shap.readthedocs.io/">SHAP</a>: for the feature importance analysis;
- <a href="evidentlyai.com">Evidently</a>: for the data drift analysis;
- <a href="https://flask.palletsprojects.com/">Flask</a>: for the API;
- <a href="https://streamlit.io/">Streamlit</a>: for the dahsboard;
- <a href="https://plotly.com/">Plotly</a>: for the gauge chart (in the dashboard).

## Web application architecture

The interactive dashboard is web application running on <a href="share.streamlit.io/">Streamlit share cloud system</a>. Source code comes directly from this GitHub repository.
The API is hosted on <a href="https://www.pythonanywhere.com/">PythonAnywhere cloud system</a>. The API provides, on HTTP request (sent by the dashboard), clients data and predictions on loan repay probabilities.

## Documents

- <a href="https://github.com/biancof/oc_bank_scoring/blob/main/doc/presentation.pptx">Power point presentation</a> (in French);
- <a href="https://github.com/biancof/oc_bank_scoring/blob/main/doc/note_methodologique.pdf">Methodological notes</a>. (in French)

## Links

- Data source: https://www.kaggle.com/c/home-credit-default-risk/data 
- Kernels Kaggle (for data cleaning, exploration and engeneering):
  - https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction;
  - https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/script;
- Dashboard: https://bankscoring.streamlit.app
- API: https://biancof.pythonanywhere.com