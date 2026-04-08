from flask import Flask, request, jsonify, render_template
import pickle
import os


app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

# Render HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    cgpa = float(data["cgpa"])
    skills = float(data["skills"])

    prediction = model.predict([[cgpa, skills]])

    return jsonify({
        "prediction": int(prediction[0]),
        "message": "Placed" if prediction[0] == 1 else "Not Placed"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)