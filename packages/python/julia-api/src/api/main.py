import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def check_fastapi() -> dict:
    return {"msg": "'FastAPI' checked!"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
    )
