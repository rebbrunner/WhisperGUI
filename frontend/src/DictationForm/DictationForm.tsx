import './DictationForm.css';


export interface DictationFormProps {
    btnLbl?: string;
}
function DictationForm({ btnLbl = 'Process' }: DictationFormProps) {
    return(
        <>
            <div className="left">
                <div className="mic"><i className="fas fa-microphone"></i></div>
                <form action="#">
                    <button>{btnLbl}</button>
                </form>
            </div>
            <div className="right">
                <textarea name="textOut" id="textOut"></textarea>
            </div>
        </>
    )
}

export default DictationForm;
