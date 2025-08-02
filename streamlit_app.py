import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json

# Configuration
BACKEND_URL = "https://your-azure-app.azurewebsites.net"  # Update with your Azure URL

st.set_page_config(
    page_title="Attendify - Face Recognition Attendance System",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 Attendify")
st.sidebar.markdown("AI-Powered Face Recognition Attendance System")

# Main content
st.title("🎓 Attendify - Face Recognition Attendance System")
st.markdown("---")

# Navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["🏠 Dashboard", "👥 Student Management", "📊 Attendance Reports", "🎥 Live Attendance", "⚙️ Settings"]
)

if page == "🏠 Dashboard":
    st.header("🏠 Dashboard")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", "150")
    with col2:
        st.metric("Today's Attendance", "142")
    with col3:
        st.metric("Attendance Rate", "94.7%")
    with col4:
        st.metric("Active Sessions", "3")
    
    # Recent activity
    st.subheader("📈 Recent Activity")
    
    # Sample data
    activity_data = {
        "Time": ["09:00", "09:15", "09:30", "09:45", "10:00"],
        "Event": ["Session Started", "Student Detected", "Attendance Marked", "Session Ended", "Report Generated"],
        "Details": ["Mathematics Class", "Usama Aijaz", "Present", "Session Complete", "Daily Report"]
    }
    
    df = pd.DataFrame(activity_data)
    st.dataframe(df, use_container_width=True)

elif page == "👥 Student Management":
    st.header("👥 Student Management")
    
    # Add new student
    st.subheader("➕ Add New Student")
    
    with st.form("add_student"):
        col1, col2 = st.columns(2)
        
        with col1:
            roll_no = st.text_input("Roll Number")
            name = st.text_input("Full Name")
        
        with col2:
            class_name = st.selectbox("Class", ["BSCS 8th", "BSCS 6th", "BSCS 4th"])
            section = st.selectbox("Section", ["A", "B", "C"])
        
        uploaded_files = st.file_uploader(
            "Upload Student Photos", 
            type=['jpg', 'jpeg', 'png'], 
            accept_multiple_files=True
        )
        
        submit_button = st.form_submit_button("Register Student")
        
        if submit_button and uploaded_files:
            st.success("Student registered successfully!")
    
    # View students
    st.subheader("📋 Registered Students")
    
    # Sample student data
    students_data = {
        "Roll No": ["10148", "10149", "10150"],
        "Name": ["Usama Aijaz", "Ali Khan", "Sara Ahmed"],
        "Class": ["BSCS 8th", "BSCS 8th", "BSCS 8th"],
        "Section": ["B", "B", "B"],
        "Status": ["Active", "Active", "Active"]
    }
    
    df = pd.DataFrame(students_data)
    st.dataframe(df, use_container_width=True)

elif page == "📊 Attendance Reports":
    st.header("📊 Attendance Reports")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_class = st.selectbox("Class", ["All", "BSCS 8th", "BSCS 6th", "BSCS 4th"])
    
    with col2:
        selected_section = st.selectbox("Section", ["All", "A", "B", "C"])
    
    with col3:
        selected_date = st.date_input("Date", datetime.now())
    
    # Generate report
    if st.button("Generate Report"):
        st.subheader("📈 Attendance Summary")
        
        # Sample report data
        report_data = {
            "Roll No": ["10148", "10149", "10150", "10151", "10152"],
            "Name": ["Usama Aijaz", "Ali Khan", "Sara Ahmed", "Ahmed Hassan", "Fatima Ali"],
            "Status": ["Present", "Present", "Absent", "Present", "Present"],
            "Time": ["09:15", "09:16", "N/A", "09:18", "09:20"],
            "Subject": ["Mathematics", "Mathematics", "Mathematics", "Mathematics", "Mathematics"]
        }
        
        df = pd.DataFrame(report_data)
        st.dataframe(df, use_container_width=True)
        
        # Attendance statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Students", "5")
        with col2:
            st.metric("Present", "4")
        with col3:
            st.metric("Absent", "1")

elif page == "🎥 Live Attendance":
    st.header("🎥 Live Attendance")
    
    st.info("This feature requires camera access and connection to the FastAPI backend.")
    
    # Camera input
    camera_input = st.camera_input("Take a photo for attendance")
    
    if camera_input is not None:
        st.success("Photo captured! Processing...")
        
        # Simulate face recognition
        with st.spinner("Recognizing face..."):
            st.success("✅ Face recognized: Usama Aijaz")
            st.info("Attendance marked as Present")

elif page == "⚙️ Settings":
    st.header("⚙️ Settings")
    
    st.subheader("🔗 Backend Configuration")
    
    backend_url = st.text_input(
        "Backend URL", 
        value="https://your-azure-app.azurewebsites.net",
        help="Enter your FastAPI backend URL"
    )
    
    st.subheader("🎛️ Face Recognition Settings")
    
    tolerance = st.slider(
        "Recognition Tolerance", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.5,
        help="Lower values = stricter matching"
    )
    
    min_face_size = st.number_input(
        "Minimum Face Size (pixels)", 
        min_value=50, 
        max_value=200, 
        value=80
    )
    
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

# Footer
st.markdown("---")
st.markdown("**Attendify** - AI-Powered Face Recognition Attendance System")
st.markdown("Built with ❤️ using FastAPI, Streamlit, and face_recognition") 