from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(**name**)

# Load model once when server starts

model = tf.keras.models.load_model("mobilenet_plant_model.h5")

classes = [
"Healthy","Apple___Apple_scab","Apple___Black_rot","Apple___Cedar_apple_rust","Apple___healthy",
"Blueberry___healthy","Cherry___Powdery_mildew","Cherry___healthy",
"Corn___Cercospora_leaf_spot Gray_leaf_spot","Corn___Common_rust","Corn___Northern_Leaf_Blight","Corn___healthy",
"Grape___Black_rot","Grape___Esca_(Black_Measles)","Grape___Leaf_blight","Grape___healthy",
"Orange___Haunglongbing","Peach___Bacterial_spot","Peach___healthy",
"Pepper_bell___Bacterial_spot","Pepper_bell___healthy",
"Potato___Early_blight","Potato___Late_blight","Potato___healthy",
"Raspberry___healthy","Soybean___healthy",
"Squash___Powdery_mildew",
"Strawberry___Leaf_scorch","Strawberry___healthy",
"Tomato___Bacterial_spot","Tomato___Early_blight","Tomato___Late_blight","Tomato___Leaf_Mold",
"Tomato___Septoria_leaf_spot","Tomato___Spider_mites","Tomato___Target_Spot",
"Tomato___Yellow_Leaf_Curl_Virus","Tomato___Mosaic_virus","Tomato___healthy"
]

def preprocess(img):
img = img.convert("RGB")
img = img.resize((224, 224))
img = np.array(img) / 255.0
img = np.expand_dims(img, axis=0)
return img

@app.route("/")
def home():
return "Plant Disease API Running"

@app.route("/predict", methods=["POST"])
def predict():
if "file" not in request.files:
return jsonify({"error": "No file uploaded"}), 400

```
file = request.files["file"]
img = Image.open(file)
img = preprocess(img)

pred = model.predict(img)
result = classes[np.argmax(pred)]

return jsonify({"prediction": result})
```

if **name** == "**main**":
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
