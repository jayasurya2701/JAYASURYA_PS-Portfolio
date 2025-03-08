import streamlit as st
import base64

# Page Config with a Modern UI
st.set_page_config(page_title="JAYASURYA PS | AI & Cloud Portfolio", layout="wide")

# Custom CSS for a Stunning UI
st.markdown("""
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Arial', sans-serif;
        }
        .section {
            padding: 30px;
            background: #161b22;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .sidebar .stRadio > label {
            color: #58a6ff;
        }
        h1, h2, h3 {
            color: #58a6ff;
            text-align: center;
        }
        .download-button {
            background-color: #238636;
            color: white;
            border-radius: 8px;
            padding: 12px;
            font-size: 16px;
            text-align: center;
        }
        a {
            color: #58a6ff;
            text-decoration: none;
        }
        .button {
            background-color: #1f6feb;
            padding: 12px;
            border-radius: 8px;
            color: white;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔗 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "💡 Skills", "📄 Resume", "🚀 Projects", "📞 Contact"])

if page == "🏠 Home":
    st.image("profile.jpg", width=200, caption="JAYASURYA PS")
    st.title("JAYASURYA PS")
    st.subheader("AI & Cloud Visionary | B.Tech - AI & Data Science | AWS Certified | Innovation Seeker")
    st.write("""
    🚀 AI & Cloud Enthusiast | Data Science Innovator | AWS Certified | Problem-Solver
    
    Passionate about leveraging AI, cloud computing, and data-driven insights to solve real-world problems.
    """)

elif page == "💡 Skills":
    st.header("💡 Skills")
    skills = ["☁️ Cloud Computing", "🐍 Python", "📊 Machine Learning", "🤖 Deep Learning", "☁️ AWS", "🖥️ Streamlit", "📂 FAISS"]
    for skill in skills:
        st.markdown(f"✅ {skill}")

elif page == "📄 Resume":
    st.header("📄 View & Download My Resume")

    # Google Drive File ID (Extract from your link)
    file_id = "1fa2HqwrHx2h-ILYAXj_6ySb3lUchCENq"

    # Correct Google Drive Embed & Download URLs
    embed_url = f"https://drive.google.com/file/d/{file_id}/preview"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # Display PDF in Streamlit using iframe
    st.markdown(f'<iframe src="{embed_url}" width="100%" height="600px"></iframe>', unsafe_allow_html=True)

    # Provide a download link
    st.markdown(f'<a href="{download_url}" target="_blank"><button>📥 Download Resume</button></a>', unsafe_allow_html=True)

elif page == "🚀 Projects":
    st.header("🚀 Projects")
    projects = {
        "Conversational CSV Chatbot using LLM API": ["AI", "https://github.com/jayasurya2701/Conversational_CSV_Chatbot-using-LLM-"],
        "AI-Driven-Guest-Experience-for-Personalization-System-for-Hosipitality": ["AI", "https://github.com/jayasurya2701/AI-Driven-Guest-Experience-for-Personalization-System-for-Hospitality"],
        "Intent-Based-Chatbot-for-Automated-Queries": ["An advanced AI solution for improving English proficiency.", "https://github.com/jayasurya2701/Intent-Based-Chatbot-for-Automated-Queries"],
        "Face-Detection-and-Recognition-Model-using-Python-and-OpenCV": ["An AI chatbot that interacts with CSV datasets using LLaMA 3 and FAISS.", "https://github.com/jayasurya2701/Face-Detection-and-Recognition-Model-using-Python-and-OpenCV"],
        "WebScrapeX: Automated Google Search Result Extractor": ["An NLP-based chatbot for analyzing JIRA datasets and generating insights.", "https://github.com/jayasurya2701/WebScrapeX-Automated-Google-Search-Result-Extractor-"],
        "IPL-Analytics Dashboard using PowerBI": ["AI-powered task management assistant with voice command support.", "https://github.com/jayasurya2701/IPL-Analytics-Dashboard-using-PowerBI"]
    }
    for title, (desc, link) in projects.items():
        st.subheader(f"🎯 {title}")
        st.write(desc)
        st.markdown(f"🔗 [View on GitHub]({link})", unsafe_allow_html=True)

elif page == "📞 Contact":
    st.header("📞 Contact Me")
    st.write("📧 Email: [suryapazhani27@gmail.com](mailto:suryapazhani27@gmail.com)")
    st.write("📞 Mobile: [+91 7604805128](tel:+917604805128)")
    st.write("🔗 LinkedIn: [linkedin.com/in/jayasuryaps](https://www.linkedin.com/in/jayasuryaps)")
    st.write("🐙 GitHub: [github.com/jayasuryaps](https://github.com/jayasuryaps)")
    
    st.markdown("""
    <div style="text-align: center;">
        <a href="mailto:suryapazhani27@gmail.com" class="button">📩 Send an Email</a>
    </div>
    """, unsafe_allow_html=True)
