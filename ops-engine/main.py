import sys

from typing import Optional
from unittest import result
from click import password_option

from fastapi import FastAPI, Form, WebSocket, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, HttpUrl

from cmd import run_wrk_process, run_ping_process, run_iperf_process, run_nmap_process

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>wrk性能测试</title>
    </head>
    <body>
        <h1>wrk性能测试</h1>
        <label>website: <input type="text" id="website" autocomplete="off" value="http://127.0.0.1"/></label>
        <button onclick="sendMessage(event)">send</button>
        
        <ul id='messages'>
        </ul>
        <script>
            var ws = null;
            function sendMessage(event) {
                ws=new WebSocket("ws://localhost:8000/wrkws");
                ws.onopen=function(event) {
                    var website=document.getElementById("website");
                    alert(website.value);
                    ws.send(website.value);
                }
                
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                    event.preventDefault()
                };
            }
        </script>
    </body>
</html>
"""


class WrkArgs(BaseModel):
    # wrk 请求内容

    connections: Optional[int] = None
    duration: Optional[int] = None
    thread: Optional[int] = None
    script: Optional[str] = None
    header: Optional[str] = None
    latency: Optional[str] = None
    timeout: Optional[str] = None
    website: HttpUrl


class PingArgs(BaseModel):
    # ping请求内容
    ip: str = Field(
        regex=
        "^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$"
    )


class IperfArgs(BaseModel):
    # iperf3请求内容
    ip: str = Field(
        regex=
        "^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$"
    )


class NmapArgs(BaseModel):
    # nmap请求内容
    ip: str = Field(
        regex=
        "^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$"
    )


class SSHTarget(BaseModel):
    # ssh目标请求内容
    host: str = Field(
        regex=
        "^((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))$"
    )
    post: int
    user: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/wrk")
async def get():
    return HTMLResponse(html)


@app.post("/wrk")
async def post_wrk(post_args: WrkArgs):
    #
    #print(post_args)
    wrk_args = {}
    if post_args.connections is not None:
        wrk_args["connections"] = post_args.connections
    if post_args.duration is not None:
        wrk_args["duration"] = post_args.duration
    if post_args.thread is not None:
        wrk_args["thread"] = post_args.thread
    if post_args.script is not None:
        wrk_args["script"] = post_args.script
    if post_args.header is not None:
        wrk_args["header"] = post_args.header
    if post_args.latency is not None:
        wrk_args["latency"] = post_args.latency
    if post_args.timeout is not None:
        wrk_args["timeout"] = post_args.timeout

    website = post_args.website
    result = run_wrk_process(wrk_args, website)
    return {"result": result}


@app.post("/ping")
async def post_ping(post_args: PingArgs):
    #
    #print(post_args.ip)
    result = run_ping_process(post_args.ip)
    return {"result": result}


@app.post("/iperf")
async def post_iperf(post_args: IperfArgs):
    #
    iperf_args = {}

    ip = post_args.ip
    result = run_iperf_process(iperf_args, ip)
    return {"result": result}


@app.post("/nmap")
async def post_nmap(post_args: NmapArgs):
    #
    nmap_args = {}

    ip = post_args.ip
    result = run_nmap_process(nmap_args, ip)
    return {"result": result}


@app.post("/wrk/targetdeploy")
async def post_wrk_targetdeploy(post_args: SSHTarget):
    pass


@app.websocket('/wrkws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        #await websocket.send_text(f"Message text was: {data}")
        wrkArgs = {"-d 2s"}
        #proc = run_wrk_process(wrkArgs, data)
        proc = run_ping_process(data)
        while proc.poll() is None:
            #lines = str(proc.stdout).split('\n')
            #for line in lines:
            '''
            with open('nohup.out') as tf:
                tf.seek(0, 2)
                while True:
                    message = tf.readline().strip()
                    if message:
                        print(message)
                        await websocket.send_text(message)
            '''
            websocket.send(sys.stdout)
            '''
            for line in proc.stdout.readlines():
                print(str(line))

                await websocket.send_text(str(line))
            '''
            '''
            try:
                outs, errs = proc.communicate(timeout=15)
            except TimeoutError:
                proc.kill()
                outs, errs = proc.communicate()
            await websocket.send_text(str(outs).split('\n'))
            '''
            #line = proc.stdout.readline()
            #lines=proc.stdout.read()
            #await websocket.send_text(str(lines))
            ''' 
            while line:
            yield line
            line = proc.stdout.readline()
            #for line in proc.stdout():
            #line = proc.stdout.readline()
            #print(str(line))
            await websocket.send_text(str(line))
            '''


"""
wrkArgs = {"thread": "2", "connections": "2"}
website = "https://www.baidu.com"
run_wrk_process(wrkArgs, website)
"""
