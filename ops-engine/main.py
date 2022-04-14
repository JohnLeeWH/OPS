from lib2to3.pgen2.token import OP
from typing import Optional

from fastapi import FastAPI, Form
from pydantic import BaseModel

from wrk import run_wrk_process

app = FastAPI()


class WrkArgs(BaseModel):
    # wrk 请求内容

    connections: Optional[int] = None
    duration: Optional[int] = None
    thread: Optional[int] = None
    script: Optional[str] = None
    header: Optional[str] = None
    latency: Optional[str] = None
    timeout: Optional[str] = None
    website: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/wrk")
async def post_wrk(post_args: WrkArgs):
    #
    print(post_args)
    wrkArgs = {}
    website = post_args.website
    result = run_wrk_process(wrkArgs, website)
    return {"result": result}


"""
wrkArgs = {"thread": "2", "connections": "2"}
website = "https://www.baidu.com"
run_wrk_process(wrkArgs, website)
"""
