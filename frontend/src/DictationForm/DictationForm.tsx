import { useState } from 'react';
import './DictationForm.css';

export interface DictationFormProps {
    btnLbl?: string;
}
function DictationForm({ btnLbl = 'Process' }: DictationFormProps) {
    const [text, setText] = useState('');

    async function transcribe() {
        const res = await fetch('http://127.0.0.1:8000/transcribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input_path: 'D:/Dev/WhisperGUI/backend/test_recording.wav'})
        })
        const data = await res.json();
        setText(data.transcribed_text);
    }

    return(
        <>
            <div className="left">
                <div className="mic"><i className="fas fa-microphone"></i></div>
                <form action="#">
                    <button type="button" onClick={transcribe}>{btnLbl}</button>
                </form>
            </div>
            <div className="right">
                <textarea name="textOut" id="textOut" value={text}></textarea>
            </div>
        </>
    )
}

export default DictationForm;
