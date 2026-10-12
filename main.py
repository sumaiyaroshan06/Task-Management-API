
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task Management API")


class Task(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


tasks = {}
next_id = 1


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_id

    task_id = next_id
    tasks[task_id] = task
    next_id += 1

    return {"id": task_id, **task.model_dump()}


@app.get("/tasks")
def get_tasks():
    return [
        {"id": task_id, **task.model_dump()}
        for task_id, task in tasks.items()
    ]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"id": task_id, **tasks[task_id].model_dump()}
