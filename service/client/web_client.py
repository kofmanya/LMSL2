from flask import Flask, request, render_template, jsonify, url_for
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"  # Folder to store uploaded images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_URL = "http://api:8000/predict"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    image_url = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            try:
                # Save the uploaded file locally
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                image_url = url_for("static", filename=f"uploads/{file.filename}")

                # Send the file to the API for prediction
                with open(file_path, "rb") as f:
                    response = requests.post(API_URL, files={"file": f})
                    data = response.json()
                    result = data.get("predicted_category")
            except Exception as e:
                error = f"Error: {str(e)}"

    return render_template("index.html", result=result, error=error, image_url=image_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

