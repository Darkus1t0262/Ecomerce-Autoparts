from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database for orders
orders = {}

class Order(BaseModel):
    id: int
    user_id: int
    product_ids: List[int]

@app.websocket("/orders/ws")
async def order_updates(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            order = Order(**data)
            if order.id in orders:
                await websocket.send_json({"error": "Order ID already exists"})
                continue
            orders[order.id] = order.dict()
            await websocket.send_json({"message": "Order received successfully", "order": order.dict()})
        except Exception as e:
            await websocket.send_json({"error": str(e)})
