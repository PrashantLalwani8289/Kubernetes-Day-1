from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 3, 25),
}

dag = DAG(
    dag_id='pyspark_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
)

spark_task = SparkSubmitOperator(
    task_id='run_spark_job',
    application='local:///app/pyspark_pipeline.py',
    conn_id='spark_default',
    dag=dag,
)

spark_task
