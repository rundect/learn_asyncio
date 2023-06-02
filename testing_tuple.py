import os

CONNECTOR_FOLDER = '/home/airflow/PycharmProjects/Orchestrator/tests/files/connectors'
old_norm_abs_path = '/home/airflow/PycharmProjects/Orchestrator/tests/files/connectors'
new_norm_abs_path = '/home/airflow/PycharmProjects/Orchestrator/tests/files/connectorstest_connector_1'


if os.path.normpath(CONNECTOR_FOLDER) in (old_norm_abs_path, new_norm_abs_path):
    print('catch it')
