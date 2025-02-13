import whisper
import gradio as gr
import os

# Available Whisper models
WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]

# Supported languages
LANGUAGES = {
    "Auto-Detect": None, "English": "en", "Spanish": "es", "French": "fr",
    "German": "de", "Italian": "it", "Portuguese": "pt", "Dutch": "nl",
    "Russian": "ru", "Chinese": "zh", "Japanese": "ja", "Korean": "ko",
    "Arabic": "ar", "Hindi": "hi", "Turkish": "tr"
}

# Default model
current_model_name = "base"
current_model = whisper.load_model(current_model_name)

def transcribe_audio(audio, selected_language, selected_model):
    """ Transcribe audio and save as .txt file """
    global current_model, current_model_name

    # Load the selected model if different
    if selected_model != current_model_name:
        current_model = whisper.load_model(selected_model)
        current_model_name = selected_model

    language_code = LANGUAGES[selected_language]

    # Transcribe with selected language or auto-detect
    if language_code:
        result = current_model.transcribe(audio, language=language_code)
    else:
        result = current_model.transcribe(audio)

    transcript_text = result["text"]

    # Save the transcription as a .txt file
    transcript_path = os.path.splitext(audio)[0] + "_transcription.txt"
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(transcript_text)

    return transcript_text, transcript_path

# Create Gradio interface
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(sources=["upload"], type="filepath"),
        gr.Dropdown(choices=list(LANGUAGES.keys()), value="Auto-Detect", label="Select Language"),
        gr.Dropdown(choices=WHISPER_MODELS, value="base", label="Select Model")
    ],
    outputs=[
        "text", gr.File(label="Download Transcription")
    ],
    title="Careless Whisper Transcription",
    description="Upload an audio file and select a Whisper model & language (or use auto-detect) for transcription. You can download the transcription as a .txt file."
)

# Launch the interface
iface.launch()
