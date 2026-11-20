import os
import sys
from pyspark.sql import SparkSession


def get_spark(app_name: str = "HM_RFM_Segmentation", driver_memory: str = "4g", shuffle_partitions: int = 16) -> SparkSession:
    """
    Khởi tạo và trả về SparkSession dùng chung cho toàn bộ dự án.
    Đảm bảo đồng bộ cấu hình giữa các thành viên trong nhóm.
    """
    # Đảm bảo PySpark dùng đúng trình thông dịch Python của môi trường ảo (.venv)
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName(app_name)
        .config("spark.driver.memory", driver_memory)
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions))
        # Tối ưu đọc/ghi Parquet và xử lý định dạng thời gian
        .config("spark.sql.parquet.int96RebaseModeInRead", "CORRECTED")
        .config("spark.sql.parquet.datetimeRebaseModeInRead", "CORRECTED")
        .config("spark.sql.session.timeZone", "UTC")
        # Tắt bớt log cảnh báo thừa trong notebook
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")
    return spark