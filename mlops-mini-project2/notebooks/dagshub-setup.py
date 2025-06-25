import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/amit5631/mlops-mini-project2.mlflow')
dagshub.init(repo_owner='amit5631', repo_name='mlops-mini-project2', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)