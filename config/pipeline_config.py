# pipeline_config.py — Pipeline Configuration Variables
# Single source of truth for all medallion pipeline paths and settings

BASE_PATH = "/Volumes/workspace/default/olist_data"
BRONZE_PATH = f"{BASE_PATH}/bronze"
SILVER_PATH = f"{BASE_PATH}/silver"
GOLD_PATH = f"{BASE_PATH}/gold"

SOURCE_FILE = f"{BASE_PATH}/olist_customers_dataset.csv"

SILVER_SCD_TABLE = "default.silver_customers_scd"
GOLD_CURRENT_TABLE = "default.gold_customer_current"
GOLD_HISTORY_TABLE = "default.gold_customer_history"
WATERMARK_TABLE = "default.pipeline_watermarks"

SCD_TRACKED_COLUMNS = ["customer_zip_code_prefix", "customer_city", "customer_state"]

PIPELINE = {
    "source_table": "olist_customers",
    "natural_key": "customer_unique_id",
    "batch_id": "batch_1"
}
