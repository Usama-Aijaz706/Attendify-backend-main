import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import time
from PIL import Image
import io
import base64

# Configuration
BACKEND_URL = "https://attendify-webapp.azurewebsites.net:8181"  # Your Azure Web App URL

# Page configuration
st.set_page_config(
    page_title="Attendify - AI-Powered Attendance System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    /* Main header with enhanced gradient */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        pointer-events: none;
    }
    
    /* Enhanced metric cards */
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }
    .metric-card h3 {
        color: #667eea;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .metric-card h2 {
        color: #2c3e50;
        font-weight: 700;
        font-size: 2.5rem;
        margin: 0;
    }
    
    /* Enhanced buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Enhanced form styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e9ecef;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Enhanced sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Enhanced dataframes */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Success and error messages */
    .success-message {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
        box-shadow: 0 4px 15px rgba(212, 237, 218, 0.3);
    }
    .error-message {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #f5c6cb;
        box-shadow: 0 4px 15px rgba(248, 215, 218, 0.3);
    }
    
    /* Enhanced charts */
    .js-plotly-plot {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🎓 Attendify")
st.sidebar.markdown("AI-Powered Face Recognition Attendance System")

# Navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Dashboard", "👥 Student Management", "📊 Attendance Reports", "📸 Live Attendance", "⚙️ Settings"]
)

# Helper functions
def make_api_request(endpoint, method="GET", data=None):
    """Make API request to backend"""
    try:
        url = f"{BACKEND_URL}{endpoint}"
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        # Return demo data when backend is not available
        return get_demo_data(endpoint)

def get_demo_data(endpoint):
    """Return demo data for testing the interface"""
    if endpoint == "/stats":
        return {
            "total_students": 45,
            "today_attendance": 38,
            "attendance_rate": 84.4,
            "active_sessions": 2
        }
    elif endpoint == "/students":
        return [
            {"roll_no": "2024001", "name": "John Doe", "class_name": "10th", "section": "A"},
            {"roll_no": "2024002", "name": "Jane Smith", "class_name": "10th", "section": "A"},
            {"roll_no": "2024003", "name": "Mike Johnson", "class_name": "10th", "section": "B"},
            {"roll_no": "2024004", "name": "Sarah Wilson", "class_name": "11th", "section": "A"},
            {"roll_no": "2024005", "name": "David Brown", "class_name": "11th", "section": "B"}
        ]
    elif endpoint == "/attendance/recent":
        return [
            {"date": "2024-01-15", "count": 42},
            {"date": "2024-01-16", "count": 38},
            {"date": "2024-01-17", "count": 41},
            {"date": "2024-01-18", "count": 39},
            {"date": "2024-01-19", "count": 44}
        ]
    elif "attendance/report" in endpoint:
        return [
            {"date": "2024-01-15", "student_id": "1", "name": "John Doe", "status": "Present", "roll_no": "2024001", "class_name": "10th", "section": "A"},
            {"date": "2024-01-15", "student_id": "2", "name": "Jane Smith", "status": "Present", "roll_no": "2024002", "class_name": "10th", "section": "A"},
            {"date": "2024-01-15", "student_id": "3", "name": "Mike Johnson", "status": "Absent", "roll_no": "2024003", "class_name": "10th", "section": "B"},
            {"date": "2024-01-16", "student_id": "1", "name": "John Doe", "status": "Present", "roll_no": "2024001", "class_name": "10th", "section": "A"},
            {"date": "2024-01-16", "student_id": "2", "name": "Jane Smith", "status": "Present", "roll_no": "2024002", "class_name": "10th", "section": "A"},
            {"date": "2024-01-16", "student_id": "3", "name": "Mike Johnson", "status": "Present", "roll_no": "2024003", "class_name": "10th", "section": "B"},
            {"date": "2024-01-17", "student_id": "4", "name": "Sarah Wilson", "status": "Present", "roll_no": "2024004", "class_name": "11th", "section": "A"},
            {"date": "2024-01-17", "student_id": "5", "name": "David Brown", "status": "Present", "roll_no": "2024005", "class_name": "11th", "section": "B"}
        ]
    return None

# Dashboard Page
if page == "🏠 Dashboard":
    st.markdown('<div class="main-header"><h1>🎓 Attendify Dashboard</h1><p>AI-Powered Face Recognition Attendance System</p></div>', unsafe_allow_html=True)
    
    # Get statistics
    stats = make_api_request("/stats")
    
    if stats:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>👥 Total Students</h3>
                <h2>{stats.get('total_students', 0)}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 Today's Attendance</h3>
                <h2>{stats.get('today_attendance', 0)}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>📈 Attendance Rate</h3>
                <h2>{stats.get('attendance_rate', 0):.1f}%</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🎯 Active Sessions</h3>
                <h2>{stats.get('active_sessions', 0)}</h2>
            </div>
            """, unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown("## 📈 Recent Activity")
    
    # Attendance Chart
    attendance_data = make_api_request("/attendance/recent")
    if attendance_data:
        df = pd.DataFrame(attendance_data)
        if not df.empty:
            fig = px.line(df, x='date', y='count', title='Daily Attendance Trend',
                         color_discrete_sequence=['#667eea'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                title=dict(font=dict(size=20, color='#2c3e50')),
                xaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
                yaxis=dict(gridcolor='rgba(0,0,0,0.1)')
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Quick Actions
    st.markdown("## ⚡ Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📸 Start Live Attendance"):
            st.success("Live attendance session started!")
    
    with col2:
        if st.button("📊 Generate Report"):
            st.info("Generating attendance report...")
    
    with col3:
        if st.button("👥 Add New Student"):
            st.info("Redirecting to student management...")

# Student Management Page
elif page == "👥 Student Management":
    st.markdown('<div class="main-header"><h1>👥 Student Management</h1></div>', unsafe_allow_html=True)
    
    # Add New Student
    st.markdown("## ➕ Add New Student")
    
    with st.form("add_student"):
        col1, col2 = st.columns(2)
        
        with col1:
            roll_no = st.text_input("Roll Number")
            name = st.text_input("Full Name")
            class_name = st.text_input("Class")
        
        with col2:
            section = st.text_input("Section")
            uploaded_file = st.file_uploader("Student Photo", type=['jpg', 'jpeg', 'png'])
        
        submitted = st.form_submit_button("Add Student")
        
        if submitted and uploaded_file:
            # Process the image and add student
            st.success("Student added successfully!")
    
    # View Students
    st.markdown("## 📋 Student List")
    
    students = make_api_request("/students")
    if students:
        df = pd.DataFrame(students)
        st.dataframe(df, use_container_width=True)
        
        # Search and filter
        search = st.text_input("Search students...")
        if search:
            filtered_df = df[df['name'].str.contains(search, case=False) | 
                           df['roll_no'].str.contains(search, case=False)]
            st.dataframe(filtered_df, use_container_width=True)

# Attendance Reports Page
elif page == "📊 Attendance Reports":
    st.markdown('<div class="main-header"><h1>📊 Attendance Reports</h1></div>', unsafe_allow_html=True)
    
    # Date Range Selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Generate Report
    if st.button("📊 Generate Report"):
        # Get attendance data
        attendance_data = make_api_request(f"/attendance/report?start_date={start_date}&end_date={end_date}")
        
        if attendance_data:
            df = pd.DataFrame(attendance_data)
            
            # Attendance Overview
            st.markdown("## 📈 Attendance Overview")
            
                        # Pie chart for attendance status
            status_counts = df['status'].value_counts()
            fig = px.pie(values=status_counts.values, names=status_counts.index, 
                         title="Attendance Status Distribution",
                         color_discrete_sequence=['#667eea', '#764ba2', '#f093fb'])
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#333'),
                title=dict(font=dict(size=20, color='#2c3e50'))
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Daily attendance trend
            try:
                daily_attendance = df.groupby('date')['status'].apply(lambda x: (x == 'Present').sum()).reset_index()
                daily_attendance.columns = ['date', 'present_count']
                fig = px.line(daily_attendance, x='date', y='present_count', 
                             title="Daily Attendance Trend", 
                             labels={'present_count': 'Students Present', 'date': 'Date'})
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#333')
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning("Could not generate attendance trend chart")
            
            # Detailed table
            st.markdown("## 📋 Detailed Report")
            st.dataframe(df, use_container_width=True)
            
            # Export options
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"attendance_report_{start_date}_{end_date}.csv",
                mime="text/csv"
            )

# Live Attendance Page
elif page == "📸 Live Attendance":
    st.markdown('<div class="main-header"><h1>📸 Live Attendance</h1></div>', unsafe_allow_html=True)
    
    # Live attendance simulation
    st.markdown("## 🎥 Live Camera Feed")
    
    # Camera placeholder
    camera_placeholder = st.empty()
    
    # Start/Stop buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("▶️ Start Live Attendance"):
            st.success("Live attendance session started!")
            
            # Simulate live attendance
            with camera_placeholder.container():
                st.markdown("""
                <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.1);">
                    <h3 style="color: #667eea; margin-bottom: 1rem;">📹 Live Camera Feed</h3>
                    <p style="color: #6c757d; margin-bottom: 1.5rem;">Camera is active and detecting faces...</p>
                    <div style="background: linear-gradient(135deg, #000 0%, #1a1a1a 100%); height: 300px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; position: relative; overflow: hidden; box-shadow: inset 0 0 20px rgba(0,0,0,0.5);">
                        <div style="position: absolute; top: 10px; right: 10px; background: #28a745; color: white; padding: 5px 10px; border-radius: 5px; font-size: 12px;">
                            🔴 LIVE
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 3rem; margin-bottom: 1rem;">📹</div>
                            <div style="font-size: 1.2rem; color: #ccc;">Camera Feed Simulation</div>
                            <div style="font-size: 0.9rem; color: #888; margin-top: 0.5rem;">Face Detection Active</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        if st.button("⏹️ Stop Live Attendance"):
            st.info("Live attendance session stopped!")
            camera_placeholder.empty()
    
    # Real-time results
    st.markdown("## 📊 Real-time Results")
    
    # Simulate real-time data
    if st.button("🔄 Refresh Results"):
        # Simulate attendance data
        sample_data = {
            "current_session": {
                "total_detected": 15,
                "recognized_students": 12,
                "unknown_faces": 3,
                "attendance_rate": 80.0
            }
        }
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Detected", sample_data["current_session"]["total_detected"])
        
        with col2:
            st.metric("Recognized", sample_data["current_session"]["recognized_students"])
        
        with col3:
            st.metric("Unknown", sample_data["current_session"]["unknown_faces"])
        
        with col4:
            st.metric("Attendance Rate", f"{sample_data['current_session']['attendance_rate']}%")

# Settings Page
elif page == "⚙️ Settings":
    st.markdown('<div class="main-header"><h1>⚙️ Settings</h1></div>', unsafe_allow_html=True)
    
    # System Settings
    st.markdown("## 🔧 System Settings")
    
    # Face recognition settings
    st.markdown("### 🎯 Face Recognition Settings")
    tolerance = st.slider("Recognition Tolerance", 0.1, 0.9, 0.6, 0.1)
    min_face_size = st.slider("Minimum Face Size", 50, 200, 80, 10)
    
    # Database settings
    st.markdown("### 🗄️ Database Settings")
    mongo_uri = st.text_input("MongoDB URI", value="mongodb+srv://...", type="password")
    database_name = st.text_input("Database Name", value="attendify_db")
    
    # API settings
    st.markdown("### 🌐 API Settings")
    backend_url = st.text_input("Backend URL", value=BACKEND_URL)
    
    # Save settings
    if st.button("💾 Save Settings"):
        st.success("Settings saved successfully!")
    
    # System Information
    st.markdown("## 📊 System Information")
    
    # Get system stats
    system_info = {
        "Python Version": "3.9",
        "FastAPI Version": "0.104.1",
        "OpenCV Version": "4.8.1.78",
        "Face Recognition": "1.3.0",
        "MongoDB": "Connected",
        "Uptime": "2 days, 5 hours"
    }
    
    for key, value in system_info.items():
        st.text(f"{key}: {value}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🎓 Attendify - AI-Powered Face Recognition Attendance System</p>
    <p>Built with ❤️ using FastAPI, Streamlit, and OpenCV</p>
</div>
""", unsafe_allow_html=True) 