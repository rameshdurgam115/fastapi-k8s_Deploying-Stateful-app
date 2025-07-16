from fastapi import FastAPI, Request
import os

app = FastAPI()
DATA_FILE = "/data/data.txt"

@app.post("/save")
async def save_data(request: Request):
    payload = await request.body()
    # The directory /data will be created by Kubernetes, but locally we must create it:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "ab") as f:
        f.write(payload + b"\n")
    return {"status": "saved"}

@app.get("/read")
def read_data():
    if not os.path.exists(DATA_FILE):
        return {"data": []}
    with open(DATA_FILE, "rb") as f:
        lines = [line.decode().strip() for line in f]
    return {"data": lines}
