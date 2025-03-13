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
page = st.sidebar.radio("Go to", ["🏠 Home", "💡 Skills", "🏢 Professional Experience", "🚀 Projects", "📄 Resume", "📞 Contact"])

if page == "🏠 Home":
    # Centering Image in Streamlit
    col1, col2, col3 = st.columns([5, 7, 3])  # Creates 3 columns (middle column is bigger)
    with col2:  
        st.image("profile.jpg", width=200, )  # Image in the center

    # Centering the title and subheader
    st.markdown("<h1 style='text-align: center;'>JAYASURYA PS</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>AI & Cloud Visionary | B.Tech - AI & Data Science | AWS Certified | Innovation Seeker & Problem-Solver</h3>", unsafe_allow_html=True)

    # About section with better formatting
    st.write("""
    🔍 **Passionate about solving real-world problems** with intelligent systems, automation, and scalable cloud solutions.

    ✨ **Always learning, experimenting, and pushing boundaries** to create meaningful impact.

    📌 **Strengths:** AI & ML | Cloud Computing | Data Science | Problem-Solving | Innovation

    📩 **Open to collaborations and exciting opportunities**—let’s connect!
    """)



elif page == "💡 Skills":
    st.header("💡Technical Skills")

    st.write("### 💻 Programming Languages & Databases")
    st.write("- **Python:** NumPy, Pandas, Matplotlib, Scikit-Learn")
    st.write("- **SQL**")

    st.write("### 🤖 Machine Learning & AI")
    st.write("- ML Algorithms, LLMs")

    st.write("### 📊 Data Visualization Tools")
    st.write("- **Advanced Excel**,  **Microsoft Power BI**,  **Google Looker Studio**")

    st.write("### ☁️ AWS Cloud Services")
    st.write("- **EC2**, **S3**, **IAM**, **Route53**")
    st.write("- **RDS**, **VPC**, **CloudWatch**, **DynamoDB**, **Lambda**, **ELB**")

    st.write("### 🛠️ Other Technical Skills")
    st.write("- **Web Scraping:** Beautiful Soup")
    st.write("- **Networking (Basics)**")

elif page == "🏢 Professional Experience":
    st.header("🏢 Professional Experience")

    st.subheader("AWS re/Start Technical Internship | Magic Bus India Foundation (Dec 2024 - Feb 2025)")
    st.write("🚀 Designed and implemented CI/CD pipelines using AWS services, improving deployment speed by **40%**.")
    st.write("⚡ Automated software deployment with **EC2, S3, CodeDeploy, and CloudWatch**, reducing manual effort and downtime.")

    st.subheader("🤖 AI Intern | Infosys Springboard (Dec 2024 - Jan 2025)")
    st.write("📊 Developed machine learning models to analyze customer behavior, achieving a **20%** improvement in predictive accuracy.")
    st.write("⚙️ Automated data preprocessing pipelines using **Python and SQL**, reducing data preparation time by **35%**.")

    st.subheader("🤝 AI Intern | Bridge Green Upcycle (June 2024 - August 2024)")
    st.write("💬 Developed a chatbot using AI for vendor communication, boosting scrap battery collection by **15%**.")
    st.write("⚡ Optimized user interaction workflows, improving response times and increasing vendor satisfaction by **20%**.")

    st.subheader("📑 Public Policy Analyst | PhospheneAI (Feb 2024 - Jun 2024)")
    st.write("📊 Performed data-driven policy research using **NLP**, analyzing trends across legislative frameworks.")
    st.write("🌍 Delivered insights that enhanced stakeholder engagement by **20%**.")

    st.subheader("📊 Data Analyst | Redink Classroom (Aug 2023 - Oct 2023)")
    st.write("📈 Conducted data wrangling and visualization using **Power BI and SQL**, increasing reporting efficiency by **50%**.")

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
    #st.write("🐙 GitHub: [github.com/jayasurya2701](https://github.com/jayasurya2701?tab=repositories)")
    
    st.markdown("""
    <div style="text-align: center;">
        <a href="mailto:suryapazhani27@gmail.com" class="button">📩 Send an Email</a>
    </div>
    """, unsafe_allow_html=True)
