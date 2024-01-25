from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import cv2
from main import LaneDetectionAPI
import numpy as np

app = FastAPI()

class VideoWebSocketManager:
    def __init__(self):
        self.active_websockets = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_websockets.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_websockets.remove(websocket)

    async def send_frame(self, frame):
        for websocket in self.active_websockets:
            try:
                await websocket.send_bytes(frame)
            except WebSocketDisconnect:
                self.disconnect(websocket)

video_manager = VideoWebSocketManager()

@app.websocket("/both")
async def both(websocket: WebSocket):
    await video_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_bytes()
            nparr = np.frombuffer(data, np.uint8)
            source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Process the received video stream
            api = LaneDetectionAPI(video_path=source)
            both = api.process_video()

            # Encode it back into JPEG for simplicity
            ret, buffer = cv2.imencode('.jpg', both)
            processed_data = buffer.tobytes()

            # Send the processed video data to the connected WebSocket clients
            await video_manager.send_frame(processed_data)
    except WebSocketDisconnect:
        video_manager.disconnect(websocket)

@app.websocket("/line_detect")
async def line(websocket: WebSocket):
    await video_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_bytes()
            nparr = np.frombuffer(data, np.uint8)
            source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Process the received video stream
            api = LaneDetectionAPI(video_path=source)
            line = api.line()

            # Encode it back into JPEG for simplicity
            ret, buffer = cv2.imencode('.jpg', line)
            processed_data = buffer.tobytes()

            # Send the processed video data to the connected WebSocket clients
            await video_manager.send_frame(processed_data)
    except WebSocketDisconnect:
        video_manager.disconnect(websocket)

@app.websocket("/sign_detect")
async def sign_detect(websocket: WebSocket):
    await video_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_bytes()
            nparr = np.frombuffer(data, np.uint8)
            source = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            # Process the received video stream
            api = LaneDetectionAPI(video_path=source)
            sign = api.sign_detect()

            # Encode it back into JPEG for simplicity
            ret, buffer = cv2.imencode('.jpg', sign)
            processed_data = buffer.tobytes()

            # Send the processed video data to the connected WebSocket clients
            await video_manager.send_frame(processed_data)
    except WebSocketDisconnect:
        video_manager.disconnect(websocket)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
