import asyncio
import websockets
import json


async def test_websocket():
    uri = "ws://localhost:8000/ws/query"

    async with websockets.connect(uri) as websocket:
        message = "Hello from Python client"
        print(f"Sending: {message}")
        await websocket.send("show all users")

        # await websocket.send(message)

        while True:
            try:
                response = await websocket.recv()
                print("Received:", response)
            except websockets.exceptions.ConnectionClosed:
                print("Connection closed")
                break


asyncio.run(test_websocket())
