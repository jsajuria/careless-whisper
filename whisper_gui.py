import whisper
import gradio as gr

# Available Whisper models
WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]

# Supported languages for selection
LANGUAGES = {
    "Auto-Detect": None, "English": "en", "Spanish": "es", "French": "fr",
    "German": "de", "Italian": "it", "Portuguese": "pt", "Dutch": "nl",
    "Russian": "ru", "Chinese": "zh", "Japanese": "ja", "Korean": "ko",
    "Arabic": "ar", "Hindi": "hi", "Turkish": "tr"
}

# Default model (loaded at startup)
current_model_name = "base"  # Track model name separately
current_model = whisper.load_model(current_model_name)

def transcribe_audio(audio, selected_language, selected_model):
    """ Transcribe audio with selected Whisper model and language """
    global current_model, current_model_name

    # Load a new model only if the user selects a different one
    if selected_model != current_model_name:
        current_model = whisper.load_model(selected_model)
        current_model_name = selected_model  # Update the tracked model name

    language_code = LANGUAGES[selected_language]

    # Transcribe with selected language or auto-detect
    if language_code:
        result = current_model.transcribe(audio, language=language_code)
    else:
        result = current_model.transcribe(audio)  # Auto-detect language

    return result["text"]

# Create Gradio interface
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=[
        gr.Audio(sources=["upload"], type="filepath"),
        gr.Dropdown(choices=list(LANGUAGES.keys()), value="Auto-Detect", label="Select Language"),
        gr.Dropdown(choices=WHISPER_MODELS, value="base", label="Select Model")
    ],
    outputs="text",
    title="Careless Whisper Transcription",
    description="Upload an audio file and select a Whisper model & language (or use auto-detect) for transcription."
)

# Launch the interface
iface.launch()
