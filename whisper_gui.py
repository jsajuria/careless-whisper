import whisper
import gradio as gr

# Load the model once
model = whisper.load_model("medium")

def transcribe_audio(audio):
    result = model.transcribe(audio)
    return result["text"]

# Create a simple Gradio interface
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(sources=["upload"], type="filepath"),
    outputs="text",
    title="Careless Whisper Transcription",
    description="Upload an audio file and get a transcription using OpenAI Whisper.",
)

# Launch the interface
iface.launch()
