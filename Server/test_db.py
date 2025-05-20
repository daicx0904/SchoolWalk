import django

django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        row = cursor.fetchone()
        print("PostgreSQL version:", row[0])

        # 测试PostGIS功能
        cursor.execute("SELECT PostGIS_version();")
        row = cursor.fetchone()
        print("PostGIS version:", row[0])
except Exception as e:
    print("Database connection failed:", e)