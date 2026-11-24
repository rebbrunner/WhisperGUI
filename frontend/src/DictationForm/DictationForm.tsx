import { useState, useRef } from 'react';
import './DictationForm.css';

export interface DictationFormProps {
    btnLbl?: string;
}
function DictationForm({ btnLbl = 'Process' }: DictationFormProps) {
    const [text, setText] = useState('');
    const [isRecording, setIsRecording] = useState(false);
    const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const chunksRef = useRef<Blob[]>([]);

    const handleTranscription = async (blob: Blob) => {
        const formData = new FormData();
        formData.append('file', blob, "audio.webm");
        
        const res = await fetch('http://127.0.0.1:8000/transcribe', {
            method: 'POST',
            body: formData
        });
        const data = await res.json();
        setText(data.transcribed_text);
    };

    const handleProcess = async () => {
        if (audioBlob) {
            await handleTranscription(audioBlob);
        } else {
            alert('Please record audio first.');
        }
    };

    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const mediaRecorder = new MediaRecorder(stream, {
                mimeType: 'audio/webm;codecs=opus'
            });
            
            mediaRecorderRef.current = mediaRecorder;
            chunksRef.current = [];
            
            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    chunksRef.current.push(event.data);
                }
            };
            
            mediaRecorder.onstop = () => {
                const blob = new Blob(chunksRef.current, { type: 'audio/webm;codecs=opus' });
                setAudioBlob(blob);
            };
            
            mediaRecorder.start();
            setIsRecording(true);
        } catch (error) {
            console.error('Error accessing microphone:', error);
            alert('Could not access microphone. Please ensure you have granted permission.');
        }
    };

    const stopRecording = () => {
        if (mediaRecorderRef.current && isRecording) {
            mediaRecorderRef.current.stop();
            mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop());
            setIsRecording(false);
        }
    };

    const toggleRecording = async () => {
        if (!isRecording) {
            await startRecording();
        } else {
            stopRecording();
        }
    };

    return(
        <>
            <div className="left">
                <div className={`mic ${isRecording ? 'is-recording' : ''}`} onClick={toggleRecording} style={{ cursor: 'pointer' }}>
                    <i className="fas fa-microphone"></i>
                </div>
                <form action="#">
                    <button type="button" onClick={handleProcess} disabled={!audioBlob}>
                        {btnLbl}
                    </button>
                </form>
            </div>
            <div className="right">
                <textarea name="textOut" id="textOut" value={text}></textarea>
            </div>
        </>
    )

}

export default DictationForm;
