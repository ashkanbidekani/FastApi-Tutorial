from fastapi import FastAPI
import uvicorn

# -----------------------------------------------------------------------------------------
app = FastAPI()
task = {}

# -----------------------------------------------------------------------------------------
# here we create a new task
@app.post("/add_task")
def add_task(name: str, status: str):
    task[name] = status
    return {'message': 'Success'}

# -----------------------------------------------------------------------------------------
# here we edit an existing task
@app.put("/edit_task")
def edit_task(name: str, status: str):
    if name in task:
        task[name] = status
        return {'message': f'Task "{name}" edited successfully'}
    else:
        return {'message': f'Task "{name}" does not exist'}

# -----------------------------------------------------------------------------------------
# here we delete an existing task
@app.delete("/delete_task")
def delete_task(name: str):
    if name in task:
        del task[name]
        return {'message': f'Task "{name}" deleted successfully'}
    else:
        return {'message': f'Task "{name}" does not exist'}

# -----------------------------------------------------------------------------------------
# here we get all tasks
@app.get("/tasks")
def get_all_tasks():
    return task

# -----------------------------------------------------------------------------------------
if __name__ == '__main__':
    uvicorn.run(app='todolist:app', host='127.0.0.1', port=8000, reload=True)
