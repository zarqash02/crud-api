from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


next_id = 4

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Finish FastAPI tutorial", "done": False},
    {"id": 3, "title": "Clean the house", "done": True},
]


class TaskRequest(BaseModel):
    title: str




@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

# Stage 1 — Your first real endpoint
@app.get("/health")
def isalive():
    return {"status" : "ok"}


# Stage 2 — Read: list and single task
@app.get("/tasks/{id}")
def view_tasks(id:int):
    for task in tasks:
        if id == task["id"]:
            return task
    return {"error": f"Task {id} not found"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskRequest):
    global next_id

    new_task = {
    "id": next_id,
    "title": task.title,
    "done": False
    }
    
    # Validate the input: if 'title' is missing or empty, return 400 Bad Request with a JSON error
    if task.title == "":
        raise HTTPException(status_code=400, detail="Please enter the title of task")
    
    # Give the task the next free id
    else:
        next_id += 1

    # Set 'done' status to false
        new_task["done"] = False

    # Add the task to the internal list
        tasks.append(new_task)
    # Return the newly created task object
        return new_task
    pass