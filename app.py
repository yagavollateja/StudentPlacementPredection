from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)

# Load model safely
model = pickle.load(open("model.pkl", "rb"))

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        cgpa = float(data.get("cgpa"))
        skills = float(data.get("skills"))

        prediction = model.predict([[cgpa, skills]])

        return jsonify({
            "prediction": int(prediction[0]),
            "message": "Placed" if prediction[0] == 1 else "Not Placed"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)