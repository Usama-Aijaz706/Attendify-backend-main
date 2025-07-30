# 🎓 Attendify - AI-Powered Face Recognition Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-4.3+-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

**Revolutionary AI-powered attendance system using face recognition technology**

[🚀 Features](#-features) • [🏗️ Architecture](#️-architecture) • [⚡ Quick Start](#-quick-start) • [📚 API Documentation](#-api-documentation) • [🚀 Deployment](#-deployment) • [🛠️ Development](#️-development)

</div>

---

## 🚀 Features

### ✨ Core Features
- **🤖 AI Face Recognition**: Advanced face detection and recognition using `face_recognition` library
- **📊 Real-time Attendance**: Instant attendance marking with live video processing
- **👥 Student Management**: Complete CRUD operations for student registration and management
- **📈 Attendance Reports**: Comprehensive attendance tracking and reporting
- **🌐 RESTful API**: Full REST API with automatic documentation
- **🔒 Secure Authentication**: MongoDB-based data persistence with secure connections

### 🎯 Advanced Capabilities
- **📸 Bulk Student Registration**: Upload multiple students with images via CSV/Excel
- **🎥 Live Webcam Integration**: Real-time face detection and recognition
- **📱 Cross-Platform**: Works with web, mobile, and desktop applications
- **⚡ High Performance**: Optimized for real-time processing with face filtering
- **🔄 Session Management**: Intelligent attendance session handling
- **📊 Analytics**: Detailed attendance analytics and reporting

---

## 🏗️ Architecture

```mermaid
graph TB
    A[📱 Client Applications] --> B[🌐 FastAPI Backend]
    B --> C[🤖 Face Recognition Engine]
    B --> D[🗄️ MongoDB Database]
    C --> E[📸 Image Processing]
    E --> F[🔍 Face Detection]
    F --> G[🧠 Face Embeddings]
    G --> H[✅ Attendance Records]
    H --> D
    
    subgraph "Backend Services"
        I[👥 Student Management]
        J[📊 Attendance Processing]
        K[📈 Reporting Engine]
    end
    
    B --> I
    B --> J
    B --> K
```

### 🏛️ System Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend API** | FastAPI | RESTful API server with automatic docs |
| **Face Recognition** | face_recognition + dlib | AI-powered face detection and matching |
| **Database** | MongoDB + Beanie ODM | NoSQL data persistence |
| **Image Processing** | OpenCV | Real-time image enhancement and filtering |
| **Containerization** | Docker | Easy deployment and scaling |
| **Client Tools** | Python + OpenCV | Webcam testing and bulk upload |

---

## ⚡ Quick Start

### 🐳 Using Docker (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/Usama-Aijaz706/Attendify-backend-main.git
cd Attendify-backend-main

# 2. Set up environment variables
cp .env.example .env
# Edit .env with your MongoDB connection string

# 3. Run with Docker
docker build -t attendify-backend .
docker run -p 8000:8000 attendify-backend

# 4. Access the API
# 🌐 API: http://localhost:8000
# 📚 Docs: http://localhost:8000/docs
```

### 🐍 Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export MONGO_URI="mongodb://localhost:27017"
export DATABASE_NAME="attendify_db"

# 3. Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📚 API Documentation

### 🔗 Base URL
```
http://localhost:8000
```

### 📖 Interactive Documentation
Visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

### 🎯 Core Endpoints

#### 👥 Student Management
```http
POST   /admin/students/register          # Register new student
GET    /admin/students                   # Get all students
GET    /admin/students/{roll_no}         # Get student by roll number
PUT    /admin/students/{roll_no}         # Update student
DELETE /admin/students/{roll_no}         # Delete student
POST   /admin/students/bulk_register_metadata  # Bulk registration
```

#### 📊 Attendance Processing
```http
POST   /attend/process_frame             # Process attendance frame
GET    /attendance/{roll_no}             # Get student attendance
GET    /attendance/report/class          # Class attendance report
POST   /attendance/manual                # Manual attendance entry
PUT    /attendance/manual/{record_id}    # Update attendance
POST   /attendance/close_session         # Close attendance session
```

#### 🎥 Camera Control
```http
POST   /start_camera                     # Start webcam
POST   /stop_camera                      # Stop webcam
POST   /capture_frame                    # Capture and process frame
```

#### 📈 Analytics & Reports
```http
GET    /attendance/report/all            # All attendance records
GET    /attendance/summary/by_subject_and_section  # Attendance summary
GET    /attendance/by_teacher_class_section        # Teacher-specific reports
```

---

## 🚀 Deployment

### ☁️ Azure App Service

```bash
# 1. Create Azure Web App for Containers
# 2. Connect to GitHub repository
# 3. Set environment variables:
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
DATABASE_NAME=attendify_db

# 4. Deploy automatically from GitHub
```

### 🐳 Docker Deployment

```bash
# Build and push to Docker Hub
docker build -t yourusername/attendify-backend .
docker push yourusername/attendify-backend

# Deploy to any container platform
docker run -p 8000:8000 yourusername/attendify-backend
```

### 🌐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | `mongodb://localhost:27017` |
| `DATABASE_NAME` | Database name | `attendify_db` |

---

## 🛠️ Development

### 📁 Project Structure

```
Attendify-backend-main/
├── 📄 main.py                    # FastAPI application entry point
├── 🗄️ database.py               # MongoDB connection setup
├── 🧠 models.py                  # Data models (Student, Attendance)
├── 🤖 face_service.py           # Face recognition logic
├── 📸 prepare_student_data.py   # Student image processing
├── ⬆️ upload_students.py        # Bulk student upload
├── 🎥 webcam_test_client.py     # Webcam testing client
├── 🐳 Dockerfile                # Docker configuration
├── 📋 requirements.txt          # Python dependencies
├── 📖 Procfile                  # Deployment configuration
└── 📚 README.md                 # This file
```

### 🔧 Development Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up MongoDB
# Install MongoDB locally or use MongoDB Atlas

# 4. Run development server
uvicorn main:app --reload
```

### 🧪 Testing

```bash
# Test attendance endpoint
python test_attendance_endpoint.py

# Test webcam client
python webcam_test_client.py

# Test bulk upload
python prepare_student_data.py --source_dir ./Student_Photos --class_name "BSCS 8th" --section "B"
python upload_students.py
```

---

## 📊 Data Models

### 👤 Student Model
```python
class Student(Document):
    roll_no: str                    # Unique roll number
    name: str                       # Student name
    class_name: str                 # Class name
    section: str                    # Section
    face_embeddings: List[FaceEmbedding]  # Face recognition data
```

### 📝 Attendance Record Model
```python
class AttendanceRecord(Document):
    student_id: str                 # Student reference
    roll_no: str                    # Roll number
    name: str                       # Student name
    class_name: str                 # Class name
    section: str                    # Section
    teacher_name: str               # Teacher name
    date: str                       # Attendance date
    time: str                       # Attendance time
    status: str                     # Present/Absent/Leave
    subject_name: str               # Subject name
    class_time: str                 # Class time
```

---

## 🔧 Configuration

### 🎛️ Face Recognition Settings

```python
# Minimum face size for detection (pixels)
MIN_FACE_SIZE = 80

# Maximum aspect ratio for face filtering
MAX_ASPECT_RATIO = 1.5

# Face recognition tolerance (0.0 = strict, 1.0 = lenient)
RECOGNITION_TOLERANCE = 0.5
```

### ⚡ Performance Settings

```python
# Frame processing interval (seconds)
SEND_INTERVAL = 2.0

# Frame skip for local detection
FRAME_SKIP = 10

# Unrecognized face retry interval
UNRECOGNIZED_RETRY_INTERVAL = 5.0
```

---

## 🎯 Usage Examples

### 📸 Register a Student

```python
import requests

# Register student with face image
files = {'images': open('student_photo.jpg', 'rb')}
data = {
    'roll_no': '10148',
    'name': 'Usama Aijaz',
    'class_name': 'BSCS 8th',
    'section': 'B'
}

response = requests.post(
    'http://localhost:8000/admin/students/register',
    files=files,
    data=data
)
print(response.json())
```

### 🎥 Process Attendance

```python
# Process attendance frame
files = {'file': open('frame.jpg', 'rb')}
data = {
    'class_id': 'BSCS 8th',
    'teacher_name': 'Miss Maria Khattak',
    'subject_name': 'Mathematics'
}

response = requests.post(
    'http://localhost:8000/attend/process_frame',
    files=files,
    data=data
)
print(response.json())
```

### 📊 Get Attendance Report

```python
# Get student attendance
response = requests.get('http://localhost:8000/attendance/10148')
attendance_data = response.json()
print(f"Found {attendance_data['total_records']} attendance records")
```

---

## 🔒 Security Considerations

### 🛡️ Production Security
- ✅ Use HTTPS in production
- ✅ Implement authentication for admin endpoints
- ✅ Configure CORS for specific domains
- ✅ Use environment variables for sensitive data
- ✅ Regular security updates

### 🔐 API Security
```python
# Configure CORS for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

---

## 🐛 Troubleshooting

### ❌ Common Issues

| Issue | Solution |
|-------|----------|
| **dlib build fails** | Use Docker or upgrade to Premium SKU on Azure |

### 🔧 Debug Mode

```bash
# Enable debug logging
export PYTHONPATH=.
python -m uvicorn main:app --reload --log-level debug
```

---

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### 📋 Development Guidelines
- ✅ Follow PEP 8 style guidelines
- ✅ Add type hints to new functions
- ✅ Include docstrings for new endpoints
- ✅ Test new features thoroughly
- ✅ Update documentation

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **FastAPI** - Modern, fast web framework
- **face_recognition** - Simple face recognition library
- **OpenCV** - Computer vision library
- **MongoDB** - NoSQL database
- **Beanie** - MongoDB ODM for Python

---

## 📞 Support

- **📧 Email**: [usamaaijaz706@gmail.com]
- **🐛 Issues**: [GitHub Issues](https://github.com/Usama-Aijaz706/Attendify-backend-main/issues)
- **📖 Documentation**: [API Docs](http://localhost:8000/docs)

---

<div align="center">

**Made with ❤️ by the Usama Aijaz**

[⬆️ Back to Top](#-attendify---ai-powered-face-recognition-attendance-system)

</div> 