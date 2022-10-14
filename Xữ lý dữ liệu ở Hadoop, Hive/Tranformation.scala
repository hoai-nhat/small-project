import org.apache.spark.sql.{SaveMode,SparkSession}
import org.apache.spark.functions._

object Tranfomation{
    def main(args: Array[String]) = {
        // get argument
        var executionDate = ""
        args.sliding(2,2).toList.collect{
            case Array("--executionDate", argExecutionDate: String) => executionDate = argExecutionDate
        }
        val runTime = executionDate.split("-")
        val year = runTime(0)
        val month = runTime(1)
        val day = runTime(2)

        //create spark Session
        val spark = SparkSession
        .builder()
        .appName("Daily Gross Revenue Report")
        .config("hive.metastore.urls","thrift://localhost:9883")
        .config("hive.exec.dynamic.partition","true")
        .config("hive.exec.dynamic.partition.mode","nóntrict")
        .enableHiveSupport()
        .getOrCreate()

        //load data to spark df
        val ordersDF = spark.read.parquet("hdfs://localhost:9000/datalake/orders").drop("year", "month", "day")
        val orderDetailDF = spark.read.parquet("hdfs://localhost:9000/datalake/order_detail").drop("year", "month", "day")
        val productsDF = spark.read.parquet("hdfs://localhost:9000/datalake/products").drop("year", "month", "day")
        val inventoryDF = spark.read.parquet("hdfs://localhost:9000/datalake/inventory").drop("year", "month", "day")
        
        //join dataframe
        val preDF = ordersDF
        .filter(ordersDF("created_at")=== executionDate)
        .join(orderDetailDF,ordersDF("id")===orderDetailDF("order_id"),"inner")
        .join(productsDF,ordersDF("product_id")as "inv+quantity",col("id"),productsDF("inventory_id")=== inventoryDF("id),"inner")


        //aggregate data
        val mapDF = preDF.groupBy("Make","Model","category","product_id","inv_quantity")
        .agg(
            sum("quantity").as("Sales"),
            sum("total").as("Revenue")
        )

        //prepare result
        val resultDF = mapDF
        .withColumn("LeftOver", col("inv_quantity") - col("Sales"))
        .withColumn("year",lit(year))
        .withColumn("month",lit(month))
        .withColumn("day",lit(day))
        .select("Make","Model","Category","Sales","Revenue","LeftOver","year","month","day")


        // write to data warehouse
        resultDF.write
            .format("hive")
            .partitionBy("year","month","day")
            .mode(SaveMode.Append)
            .saveAsTable("repors.daily_gross-revenue")
    }
}