from lib.task_tracker import *

def test_for_empty_list():
    tasktracker = Tasktracker()
    assert tasktracker.see_tasks() == []

def test_adding_one_task():
    tasktracker = Tasktracker()
    tasktracker.add_task("Feed cat")
    assert tasktracker.see_tasks() == ["Feed cat"]


def test_adding_multiple_tasks():
    tasktracker = Tasktracker()
    tasktracker.add_task("Feed cat")
    tasktracker.add_task("Wash car")
    assert tasktracker.see_tasks() == ["Feed cat", "Wash car"]

def test_mark_a_task_complete():
    tasktracker = Tasktracker()
    tasktracker.add_task("Feed cat")
    tasktracker.add_task("Wash car")
    tasktracker.mark_complete("Feed cat")
    assert tasktracker.see_tasks() == ["Wash car"]