 
import os

# Define the root directory of the project
root_dir = "real_time_processing_project"

# Create the directory structure
os.makedirs(os.path.join(root_dir, "kinesis"))
os.makedirs(os.path.join(root_dir, "airflow", "dags"))
os.makedirs(os.path.join(root_dir, "streamlit"))

# Define the file extensions for the empty files
kinesis_ext = ".json"
airflow_ext = ".py"
streamlit_ext = ".py"

# Create the empty files
open(os.path.join(root_dir, "kinesis", "data" + kinesis_ext), "w").close()
open(os.path.join(root_dir, "airflow", "dags", "etl_pipeline" + airflow_ext), "w").close()
open(os.path.join(root_dir, "streamlit", "dashboard" + streamlit_ext), "w").close()
