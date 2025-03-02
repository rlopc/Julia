import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def check_fastapi() -> dict:
    return {"msg": "'FastAPI' checked!"}


def start_local_server() -> None:
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
    )


if __name__ == "__main__":
    start_local_server()
