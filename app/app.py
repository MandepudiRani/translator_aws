#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
import boto3
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

s3 = boto3.client('s3',
                    aws_access_key_id='AKIAQTEULHALY2J4O7P2',
                    aws_secret_access_key= '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',
                   
                     )
BUCKET_NAME='projecttranslator'
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)
        s3.upload_file(
					 Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
					)
              
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        print(os.system("python script.py > new.txt"))
        k=open("new.txt", "r").read() 
        print(k) 
        return render_template('index.html', filename=filename, val=k)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run()