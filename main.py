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
    col1, col2, col3 = st.columns([6, 7, 3])  # Creates 3 columns (middle column is bigger)
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
    st.header("💡 Technical Skills")

    st.write("### 💻 Programming & Databases")
    st.write("- **Python:** NumPy, Pandas, Matplotlib, Scikit-Learn, Streamlit")
    st.write("- **SQL:** Query Optimization, Joins, Indexing")

    st.write("### 🤖 Machine Learning & AI")
    st.write("- **ML Algorithms:** Supervised & Unsupervised Learning")
    st.write("- **Large Language Models (LLMs), NLP**")
    st.write("- **Model Deployment:** Streamlit")

    st.write("### 📊 Data Visualization & Analytics")
    st.write("- **Microsoft Power BI**, **Google Looker Studio**, **Advanced Excel**")

    st.write("### ☁️ AWS Cloud Services")
    st.write("- **Compute & Storage:** EC2, S3, Lambda")
    st.write("- **Networking & Security:** IAM, VPC, Route53, ELB")
    st.write("- **Databases & Monitoring:** RDS, DynamoDB, CloudWatch")

    st.write("### 🛠️ Other Technical Skills")
    st.write("- **Web Scraping:** Beautiful Soup, Selenium")

elif page == "🏢 Professional Experience":
    st.header("🏢 Professional Experience")

    st.subheader("AWS re/Start Technical Intern | Magic Bus India Foundation (Dec 2024 - Feb 2025)")
    st.write("- **Designed and implemented CI/CD pipelines** using **AWS CodePipeline, CodeBuild, and CodeDeploy**, improving deployment speed by **40%**.")
    st.write("- **Automated software deployment** with **EC2, S3, IAM, CloudWatch**, reducing manual effort and downtime.")

    st.subheader("AI Intern | Infosys Springboard (Dec 2024 - Jan 2025)")
    st.write("- **Implemented an AI-driven personalization system** leveraging **LLMs (OpenAI GPT,Meta Llama)** for real-time sentiment analysis, boosting guest satisfaction by **25%** through personalized service recommendations.")
    st.write("- **Enhanced data integration from mock CRM systems**, improving guest preference analysis accuracy by **30%** and speeding up service response times by **35%**.")

    st.subheader("AI Intern | Bridge Green Upcycle (June 2024 - Aug 2024)")
    st.write("- **Developed an AI-powered chatbot** for vendor communication using **NLTK, Dialogflow**, boosting scrap battery collection by **15%**.")
    st.write("- **Optimized user interaction workflows**, improving response times and increasing vendor satisfaction by **20%**.")

    st.subheader("Public Policy Analyst | PhospheneAI (Feb 2024 - Jun 2024)")
    st.write("- **Performed NLP-based policy analysis** using **spaCy, NLTK, and Python**, identifying trends across regulatory frameworks.")
    st.write("- **Provided data-driven insights**, leading to a **20% improvement** in stakeholder engagement.")

    st.subheader("Data Analyst | Redink Classroom (Aug 2023 - Oct 2023)")
    st.write("- **Conducted data wrangling and visualization** using **Power BI, SQL, and Pandas**, improving reporting efficiency by **50%**.")
    st.write("- **Designed interactive dashboards**, providing real-time insights for business decisions.")

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
        "Conversational CSV Chatbot using LLM API": ["Developed an AI-powered chatbot that enables users to interact with CSV datasets using natural language, making data retrieval 40% more efficient. Designed an intuitive UI with features like dynamic theme switching, real-time chat history, and adjustable response creativity, boosting user engagement by 35%. Integrated contextual conversation handling, improving response accuracy by 50%, making data analysis effortless and accessible.", "https://github.com/jayasurya2701/Conversational_CSV_Chatbot-using-LLM-"],
        "AI-Driven-Guest-Experience-for-Personalization-System-for-Hosipitality": ["Designed an AI-powered system that personalizes guest experiences in the hospitality industry by analyzing customer preferences and feedback in real-time. Leveraged LLMs like OpenAI GPT and Meta LLaMA for NLP and sentiment analysis, integrating seamlessly with Google Sheets and mock CRM data via user emails. This solution streamlines customer interactions, enhances service personalization, and improves customer satisfaction by 25%, while increasing operational efficiency by 30%.", "https://github.com/jayasurya2701/AI-Driven-Guest-Experience-for-Personalization-System-for-Hospitality"],
        "Intent-Based-Chatbot-for-Automated-Queries": ["Developed an AI-powered chatbot that uses NLP and machine learning to accurately analyze user intent, reducing average query handling time by 25% and boosting customer satisfaction by 15% within three months. Automated responses for common queries with 75%+ accuracy, significantly minimizing the need for human intervention in basic inquiries. Enhanced user engagement and streamlined vendor communication, improving overall operational efficiency..", "https://github.com/jayasurya2701/Intent-Based-Chatbot-for-Automated-Queries"],
        "Face-Detection-and-Recognition-Model-using-Python-and-OpenCV": ["An AI chatbot that interacts with CSV datasets using LLaMA 3 and FAISS.", "https://github.com/jayasurya2701/Face-Detection-and-Recognition-Model-using-Python-and-OpenCV"],
        "WebScrapeX: Automated Google Search Result Extractor": ["Developed WebScrapeX, a Python-based tool that automates Google search result extraction. Utilized Requests and BeautifulSoup to scrape and retrieve the top 10 search results for any keyword, significantly reducing manual effort in web research. By simulating browser behavior with GET requests and HTML parsing, this tool maximizes productivity, making data extraction faster, efficient, and hassle-free.", "https://github.com/jayasurya2701/WebScrapeX-Automated-Google-Search-Result-Extractor-"],
        "IPL-Analytics Dashboard using PowerBI": [" Designed a comprehensive IPL analytics dashboard using Microsoft Power BI, providing in-depth analysis of player performance, match statistics, and team dynamics. Leveraged data visualization and advanced analytics to derive actionable insights, enhancing strategic decision-making and driving team performance and operational efficiency by 20%. .", "https://github.com/jayasurya2701/IPL-Analytics-Dashboard-using-PowerBI"]
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
