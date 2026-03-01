import os
import datetime

####### CREDENTIAlS #######
# ChatGPT
GPT_API_KEY = os.environ.get("GPT_API_KEY")
GPT_ORG_ID = os.environ.get("GPT_ORG_ID")

# GCP
PROJECT_ID = os.environ.get("PROJECT_ID")
BQ_DATASET = os.environ.get("BQ_DATASET")
RAW_TABLE = os.environ.get("RAW_TABLE")
PROCESSED_TABLE = os.environ.get("PROCESSED_TABLE")
