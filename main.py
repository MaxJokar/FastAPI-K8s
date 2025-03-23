from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World 17.03.2025  1"}

#  dev1 added
