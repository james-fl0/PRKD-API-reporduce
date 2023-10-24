from flask import Flask, jsonify, request, Response
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Logging message to the console.")
    current_time = time.strftime("%H:%M:%S")
    print(f"[{current_time}] This message will be logged every 1 second.")
    return jsonify({"message": "Hello, World!"}), 200

if __name__ == '__main__':
    app.run()