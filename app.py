from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import yt_dlp
import requests

app = Flask(__name__)
CORS(app) # Esto evita que el navegador bloquee la conexión

@app.route('/')
def index():
    return "Servidor API Hacker Online"

# RUTA 1: Para obtener la información del audio
@app.route('/hack_video', methods=['POST'])
def hack_video():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No se recibió JSON'}), 400
        
    url = data.get('url')
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True, # Evita que intente analizar toda una lista si es un mix
        'extract_flat': False, # Obliga a ir directo al grano
        'skip_download': True, # IMPORTANTE: Solo queremos el link, NO bajarlo al servidor
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                'status': 'SUCCESS',
                'title': info.get('title', 'audio_hacker'),
                'download_link': info.get('url')
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# RUTA 2: Para descargar el archivo real
@app.route('/proxy_download')
def proxy_download():
    video_url = request.args.get('url')
    title = request.args.get('title', 'audio_hacker')
    
    if not video_url:
        return "Falta la URL del video", 400

    filename = "".join([c for c in title if c.isalnum() or c in (' ', '.', '_')]).strip() + ".mp3"
    
    # Hacemos la petición a los servidores de Google/YouTube
    req = requests.get(video_url, stream=True)
    
    return Response(
        req.iter_content(chunk_size=1024*1024),
        headers={
            "Content-Disposition": f"attachment; filename=\"{filename}\"",
            "Content-Type": "audio/mpeg"
        }
    )

if __name__ == '__main__':
    # Importante: Puerto 5000
    app.run(debug=True, port=5000)