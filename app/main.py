from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}
#lozano

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
