# 🎤 Careless Whisper - AI Web-Based Transcription App  
README file created with the help of ChatGPT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)  
[![Whisper](https://img.shields.io/badge/Powered%20By-OpenAI%20Whisper-blue)](https://openai.com/research/whisper)  

🚀 **Careless Whisper** is a **web-based transcription tool** that uses OpenAI’s **Whisper model** to transcribe audio files into text.  
This app runs **locally** on your machine, ensuring privacy while providing **real-time progress updates**.  

## **🔹 Features**  
✅ **Upload & Transcribe**: Supports `.mp3`, `.wav`, `.m4a` files.  
✅ **Fast & Simple**: Just upload a file and get instant transcription.  
✅ **Privacy-Friendly**: Runs entirely **locally**—no cloud processing.  
✅ **User-Friendly Web UI**: Powered by **Gradio**

---

## **📸 Screenshots**  
![Screenshot of Whisper AI Web App](./assets/Screenshot.png)  

---

## **💻 Installation & Usage**  
### **1️⃣ Prerequisites**  
Ensure you have:  
- **Python 3.8+** → [Download here](https://www.python.org/downloads/)  
- **FFmpeg** → Install via Homebrew:  
  ```bash
  brew install ffmpeg
  ```
- **Pip & Virtual Environment (Recommended)**

---

### **2️⃣ Clone the repository**  
```bash
git clone https://github.com/jsajuria/careless-whisper.git
cd careless-whisper
```

---

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### **4️⃣ Run the Desktop App**
```bash
python whisper_gui.py
```
Then open your browser and go to:
👉 http://127.0.0.1:7860

---

📂 **File Structure**

```bash
careless-whisper-transcription/
│── whisper_gui.py      # Main web app
│── assets/             # Icons, screenshots, and branding
│── flagged/            # (Optional) Saves generated text files into a csv
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
```



