import os

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret"
#app.config['UPLOAD_FOLDER'] = "/home/e3s/Documents/scripts/mypackages/facto/custom_imports/templates/UPLOAD_FOLDER"
app.config['UPLOAD_FOLDER'] = "/home/e3s/Documents/facto/facto/custom_imports/UPLOAD_FOLDER"
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def index():
	return render_template('index.html')
                                                                                                                                                               
         

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File(s) successfully uploaded')
			return redirect('/')
			print("benaan")

#86.88.42.33

def main():
	if __name__ == "__main__":
		app.run()