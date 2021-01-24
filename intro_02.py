from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get('/get/{path}')
async def path_and_query_params(
        path: str,
        query: int,
        default_none: Optional[str] = None):
    return {"text": f"hello, {path}, {query} and {default_none}"}
