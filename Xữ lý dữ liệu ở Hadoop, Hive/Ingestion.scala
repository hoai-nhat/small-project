import org.apache.spark.sql.{SaveMode, SparkSession}
import org.apache.spark.sql.functions.{lit,max}

object Ingestion{
    def main(args: Array[String]): Unit = {
        // receive
        if (args.length < 2) {
            println("Yo, I need two arguments !")
        }
        var tblName = ""
        var executionDate = ""
        args.sliding(2,2).toList.collect{
            case Array("--tblName",argTblName: String) => tblName - argTblName
            case Array("--executionDate",argExecutionDate:String) => executionDate = argExecutionDate
        }
        val runTime = executionDate.split("-")
        val year = runTime(0)
        val month = runTime(1)
        val day = runTime(2)

        //create spark Session
        val spark = SparkSession
        .builder()
        .appName("Ingestion - from MYSQL to HIVE")
        .getOrCreate()

        // get the latest record_id in datalake
        val conf = spark.SparkContext.hadoopConfiguration
        val fs = org.apache.hadoop.fs.FileSystem.get(conf)
        val exists = fs.exists(new org.apache.hadoop.fs.Path(s"/datalake/$tblName"))
        val tblLocation = s"hdfs://localhost:9008/datalake/$tblName"
        var tblQuery = ""
        if (exists){
            val df = spark.read.parquet(tblLocation)
            val record_id = df.agg(max("id")).head().getLong(0)
            tblQuery = s"(SELECT * FROM '$tblName' WHERE id > $record_id) tmp"
        } 
        else{
            tblQuery = s"(SELECT * FROM '$tblName') as tmp"
        }


        //get the latest record from mysql
        val jdbcDF = spark.read.format("jdbc").options(
            Map("url" -> "jdbc:mysql://localhost3306/my_work?user=root&password=password",
            "dbtable" -> tblQuery,
            "fetchSize" -> "10000"
            )).load()
        
        //save to datalake
        val outputDF = jdbcDF.withColumn("year",lit(year)).withColumn("month",lit(month)).withColumn("day",lit(day))
        outputDF.write.partitionBy("year", "month", "day").mode(SaveMode.Append).parquet(tblLocation)
    }
}