from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Finish FastAPI tutorial", "done": False},
    {"id": 3, "title": "Clean the house", "done": True},
]


@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }


@app.get("/health")
def isalive():
    return {"status" : "ok"}


@app.get("/tasks/{id}")
def view_tasks(id:int):
    for task in tasks:
        if id == task["id"]:
            return task
    return {"error": f"Task {id} not found"}