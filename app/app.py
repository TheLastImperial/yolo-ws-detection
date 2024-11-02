from flask import Flask, request, jsonify
from PIL import Image
from ultralytics import YOLO, settings

model = YOLO( "weights/yolo11n.pt" )
app = Flask(__name__)

@app.route("/detection", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    results = model(img)
    predictions = []
    for result in results:
        for box in result.boxes.numpy():
            predictions.append({
                'label': result.names[box.cls[0]],
                'xyxy': [
                    int(xyxy) for xyxy in list(box.xyxy[0])
                ],
                'xyxyn': [
                    float(xyxyn) for xyxyn in list(box.xyxyn[0])
                ],
                'score': float(box.conf[0])
            })

    return jsonify({
        'predictions': predictions
    })

if __name__ == "__main__":
    app.run(debug=True)
