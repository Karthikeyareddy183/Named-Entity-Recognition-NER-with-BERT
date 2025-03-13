from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)

# Initialize Basic Authentication
auth = HTTPBasicAuth()

# User credentials (username and password)
users = {
    "admin": generate_password_hash("password")  # Replace with your desired username and password
}

# Verify user credentials
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# Load the fine-tuned NER model
def load_model():
    model_path = "./ner-bert-model"  # Path to your fine-tuned model
    ner_pipeline = pipeline("ner", model=model_path, tokenizer=model_path, aggregation_strategy="simple")
    return ner_pipeline

# Load the model
ner_pipeline = load_model()

# Home route (renders home.html)
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Predict route (renders predict.html and handles POST requests)
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Get input text from the form
        text = request.form.get("text")

        if not text:
            return jsonify({"error": "Missing 'text' field in form data"}), 400

        # Run the NER pipeline
        results = ner_pipeline(text)

        # Format the results for display
        entities = [{"word": entity["word"], "entity": entity["entity_group"]} for entity in results]

        return render_template("predict.html", text=text, entities=entities)

    # Render the initial form for GET requests
    return render_template("predict.html", text="", entities=[])

# Predict API endpoint (accepts JSON input via Postman)
@app.route("/api/predict", methods=["POST"])
@auth.login_required
def predict_api():
    # Get input text from JSON
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON input"}), 400

    text = data["text"]

    # Run the NER pipeline
    results = ner_pipeline(text)

    # Format the results
    entities = [{"word": entity["word"], "entity": entity["entity_group"]} for entity in results]

    return jsonify({"text": text, "entities": entities})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)