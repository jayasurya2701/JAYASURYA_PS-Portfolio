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
    st.write("- **SQL** ")

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
    st.write("- **Web Scraping:** Beautiful Soup")

elif page == "🏢 Professional Experience":
    st.header("🏢 Professional Experience")

    st.subheader("AWS re/Start Technical Intern | Magic Bus India Foundation (Dec 2024 - Feb 2025)")
    st.write("- **Designed and implemented CI/CD pipelines** using **AWS CodePipeline, CodeBuild, and CodeDeploy**, improving deployment speed by **40%**.")
    st.write("- **Automated software deployment** with **EC2, S3, IAM, CloudWatch**, reducing manual effort and downtime.")

    st.subheader("AI Intern | Infosys Springboard (Nov 2024 - Jan 2025)")
    st.write("- **Implemented an AI-driven personalization system** leveraging **LLMs (OpenAI GPT,Meta Llama)** for real-time sentiment analysis, boosting guest satisfaction by **25%** through personalized service recommendations.")
    st.write("- **Enhanced data integration from mock CRM systems**, improving guest preference analysis accuracy by **30%** and speeding up service response times by **35%**.")

    st.subheader("AI Intern | Bridge Green Upcycle (June 2024 - Aug 2024)")
    st.write("- **Developed an intent based chatbot** for vendor communication using **Machine Learing, NLP**, boosting scrap battery collection by **15%**.")
    st.write("- **Optimized user interaction workflows**, improving response times and increasing vendor satisfaction by **20%**.")

    st.subheader("Public Policy Analyst | PhospheneAI (Feb 2024 - Jun 2024)")
    st.write("- **Performed data-driven policy research** using **WebScraping**, identifying trends across regulatory frameworks.")
    st.write("- **Provided data-driven insights**, leading to a **20% improvement** in stakeholder engagement.")

    st.subheader("Data Analyst | Redink Classroom (Aug 2023 - Oct 2023)")
    st.write("- **Conducted data wrangling and visualization** using **Power BI and SQL**, improving reporting efficiency by **50%**.")
    st.write("- **Designed interactive dashboards**, providing real-time insights for business decisions.")

elif page == "📄 Resume":
    st.header("📄 View & Download My Resume")

    # Google Drive File ID (Extract from your link)
    file_id = "10FblvaVGMYYP8NK6h1sCGNmbRFFll11D"

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
        "AutoPost-AI : An AI-Powered-LinkedIn-Post-Generator": ["AutoPost AI is an AI-driven LinkedIn post generator designed for professionals, marketers, and businesses to create engaging, high-quality LinkedIn content effortlessly.Built with Llama 3, LangChain, and Streamlit, this tool leverages LLM-powered content generation, few-shot learning, and metadata-based topic filtering to generate posts with precise tone, structure, and relevance.With Bi-language support, Personal Growth topics, post-purpose selection, and optimized API performance, AutoPost AI ensures that users can generate content faster, smarter, and more effectively.", "https://github.com/jayasurya2701/AutoPost-AI"],
        "Conversational CSV Chatbot using LLM API": ["Developed an AI-powered chatbot that enables users to interact with CSV datasets using natural language, making data retrieval 40% more efficient. Designed an intuitive UI with features like dynamic theme switching, real-time chat history, and adjustable response creativity, boosting user engagement by 35%. Integrated contextual conversation handling, improving response accuracy by 50%, making data analysis effortless and accessible.", "https://github.com/jayasurya2701/Conversational_CSV_Chatbot-using-LLM-"],
        "AI Driven Guest Experience for Personalization System for Hosipitality": ["The project aims to revolutionize guest experiences in the hospitality industry by leveraging advanced AI-powered systems. By harnessing LLMs such as OpenAI GPT and Meta LLaMA for NLP and Sentiment Analysis and integrating seamlessly with Mock CRM data via Google Sheets and User Emails, the system will analyze guest preferences, interpret feedback, and evaluate sentiment in real time. This approach will streamline customer interactions, enhance service personalization, and drive a measurable 25% improvement in customer satisfaction while boosting operational efficiency by 30%. .", "https://github.com/jayasurya2701/AI-Driven-Guest-Experience-for-Personalization-System-for-Hospitality"],
        "WebScrapeX: Automated Google Search Result Extractor": ["This Python project utilizes the Requests library and BeautifulSoup to efficiently scrape and retrieve up to 10 Google search results for a specified keyword, delivering relevant URLs. By simulating browser behavior with GET requests and parsing HTML content, it automates data extraction, significantly reducing manual effort and maximizing productivity in web scraping tasks. ", "https://github.com/jayasurya2701/WebScrapeX-Automated-Google-Search-Result-Extractor-"],
        "Intent Based Chatbot for Automated Queries": ["Engineered an advanced chatbot leveraging NLP and machine learning to analyze user intent, achieving a 25% reduction in average handling time and boosting customer satisfaction by 15% within three months. Automated common queries with over 75% response accuracy, minimizing human intervention in basic inquiries and enhancing user engagement streamlining vendor communication", "https://github.com/jayasurya2701/Intent-Based-Chatbot-for-Automated-Queries"],
        "Face Detection and Recognition Model using Python and OpenCV": ["Constructed an advanced facial recognition system with Python and OpenCV, achieving 95% accuracy in real-time tasks, improving system efficiency by 30%. Trained on a diverse dataset to refine performance and integrated facial recognition capabilities. ", "https://github.com/jayasurya2701/Face-Detection-and-Recognition-Model-using-Python-and-OpenCV"],
        "IPL-Analytics Dashboard using PowerBI": ["Designed a comprehensive IPL analytics dashboard using Microsoft Power BI, providing in-depth analysis of player performance, match statistics, and team dynamics. Leveraged data visualization and advanced analytics to derive actionable insights, enhancing strategic decision-making and driving team performance and operational efficiency by 20%.", "https://github.com/jayasurya2701/IPL-Analytics-Dashboard-using-PowerBI"]
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
