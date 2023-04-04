import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< Mensagem recebida main.py: {name}")

    greeting = f"| main.py {name} |"

    await websocket.send(greeting)
    print(f">>> Mensagem enviada main.py: {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())