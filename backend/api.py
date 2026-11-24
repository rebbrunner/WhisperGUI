import os
import tempfile

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from whisper_cli import Transcriber

load_dotenv()

ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', 'http://localhost:5173').split(',')

app = FastAPI(title="Transcriber API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

transcriber = None

@app.on_event('startup')
def startup_event():
    global transcriber
    transcriber = Transcriber(os.getenv('CACHE_PATH'))

@app.post('/transcribe')
async def transcribe_file(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}")
    
    content = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix=os.path.splitext(file.filename)[1]) as temp_file:
        temp_file.write(content)
        temp_path = temp_file.name
    
    try:
        result = transcriber.transcribe(temp_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    return {
        'transcribed_text': result
    }

if __name__ == '__main__':

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
