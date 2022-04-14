from typing import Optional

from fastapi import FastAPI, Form, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from wrk import run_wrk_process

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>wrk性能测试</title>
    </head>
    <body>
        <h1>wrk性能测试</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <label>website: <input type="text" id="website" autocomplete="off" value="http://127.0.0.1"/></label>
            <button onclick="connect(event)">Connect</button>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
            function connect(event) {
                ws = new WebSocket("ws://localhost:8000/wrk");
                var website=document.getElementById("website")
                ws.send(website)
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
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
    website: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/wrk")
async def get():
    return HTMLResponse(html)


@app.post("/wrk")
async def post_wrk(post_args: WrkArgs):
    #
    print(post_args)
    wrkArgs = {}
    website = post_args.website
    result = run_wrk_process(wrkArgs, website)
    return result


@app.websocket('/wrk')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


"""
wrkArgs = {"thread": "2", "connections": "2"}
website = "https://www.baidu.com"
run_wrk_process(wrkArgs, website)
"""
