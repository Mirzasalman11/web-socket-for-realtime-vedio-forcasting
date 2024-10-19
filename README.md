# WebSocket for Real-time Video Processing

This project is a FastAPI-based application that processes real-time video streams for tasks such as lane detection and traffic sign detection using WebSocket connections. The application allows clients to send video frames and receive processed frames with detected lanes and traffic signs.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [WebSocket Endpoints](#websocket-endpoints)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contact](#contact)

## Introduction

This project provides a real-time video processing solution for detecting road lanes and traffic signs. It utilizes WebSocket connections for streaming video frames from clients, processes these frames using OpenCV, and sends the processed frames back to the clients.

The application supports multiple WebSocket clients and provides three endpoints:
- `/both`: Detects both lanes and traffic signs.
- `/line_detect`: Detects road lanes.
- `/sign_detect`: Detects traffic signs.

## Features

- Real-time lane detection and traffic sign recognition.
- Supports multiple WebSocket clients simultaneously.
- FastAPI backend with WebSocket communication.
- Uses OpenCV for video processing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mirzasalman11/web-socket-for-realtime-vedio-forcasting.git
    cd web-socket-for-realtime-vedio-forcasting
    ```

2. Ensure you have OpenCV installed:
    ```bash
    pip install opencv-python
    ```

3. Install FastAPI and Uvicorn:
    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1. Start the FastAPI WebSocket server:
    ```bash
    uvicorn websocket_server:app --host 0.0.0.0 --port 5000
    ```

2. Use a WebSocket client to connect to one of the endpoints (`/both`, `/line_detect`, `/sign_detect`) and start sending video frames in byte format.

3. The server will process the frames and send back the processed video frames in JPEG format.

## WebSocket Endpoints

1. **`/both`**:  
    Detects both road lanes and traffic signs from the video stream.

2. **`/line_detect`**:  
    Detects only the road lanes from the video stream.

3. **`/sign_detect`**:  
    Detects only traffic signs from the video stream.

## Testing

### WebSocket Server Testing

The project includes a `websocket_test.py` file that allows you to test the WebSocket server functionality. Here's how the testing process works:

1. **Purpose of Testing**:  
    The `websocket_test.py` script is used to simulate the behavior of a WebSocket client. It sends video frames (in byte format) to the WebSocket server, which processes them and returns the results (processed frames). This testing script ensures that the WebSocket communication and the video processing pipeline are working correctly.

2. **Steps in the Test**:  
    - The test script first connects to the WebSocket server on the specified endpoint (e.g., `/both`, `/line_detect`, or `/sign_detect`).
    - It captures video frames from a local source (such as a webcam or video file) and sends them to the WebSocket server.
    - The server receives and processes the frames by detecting road lanes or traffic signs.
    - Once the server processes the frames, it sends the results back to the test client.
    - The test script then displays the processed frames, allowing the user to visually verify that the server is functioning correctly.

3. **Expected Outcome**:  
    During testing, you should expect the following:
    - The client connects successfully to the server.
    - Video frames are sent to the server and processed (you can observe the detection of lanes and/or signs in the returned video).
    - The test client receives and displays the processed video frames.
    - If an error occurs (e.g., connection loss or improper frame format), the script should handle it and print an appropriate message.

4. **How to Run the Test**:  
    To run the test, simply execute the `websocket_test.py` file:
    ```bash
    python websocket_test.py
    ```
    Ensure that the WebSocket server is already running. The test script will attempt to connect and process frames.

5. **Verification**:  
    The visual output displayed by the test client will show if lane detection or traffic sign detection is working. The returned frames should have visible lanes or signs outlined/detected by the model.

### Importance of Testing

Testing is crucial to ensure that:
- The WebSocket communication between the client and server is functional.
- Video frames are being processed correctly by the server.
- Any issues related to video encoding, decoding, and real-time streaming are identified and fixed.

By using the provided test script (`websocket_test.py`), you can simulate various scenarios and validate that the application performs as expected under different conditions (e.g., slow networks, high frame rates, etc.).

## Future Improvements

- Add support for additional video processing tasks, such as object tracking or vehicle detection.
- Improve model accuracy by training on larger datasets.
- Implement error handling for more robust WebSocket communication.
- Add support for different video codecs and input formats.
- Optimize performance for mobile applications.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Author: Mirza Salman  
Email: [salmansaluu661@gmail.com](mailto:salmansaluu661@gmail.com)

For more information, visit the repository at [web-socket-for-realtime-vedio-forcasting](https://github.com/Mirzasalman11/web-socket-for-realtime-vedio-forcasting).
