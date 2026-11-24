from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.whisper_cli import Transcriber

app = FastAPI(title="Transcriber API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

transcriber = None

@app.on_event('startup')
def startup_event():
    global transcriber
    transcriber = Transcriber()

class TranscribeRequest(BaseModel):
    input_path: str
@app.post('/transcribe')
async def transcribe_path(request: TranscribeRequest):
    result = transcriber.transcribe(request.input_path)
    return {
        'transcribed_text': result
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
