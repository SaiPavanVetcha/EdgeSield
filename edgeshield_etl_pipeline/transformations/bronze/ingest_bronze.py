from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp

SOURCE_CATALOG = spark.conf.get("edgeshield.source_catalog", "workspace")
SOURCE_SCHEMA = spark.conf.get("edgeshield.source_schema", "edgeshield_db")
TARGET_CATALOG = spark.conf.get("edgeshield.target_catalog", "edgeshield_lakehouse")
TARGET_SCHEMA = spark.conf.get("edgeshield.target_schema", "bronze")

BRONZE_TABLE_PROPERTIES = {
    "quality": "bronze",
    "layer": "bronze",
    "delta.enableChangeDataFeed": "true",
    "delta.autoOptimize.optimizeWrite": "true",
    "delta.autoOptimize.autoCompact": "true"
}

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.environment_metrics",
    comment="Incremental raw ingestion for Environment Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def environment_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.environment_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.system_metrics",
    comment="Incremental raw ingestion for System Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def system_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.system_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.cpu_metrics",
    comment="Incremental raw ingestion for CPU Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def cpu_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.cpu_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.ram_metrics",
    comment="Incremental raw ingestion for RAM Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def ram_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.ram_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.disk_metrics",
    comment="Incremental raw ingestion for Disk Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def disk_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.disk_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )

@dp.table(
    name=f"{TARGET_CATALOG}.{TARGET_SCHEMA}.battery_metrics",
    comment="Incremental raw ingestion for Battery Metrics",
    table_properties=BRONZE_TABLE_PROPERTIES
)
def battery_metrics_bronze():
    return (
        spark.readStream
        .format("delta")
        .option("skipChangeCommits", "true")
        .table(f"{SOURCE_CATALOG}.{SOURCE_SCHEMA}.battery_metrics")
        .withColumn("_ingested_at", current_timestamp())
    )