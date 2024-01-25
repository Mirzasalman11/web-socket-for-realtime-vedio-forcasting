import cv2
import numpy as np
import asyncio
import websockets
from websockets.exceptions import ConnectionClosedError

async def send_video_frames(uri, video_path):
    cap = cv2.VideoCapture(video_path)

    async with websockets.connect(uri) as websocket:
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Convert the frame to bytes
                _, buffer = cv2.imencode('.jpg', frame)
                frame_data = buffer.tobytes()

                # Send the frame to the WebSocket server
                await websocket.send(frame_data)

                # Wait for a short time (you can adjust this based on your needs)
                await asyncio.sleep(0.1)


                # Receive the frame from the WebSocket server
                frame_data = await websocket.recv()

                # Convert the frame data to a NumPy array
                frame = np.frombuffer(frame_data, dtype=np.uint8)

                # Decode the frame using OpenCV
                img = cv2.imdecode(frame, cv2.IMREAD_COLOR)

                # Display the frame
                cv2.imshow('Received Frame', img)
                cv2.waitKey(1) 


        except ConnectionClosedError:
            print("Connection closed by the server.")
        finally:
            cap.release()

async def main():
    # Specify the WebSocket URI for the desired endpoint
    uri = "ws://localhost:5000/sign_detect"  # Change the endpoint as needed

    # Specify the path to the sample video file
    video_path = "C:/salman/sir_pro/ved.mp4"

    await send_video_frames(uri, video_path)

if __name__ == "__main__":
    asyncio.run(main())


