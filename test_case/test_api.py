import uuid
import pytest
import requests


@pytest.fixture
def global_variable():
    endpoint = "https://todo.pixegami.io/"
    user_id = f"oadeyo_{uuid.uuid4().hex}"
    print(f"Creating task for user {user_id}")
    payload = {
                "content": "Oluwaseun Adeyo",
                "user_id": user_id,
                "is_done": False
            }
    
    lst = [endpoint,payload]
    return lst

def create_task(payload, endpoint, timeout = 20):
    return requests.put(endpoint + "create-task", json=payload, timeout=timeout)

def update_task(payload, endpoint, timeout = 20):
    return requests.put(endpoint + "update-task", json=payload, timeout=timeout)

def get_task(task_id, endpoint, timeout = 20):
    return requests.get(endpoint + f"get-task/{task_id}", timeout=timeout)

def list_task(user_id, endpoint, timeout = 20):
    return requests.get(endpoint + f"list-tasks/{user_id}", timeout=timeout)

def delete_task(task_id, endpoint, timeout = 20):
    return requests.delete(endpoint + f"delete-task/{task_id}", timeout=timeout)


def test_can_call_endpoint(global_variable, timeout = 20):
    response = requests.get(global_variable[0], timeout=timeout)
    # data = response.json()
    assert response.status_code == 200

def test_can_create_task(global_variable):
    # create a task
    # get and validate the task

    # create a task
    endpoint = global_variable[0]
    payload = global_variable[1]
    
    create_task_response = create_task(payload, endpoint)
    assert create_task_response.status_code == 200
    # print(create_task_response.json())
    

    # get and validate the task
    task_id = create_task_response.json()["task"]["task_id"]
    get_task_response = get_task(task_id, endpoint)
    get_task_data = get_task_response.json()

    assert get_task_response.status_code == 200
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]
    print(get_task_data)

def test_can_update_task(global_variable):
    # create a task
    # update a task
    # get and validate the task

    # create a task
    endpoint = global_variable[0]
    payload = global_variable[1]
    
    create_task_response = create_task(payload, endpoint)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    # print(create_task_response.json())

    # update a task
    new_payload = {
                "content": "Oluwaseun John Adeyo",
                "user_id": payload["user_id"],
                "task_id": task_id,
                "is_done": True
            }
    update_task_response = update_task(new_payload, endpoint)
    assert update_task_response.status_code == 200

    # get and validate the task
    get_task_response = get_task(task_id, endpoint)
    get_task_data = get_task_response.json()

    assert get_task_response.status_code == 200
    assert get_task_data["content"] != payload["content"]
    assert get_task_data["user_id"] == new_payload["user_id"]


def test_can_list_tasks(global_variable):
    # create a task
    # list tasks

    # create a task
    endpoint = global_variable[0]
    payload = global_variable[1]
    user_id = f"oadeyo_{uuid.uuid4().hex}"
    payload["user_id"] = user_id
    for _ in range(3):
        create_task_response = create_task(payload, endpoint)
        assert create_task_response.status_code == 200

    # list tasks and check that theere are N items
    list_task_response = list_task(user_id, endpoint)
    list_task_data = list_task_response.json()["tasks"]
    assert list_task_response.status_code == 200
    assert len(list_task_data) ==  3



def test_can_delete_tasks(global_variable):
    # create a task
    # delete tasks
    # get task and check that its not found 

    # create a task
    endpoint = global_variable[0]
    payload = global_variable[1]

    create_task_response = create_task(payload, endpoint)
    assert create_task_response.status_code == 200

    # delete tasks
    task_id = create_task_response.json()["task"]["task_id"]
    delete_task_response = delete_task(task_id, endpoint)
    assert delete_task_response.status_code == 200
    

    # get task and check that its not found 
    get_task_response = get_task(task_id, endpoint)
    assert get_task_response.status_code == 404



