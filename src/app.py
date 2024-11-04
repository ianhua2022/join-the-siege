from flask import Flask, request, jsonify, render_template
import os
from src.validator import is_allowed_file
from src.classifiers.classifier import classify_file

# Get the absolute path to the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, 
              template_folder=os.path.join(project_root, 'templates'),
              static_folder=os.path.join(project_root, 'static'))

@app.route('/classify_file', methods=['POST'])
def classify_file_route():
    try:
        # Validate file exists in request
        if 'file' not in request.files:
            return jsonify({
                "status": "error",
                "message": "No file uploaded"
            }), 400

        file = request.files['file']

        # Validate file was selected
        if file.filename == '':
            return jsonify({
                "status": "error",
                "message": "No file selected"
            }), 400

        # Validate file
        if not is_allowed_file(file):
            return jsonify({
                "status": "error",
                "message": "File type not allowed."
            }), 400

        # Perform classification
        try:
            file_class = classify_file(file)
            return jsonify({
                "status": "success",
                "file_class": file_class
            }), 200
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Classification error: {str(e)}"
            }), 500

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
