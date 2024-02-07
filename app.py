from flask import Flask, render_template, request, send_from_directory, jsonify
from computations import Computations
from file_uploads import FileUploads

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize classes
computations = Computations()
file_uploads = FileUploads()

# Route for computations
@app.route('/computations', methods=['POST'])
def computations_route():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)

    operation = data.get('operation', 'sum')

    if operation == 'sum':
        result = computations.calculate_sum(a, b)
    elif operation == 'difference':
        result = computations.calculate_difference(a, b)
    elif operation == 'product':
        result = computations.calculate_product(a, b)
    elif operation == 'quotient':
        result = computations.calculate_quotient(a, b)
    else:
        result = "Invalid operation"

    return jsonify({"result": result})

# Route for file uploads
@app.route('/file_uploads', methods=['POST'])
def file_uploads_route():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    file_path = file_uploads.upload_file(file)
    return f"File uploaded successfully! Path: {file_path}"

# Route to serve uploaded files
@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route for rendering templates
@app.route('/render_template', methods=['GET'])
def render_template_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
