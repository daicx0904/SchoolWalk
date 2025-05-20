# 临时测试脚本 test_db.py
import psycopg2
from django.contrib.gis.gdal import HAS_GDAL

print("GDAL可用:", HAS_GDAL)  # 应输出True

try:
    conn = psycopg2.connect(
        dbname="student_mgmt",
        user="mgmt_user",
        password="User123!",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT PostGIS_Version()")
    print("PostGIS版本:", cursor.fetchone()[0])
except Exception as e:
    print("连接失败:", e)