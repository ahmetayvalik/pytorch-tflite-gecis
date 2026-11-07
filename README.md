# TensorFlow Lite Inference Demo

A compact Flask application that loads a TensorFlow Lite model and exposes a browser interface and a simple inference-timing endpoint.

## Repository structure

```text
tflite_flask_demo/
  app.py
  resnet18.tflite
  requirements.txt
  templates/
  static/
  vercel.json
```

## How it works

The Flask application initializes a TensorFlow Lite interpreter from `resnet18.tflite` and allocates its tensors. Its `/test` route generates random input matching the model input shape, runs one inference, and returns the measured elapsed time in milliseconds.

**Important:** The timing endpoint uses random synthetic input and is not an accuracy evaluation, a validated benchmark, or evidence of conversion fidelity.

## Run locally

From `tflite_flask_demo/`, create a Python environment and install Flask, NumPy, and a compatible TensorFlow build. Check compatibility with your Python version and platform.

```bash
python app.py
```

Then open the local Flask URL shown in your terminal. The demo uses `debug=True` and is intended for local development, not production hosting.

## Next improvements

- Pin compatible dependencies in `requirements.txt`
- Add reproducible performance tests with warm-up runs and repeated timing samples
- Document source model, conversion steps, preprocessing, and output interpretation
- Compare outputs against the original model on real test samples

## Author

Ahmet Ayvalık
