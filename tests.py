import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
  new_test_task = {
    "title": "Nova tarefa teste",
    "description": "Nova descrição teste"
  }
  
  response = requests.post(f"{BASE_URL}/tasks", json=new_test_task)
  response_json = response.json()
  assert response.status_code == 200
  assert "message" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])