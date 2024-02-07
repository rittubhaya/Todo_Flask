import os
from werkzeug.utils import secure_filename

class FileUploads:
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    def __init__(self):
        self.base_path = os.path.abspath(os.path.dirname(__file__))  # Get the absolute path of the current directory
        self.upload_path = os.path.join(self.base_path, self.UPLOAD_FOLDER)
        os.makedirs(self.upload_path, exist_ok=True)

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def upload_file(self, file):
        try:
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(self.upload_path, filename)
                file.save(file_path)
                return f"File uploaded successfully! Path: {file_path}"
            else:
                return "Invalid file format"
        except Exception as e:
            return f"File upload failed. Error: {str(e)}"
