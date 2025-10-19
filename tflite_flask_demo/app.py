from flask import Flask, jsonify, render_template
import tensorflow as tf
import numpy as np
import time

app = Flask(__name__)

# TFLite modelini yükle
interpreter = tf.lite.Interpreter(model_path="resnet18.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test_performance():
    dummy_input = np.random.random_sample(input_details[0]['shape']).astype(np.float32)
    start = time.time()
    interpreter.set_tensor(input_details[0]['index'], dummy_input)
    interpreter.invoke()
    _ = interpreter.get_tensor(output_details[0]['index'])
    end = time.time()
    return jsonify({"time_ms": round((end-start)*1000, 2)})

if __name__ == "__main__":
    app.run(debug=True)
