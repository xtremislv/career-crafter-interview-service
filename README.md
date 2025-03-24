# Career Crafters: Interview Analysis System

![GitHub License](https://img.shields.io/github/license/NamanT98/Career-Crafter-Interview-System)

## 📌 Introduction
In today's competitive job market, excelling in interviews is crucial. The **Career Crafters Interview Analysis System** is an AI-powered platform designed to simulate interviews, assess both verbal and non-verbal communication skills, and provide detailed feedback to improve performance.

This system evaluates:
- **Audio Communication** (speech fluency, articulation, pauses)
- **Body Language** (posture, gestures)
- **Facial Expressions** (confidence indicators)

🔗 **GitHub Repository:** [Career Crafters Interview System](https://github.com/NamanT98/Career-Crafter-Interview-System)

## 📊 Key Functionalities

### 🎤 Audio Processing
- **Preprocessing:** Enhance signal quality (noise reduction, normalization).
- **Feature Extraction:** Analyze speech rate, articulation, and pause duration.
- **Automatic Speech Recognition (ASR):** Use Google's Speech-to-Text API for transcription.

### 📹 Video Processing
- **Body Pose Estimation:** Analyze posture using the MediaPipe library.
- **Facial Expression Analysis:** Evaluate emotions and confidence using DeepFace and OpenCV.
- **Confidence Prediction:** Integrate audio and video analysis for a comprehensive confidence score.

### 📋 Prompt Generation
- **User Profile Input:** Customize prompts based on user data (education, profession).
- **Dynamic Prompt Generation:** Use Natural Language Generation (NLG) to create contextually relevant prompts.

## 🛠️ System Pipeline
1. **User Registration & Login** – Secure authentication using Django.
2. **User Data Collection** – Collect job-related inputs to tailor interview prompts.
3. **Prompt Generation & Selection** – Generate and display personalized interview prompts.
4. **Interview Simulation** – Record and analyze user responses (audio & video).
5. **Analysis & Feedback** – Provide detailed evaluation on verbal and non-verbal cues.

## 📷 System Output
### Bad Posture Detection
![Bad Posture Detection](https://github.com/user-attachments/assets/b94894d4-1e9c-47cd-ad7c-d6c6a00217ab)


### Good Posture Detection
![Good Posture Detection](https://github.com/user-attachments/assets/75fc368e-d7d0-4fcb-8754-34b7a6e7d1ea)



## 🧰 Technology Stack
- **Backend:** Django (Python), PostgreSQL
- **Audio Analysis:** SpeechRecognition, Praat
- **Video Analysis:** MediaPipe, DeepFace, OpenCV
- **Deployment:** Render (CI/CD integration, automatic scaling)

## 🚀 Deployment Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/NamanT98/Career-Crafter-Interview-System.git
   cd Career-Crafter-Interview-System
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django server:
   ```bash
   python manage.py runserver
   ```
5. Access the platform at `http://localhost:8000`

## 📈 Future Scope
- **MetaFlow Integration:** For advanced workflow management.
- **Custom Model Training:** Classify performance into Low, Average, and Good categories using collected data.

## 📚 References
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [My Voice Analysis](https://github.com/Shahabks/my-voice-analysis/tree/master)
- [Praat Speech Rate Detection](https://www.researchgate.net/publication/24274554)
