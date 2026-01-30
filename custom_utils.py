from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.window import Window

class transformationss:
    def dedup(self, df:DataFrame, dedup_cols:List, cdc:str):
        df = df.withColumn("dedupKey", concat(*[col(c) for c in dedup_cols]))
        df = df.withColumn("dedupCounts", row_number()\
                           .over(Window.partitionBy("dedupKey").orderBy(desc(col(cdc)))))
        df = df.filter(col('dedupCounts')==1)
        df = df.drop("dedupKey","dedupCounts")
        return df
    def process_timestamp(self, df):


        df = df.withColumn("process_timestamp", current_timestamp())

        return df
    def upsert(self,df,key_cols,table,cdc):
        merge_condition = " AND ".join([f"src.{i} = trg.{i}" for i in key_cols])
        dlt_obj = DeltaTable.forName(f"pyspark.silver.{table}")
        dlt_obj.alias("trg").merge(df.alias("src"),merge_condition)\
            .whenMatchedupdateAll(condition = "src.{cdc}} >= trg.{cdc}")\
            .whenNotMatchedinsertAll()\
                .execute()
        return 1        
