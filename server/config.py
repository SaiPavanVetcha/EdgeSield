import os
from dotenv import load_dotenv

load_dotenv()

# Server Settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))

# Databricks Settings
DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

# Clean host URL if user provided prefix or trailing slashes
if DATABRICKS_HOST and DATABRICKS_HOST.startswith("https://"):
    DATABRICKS_HOST = DATABRICKS_HOST.replace("https://", "")
if DATABRICKS_HOST and DATABRICKS_HOST.endswith("/"):
    DATABRICKS_HOST = DATABRICKS_HOST.rstrip("/")