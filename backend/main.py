from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "HU HU"

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
