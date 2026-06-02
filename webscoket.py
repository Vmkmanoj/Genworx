from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        question = await websocket.receive_text()

        # RAG logic here
        answer = f"You asked: {question}"

        await websocket.send_text(answer)