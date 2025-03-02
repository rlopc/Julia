from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def check_fastapi() -> dict:
    return {"msg": "'FastAPI' checked!"}
