
import requests

BASE_URL = "http://localhost:8000/api/"

def get_students():
    try:
        response = requests.get(f"{BASE_URL}students/")
        return response.json() if response.status_code == 200 else []
    except:
        return []

def create_student(data):
    try:
        response = requests.post(f"{BASE_URL}students/", json=data)
        return response.status_code == 201
    except:
        return False

# 类似的实现其他API调用...
