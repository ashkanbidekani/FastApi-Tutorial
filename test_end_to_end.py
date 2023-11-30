import requests
import json


def test_can_get_list_of_todos():
    resp = requests.get('http://127.0.0.1:8000/tasks')
    assert resp.status_code == 200


def test_when_added_a_task_it_shown_in_list():

    requests.post('http://127.0.0.1:8000/add_task?name=task1&status=Done')

    resp = requests.get('http://127.0.0.1:8000/tasks')
    assert resp.status_code == 200
    assert json.loads(resp.content) == {"task1": "Done"}


def test_can_edit_task_to_undone():

    requests.post('http://127.0.0.1:8000/add_task?name=task1&status=Done')

    requests.put('http://127.0.0.1:8000/edit_task?name=task1&status=Undone')

    resp = requests.get('http://127.0.0.1:8000/tasks')
    assert resp.status_code == 200
    assert json.loads(resp.content) == {"task1": "Undone"}


def test_can_delete_task():

    requests.post('http://127.0.0.1:8000/add_task?name=task1&status=Done')

    requests.delete('http://127.0.0.1:8000/delete_task?name=task1')

    resp = requests.get('http://127.0.0.1:8000/tasks')
    assert resp.status_code == 200
    assert json.loads(resp.content) == {}
