from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = Flask(__name__)
CORS(app)

model = YOLO("yolov8n.pt")

def read_image_from_file(file):
    npimg = np.frombuffer(file.read(), np.uint8)
    return cv2.imdecode(npimg, cv2.IMREAD_COLOR)

def predict_objects(image):
    results = model.predict(source=image)
    output = []
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            output.append({
                "name": model.names[cls_id],
                "confidence": round(conf, 3)
            })
    return output

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = read_image_from_file(request.files["image"])
    detections = predict_objects(image)
    return jsonify(detections)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
