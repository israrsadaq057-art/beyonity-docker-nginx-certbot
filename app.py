from flask import Flask, render_template, request, redirect, url_for, send_file, session
import boto3
import io
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'beyonity-secret-key-2026'

S3_BUCKET = 'beyonity-3d-assets-prod-945504685795'
s3_client = boto3.client('s3')

ARTISTS = ['anna', 'ben', 'carla', 'david', 'elena', 'felix', 'grace', 'henry', 'irena', 'jonas', 'karla', 'lukas', 'mona', 'niklas', 'olivia', 'paul']

def format_size(bytes):
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024 * 1024:
        return f"{bytes / 1024:.1f} KB"
    elif bytes < 1024 * 1024 * 1024:
        return f"{bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{bytes / (1024 * 1024 * 1024):.2f} GB"

@app.route('/')
def index():
    if 'artist' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html', artists=ARTISTS)

@app.route('/login', methods=['POST'])
def login():
    artist = request.form.get('artist')
    if artist in ARTISTS:
        session['artist'] = artist
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('artist', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'artist' not in session:
        return redirect(url_for('index'))
    artist = session['artist']
    prefix = f'artists/{artist}/'
    
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
        files = []
        total_size = 0
        
        if 'Contents' in response:
            for obj in response['Contents']:
                if obj['Key'] != prefix:
                    files.append({
                        'name': obj['Key'].replace(prefix, ''),
                        'size': obj['Size'],
                        'size_str': format_size(obj['Size']),
                        'last_modified': obj['LastModified'].strftime('%Y-%m-%d %H:%M'),
                    })
                    total_size += obj['Size']
        
        files.sort(key=lambda x: x['last_modified'], reverse=True)
        
        return render_template('dashboard.html', 
                             artist=artist, 
                             files=files,
                             file_count=len(files),
                             total_size=format_size(total_size))
    except Exception as e:
        return f"Error: {e}"

@app.route('/upload', methods=['POST'])
def upload():
    if 'artist' not in session:
        return redirect(url_for('index'))
    artist = session['artist']
    file = request.files.get('file')
    
    if file and file.filename:
        filename = secure_filename(file.filename)
        s3_key = f'artists/{artist}/{filename}'
        s3_client.upload_fileobj(file, S3_BUCKET, s3_key)
    
    return redirect(url_for('dashboard'))

@app.route('/download/<filename>')
def download(filename):
    if 'artist' not in session:
        return redirect(url_for('index'))
    artist = session['artist']
    s3_key = f'artists/{artist}/{filename}'
    
    response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
    return send_file(io.BytesIO(response['Body'].read()), download_name=filename, as_attachment=True)

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    if 'artist' not in session:
        return redirect(url_for('index'))
    artist = session['artist']
    s3_key = f'artists/{artist}/{filename}'
    s3_client.delete_object(Bucket=S3_BUCKET, Key=s3_key)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
