from fastapi import FastAPI


app = FastAPI()


@app.get('/')  # メソッドとエンドポイントの指定
async def hello():
    return {"text": "hello world"}
