# 📱 Object Detection App with YOLOv8 API

A complete mobile object detection system built with **Flutter** (frontend) and **Flask + YOLOv8** (backend).  
The mobile app allows users to **log in**, **upload images**, and **view detected objects** returned by the YOLOv8 model.

---

## 📂 Project Structure

```
.
├── lib/                      # Flutter app source code
├── assets/                   # App assets
├── server/                   # Flask backend with YOLOv8
├──── ├─── requirements.txt   # Python dependencies
├── pubspec.yaml              # Flutter dependencies
└── README.md                 # Documentation
```

---

## 🚀 Features

✅ **Login / Signup screen** (can be connected to backend or hardcoded credentials)  
✅ **Image picker** (camera or gallery)  
✅ **Sends image to YOLOv8 API**  
✅ **Displays detected objects with confidence scores**  
✅ **Responsive & clean UI**  

---

## 🛠 Setup Instructions

### **1️⃣ Backend (Flask + YOLOv8)**

#### Install dependencies
```bash
cd server
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the server
```bash
python main.py
```
The server will start at:
```
http://127.0.0.1:5000
```

---

### **2️⃣ Mobile App (Flutter)**

#### Install dependencies
```bash
flutter pub get
```

#### Update API URL
In `lib/api_service.dart`:
```dart
static const String _baseUrl = 'http://YOUR_SERVER_IP:5000';
```
> Replace `YOUR_SERVER_IP` with your local IP or deployed server URL.

#### Run the app
```bash
flutter run
```

---

## 📦 Dependencies

### **Flutter**
```yaml
dependencies:
  flutter:
    sdk: flutter
  image_picker: ^1.0.4
  http: ^1.2.1
  flutter_spinkit: ^5.2.0
  google_fonts: ^6.1.0
  lottie: ^2.7.0
```

### **Python (Backend)**
```
flask
flask-cors
ultralytics
opencv-python
numpy
gunicorn
```

---

## 🔑 Login Credentials (Demo)
For testing purposes (hardcoded):
```
Username: test
Password: 1234
```

---

## 🌐 API Usage

### **POST /predict**
Send an image as `multipart/form-data`:
```bash
curl -X POST -F "image=@your_image.jpg" http://127.0.0.1:5000/predict
```

**Response:**
```json
[
  {
    "name": "car",
    "confidence": 0.931
  }
]
```

---




