<h1 align="center">Hi, I'm Anees Saheba Guddi</h1>
<h3 align="center">Generative AI & LLMs | Distributed Systems | Data Engineering</h3>
<h4 align="center">MS in Applied Data Intelligence @ San José State University</h4>

<p align="center">
  <a href="mailto:aneessaheba.guddi@sjsu.edu">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/anees-saheba-guddi-215a97248/">
    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://aneessaheba.github.io">
    <img src="https://img.shields.io/badge/Portfolio-%2312100E.svg?style=for-the-badge&logo=Firefox&logoColor=white" alt="Portfolio" />
  </a>
  <a href="https://github.com/aneessaheba">
    <img src="https://img.shields.io/badge/GitHub-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.youtube.com/@BytAByte">
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="YouTube" />
  </a>
  <a href="https://leetcode.com/u/aneessaheba04/">
    <img src="https://img.shields.io/badge/LeetCode-FFA116.svg?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode" />
  </a>
  <a href="https://medium.com/@aneessaheba.guddi">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://public.tableau.com/app/profile/anees.saheba.guddi/vizzes">
    <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau" />
  </a>
</p>

---

## About Me

MS in Applied Data Intelligence student at **San José State University** (2025–2027) specializing in **Generative AI**, **LLM Fine-tuning**, and **Machine Learning Model Development**. I architect intelligent systems that combine cutting-edge AI capabilities with production-grade software engineering—from fine-tuning large language models and training deep learning networks to building agentic workflows and distributed architectures.

My expertise spans the full machine learning lifecycle: designing and training neural networks from scratch, fine-tuning foundation models for domain-specific tasks, architecting LLM-based agentic systems with LangChain and LangGraph, and deploying scalable microservices. With professional experience as a Software Development Engineer at HP Inc., I bring hands-on knowledge in building production AI systems, distributed data pipelines, and intelligent automation solutions.

**Background**
- Former Software Development Engineer at HP Inc. (Jul 2023 – Aug 2024)
- B.E. in Information Science and Engineering from Visvesvaraya Technological University (2019-2023)
- Based in San Jose, California | Originally from Bangalore, India

---

## Currently Working On

- Building production-ready agentic AI systems with LangChain, LangGraph, and multi-tool orchestration
- Exploring MLOps workflows, LLM fine-tuning techniques, and distributed machine learning training
- Deepening knowledge in scalable data platforms and real-time streaming architectures
- Contributing to open-source AI/ML projects and sharing insights through technical writing
- Creating educational content on Gen AI and Data Engineering on Medium and YouTube

---

## Featured Projects

### [RAG Tax Advisory System for International Students](https://github.com/aneessaheba/RAG-Tax-Advisory-System-for-Students)
**Tech Stack:** Python | ChromaDB | BM25 | PyMuPDF | sentence-transformers | Google Gemini

Built a RAG-based chatbot that answers U.S. tax questions for international students using 41 real IRS documents — publications, forms, tax treaties, and university guides — instead of model hallucinations. Extracted and cleaned text page-by-page using PyMuPDF, split into 2,247 chunks (500-word windows, 100-word overlap), and embedded each chunk into 384-dimensional vectors using `all-MiniLM-L6-v2` (local, free). Stored all chunks and vectors in ChromaDB.

Implemented a personalized intake flow collecting 7 student profile attributes at startup to ground every answer in the student's specific situation. Built hybrid retrieval combining vector similarity search and BM25 keyword search, merged via Reciprocal Rank Fusion (RRF) to surface the top 5 most relevant chunks — improving hit rate from 70% (vector-only) to 100%. Added dual safety guards: a keyword filter that instantly rejects off-topic questions, and a confidence threshold (≥0.70 vector score) before invoking the LLM. Integrated Gemini 2.0 Flash for generation with a raw-chunk extractive fallback if the API is unavailable.

Built a full evaluation framework (`evaluate.py`) across 5 metrics — Context Relevance, Hit Rate, Answer Relevance, Faithfulness, and an LLM-as-a-Judge (second Gemini call scoring correctness, completeness, and groundedness 0–1) — iterating from v1 to v3 with a final Judge score of 0.770. Tracks per-query latency and token estimates, logs all stats to `query_log.jsonl`, and collects y/n user feedback to `feedback_log.jsonl` after every answer.

---

### [Distributed Kayak Travel Booking System](https://github.com/aneessaheba/kayak-distributed-system)
**Tech Stack:** FastAPI | Kafka | MySQL | MongoDB | Redis

Built a distributed travel booking system inspired by Kayak supporting search, booking, billing, and analytics for flights, hotels, and cars. Designed backend microservices using FastAPI, Kafka, and relational + NoSQL databases. Developed an AI-powered recommendation service for personalized travel deals and real-time updates. Implemented scalable infrastructure and service communication for resilient, high-throughput operations.

---

### [Airbnb Prototype with Agentic AI](https://github.com/aneessaheba/airbnb-agentic-ai)
**Tech Stack:** LangChain | FastAPI | React | MySQL

Built a full-stack Airbnb-style platform with property listings, bookings, and secure authentication. Designed an Agentic AI Concierge using LangChain to generate personalized travel plans and recommendations. Integrated LLM-driven workflows with backend APIs for context-aware, goal-oriented user interactions.

---

## Professional Experience

### Hewlett Packard (HP) | Bengaluru, India
**Software Development Engineer** | Jul 2023 – Aug 2024

- Implemented rule-based chatbots for Printer Customer Support to guide users through common troubleshooting
- Prepared and organized data from customer support transcripts and internal troubleshooting documents
- Performed basic text cleaning and keyword extraction to map user queries to predefined intents
- Built decision-based conversation flows using simple rules, conditional logic, and fallback responses
- Integrated chatbot logic with backend support APIs to fetch device status and recommended actions
- Conducted limited exploration with early LLM tools to assess potential improvements in response quality and coverage

### Pheuna Technology | Bengaluru, India
**Software Engineer Intern** | May 2022 – Aug 2022

- Designed RESTful APIs using Node.js and Express with Sequelize ORM for real-time event-driven systems
- Implemented Kafka producers and consumers for distributed message processing
- Built a cross-platform mobile dashboard using React and Ionic for real-time monitoring

---

## Technical Skills

### Generative AI & LLMs

![Gen AI APIs](https://img.shields.io/badge/Gen_AI_APIs-4A90E2?style=flat)
![Prompt Engineering](https://img.shields.io/badge/Prompt_Engineering-00C853?style=flat)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=flat&logo=langchain)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat)
![Tool Calling](https://img.shields.io/badge/Tool_Calling-FF6B6B?style=flat)
![RAG](https://img.shields.io/badge/RAG-4A90E2?style=flat)
![Vector Databases](https://img.shields.io/badge/Vector_DBs-FF6B6B?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai)
![Google Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat&logo=google)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21F?style=flat&logo=huggingface&logoColor=black)
![Fine-tuning](https://img.shields.io/badge/Fine--tuning-FF5722?style=flat)
![LoRA](https://img.shields.io/badge/LoRA-9C27B0?style=flat)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat)

### Machine Learning & Deep Learning

![Model Training](https://img.shields.io/badge/Model_Training-E91E63?style=flat)
![Supervised Learning](https://img.shields.io/badge/Supervised_Learning-0088CC?style=flat)
![Unsupervised Learning](https://img.shields.io/badge/Unsupervised_Learning-6A1B9A?style=flat)
![Neural Networks](https://img.shields.io/badge/Neural_Networks-0088CC?style=flat)
![CNN](https://img.shields.io/badge/CNN-00BCD4?style=flat)
![RNN](https://img.shields.io/badge/RNN-009688?style=flat)
![Transfer Learning](https://img.shields.io/badge/Transfer_Learning-673AB7?style=flat)
![Feature Engineering](https://img.shields.io/badge/Feature_Engineering-6A1B9A?style=flat)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat&logo=keras&logoColor=white)

### Programming & Frameworks

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat&logo=express&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

### Data & Cloud Systems

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat&logo=duckdb&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonaws&logoColor=white)
![AWS SageMaker](https://img.shields.io/badge/SageMaker-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/S3-569A31?style=flat&logo=amazons3&logoColor=white)
![Amazon EC2](https://img.shields.io/badge/EC2-FF9900?style=flat&logo=amazonec2&logoColor=white)
![AWS ECS](https://img.shields.io/badge/ECS-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=white)

### Data Engineering & Big Data

![Apache Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apacheairflow&logoColor=white)
![Apache Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=flat&logo=apachehadoop&logoColor=black)
![ETL](https://img.shields.io/badge/ETL-00897B?style=flat)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white)
![AWS Glue](https://img.shields.io/badge/AWS_Glue-FF9900?style=flat&logo=amazonaws&logoColor=white)

### Data Analysis & Visualization

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)

### Tools & Development

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat&logo=jira&logoColor=white)

---

## Additional Projects

### Generative AI & Agentic Systems

#### [Multi-Agent Blog System](https://github.com/aneessaheba/ollama-agentic-ai)
**Tech Stack:** Ollama | Docker | AWS ECS | HTML/CSS/JS

Built a multi-agent workflow using Ollama LLMs (Planner, Reviewer, Finalizer) for automated blog content creation. Developed a web front-end for blog submission with HTML, CSS, and JavaScript, including JSON handling. Deployed using Docker containers and AWS ECS, integrating lightweight local LLMs ('smollm:1.7b', 'Phi3:mini'). Generated automated outputs including tags, summaries, and a publishable content package.

#### [RAG Tax Advisory System for International Students](https://github.com/aneessaheba/RAG-Tax-Advisory-System-for-Students)
**Tech Stack:** Python | ChromaDB | BM25 | PyMuPDF | sentence-transformers | Google Gemini

Built a RAG-based chatbot that answers U.S. tax questions for international students using 41 real IRS documents — publications, forms, tax treaties, and university guides — instead of model hallucinations. Extracted and cleaned text page-by-page using PyMuPDF, split into 2,247 chunks (500-word windows, 100-word overlap), and embedded each chunk into 384-dimensional vectors using `all-MiniLM-L6-v2` (local, free). Stored all chunks and vectors in ChromaDB.

Implemented a personalized intake flow collecting 7 student profile attributes at startup to ground every answer in the student's specific situation. Built hybrid retrieval combining vector similarity search and BM25 keyword search, merged via Reciprocal Rank Fusion (RRF) to surface the top 5 most relevant chunks — improving hit rate from 70% (vector-only) to 100%. Added dual safety guards: a keyword filter that instantly rejects off-topic questions, and a confidence threshold (≥0.70 vector score) before invoking the LLM. Integrated Gemini 2.0 Flash for generation with a raw-chunk extractive fallback if the API is unavailable.

Built a full evaluation framework (`evaluate.py`) across 5 metrics — Context Relevance, Hit Rate, Answer Relevance, Faithfulness, and an LLM-as-a-Judge (second Gemini call scoring correctness, completeness, and groundedness 0–1) — iterating from v1 to v3 with a final Judge score of 0.770. Tracks per-query latency and token estimates, logs all stats to `query_log.jsonl`, and collects y/n user feedback to `feedback_log.jsonl` after every answer.

---

#### [AI Memory Chatbot Agent](https://github.com/aneessaheba/Chat-agentic-ai)
**Tech Stack:** FastAPI | MongoDB | Google Gemini | Motor

Built an intelligent chatbot with multi-tiered memory architecture using FastAPI and MongoDB. Implements short-term conversational memory, session-based summaries, lifetime user context condensation, and episodic memory retrieval with vector embeddings. Features automatic memory consolidation, importance-weighted fact extraction, and context-aware responses using Google Generative AI.

#### [Bike-Share Pass Optimizer](https://github.com/aneessaheba/auth-route-and-bike-share-analysis)
**Tech Stack:** ReAct | MRKL | DuckDB | Express

Built a single-agent ReAct + MRKL workflow that analyzes Divvy bike-share trip data to recommend whether riders should purchase a membership or stay on pay-per-ride pricing. Implements custom tools (CSV SQL via DuckDB, policy retrieval with web scraping, calculator) with transparent Thought → Action → Observation traces and policy citations for decision justification.

#### [Career Counseling Agent](https://github.com/aneessaheba/streamlit-career-agent-gemini)
**Tech Stack:** Streamlit | Gemini | LangChain

Developed an AI-powered career planning assistant using Gemini LLM and custom tools. Features include Skills Gap Analyzer, Resume Scorer with improvement suggestions (0-10 scale), Salary Estimator, and Interview Question Generator for personalized career guidance.

---

### Data Engineering & Analytics

#### [Stock Data ETL & Data Warehouse Pipeline](https://github.com/aneessaheba/StockMarketETL)
**Tech Stack:** PostgreSQL | Docker | ETL | Dimensional Modeling

Built an ETL pipeline for stock market data using Python, integrating multiple sources and automating data ingestion. Designed a dimensional data warehouse in PostgreSQL for structured financial analysis and reporting. Implemented Dockerized workflows for reproducible deployments and efficient environment management. Developed analytics dashboards and SQL queries for stock trends, financial KPIs, and company-level insights.

#### [Spotify Data Analysis](https://github.com/aneessaheba/Spotify-Data-Analysis)
**Tech Stack:** AWS Glue | Snowflake | Power BI

Built an ETL pipeline with Spotify API, AWS Glue, and Snowflake. Created interactive Power BI dashboards delivering insights on peak hours, weekend listening patterns, and top artists/tracks.

#### [Retail Orders Analytics Project](https://github.com/aneessaheba/Retail-Orders-Analytics-Project)
**Tech Stack:** Python | Pandas | SQL Server

Built an end-to-end data pipeline using Python and Pandas to process retail orders dataset. Loaded cleaned data into SQL Server and performed advanced analytics to identify top-performing products, regional sales patterns, monthly trends, and year-over-year growth metrics.

---

### Software Engineering & Data Structures

#### [CheckMyGrade-OOP-Python](https://github.com/aneessaheba/CheckMyGrade-OOP-Python)
**Tech Stack:** Python | OOP | CSV | Encryption

Python console-based student grade management application using object-oriented programming principles and CSV data persistence. Supports CRUD operations, search, sort with timing analysis, data encryption, academic reports, and statistical analytics. Implements both array and linked list backends with role-based menus and comprehensive unit tests for performance validation.

#### [Stock Analysis Application](https://github.com/aneessaheba/StockMarketAnalysis)
**Tech Stack:** Python | OOP | GUI | SQLite

Object-oriented stock tracking application with both console and GUI interfaces built using Python. Features embedded database management for saving and retrieving stock data, historical price tracking from web APIs and CSV imports, profit/loss report generation, and interactive chart visualization using Python libraries.

---

### Machine Learning & Computer Vision

#### 4DX Movie Technology Using ML
**Tech Stack:** TensorFlow | CNN | Python | OpenCV | Audio Processing

Developed a CNN-based system that processes synchronized audio-visual streams to detect dynamic movie events in real-time and trigger corresponding physical theater effects (water, wind, seat motion) with millisecond-level precision for immersive 4DX experiences.

#### Face Mask Detection Using ML
**Tech Stack:** MobileNetV2 | OpenCV | TensorFlow | Python

Built a real-time face mask detection system using transfer learning with MobileNetV2, achieving 95%+ accuracy at 30+ FPS with OpenCV-based face detection and multi-face classification capabilities optimized for edge deployment.

#### Credit Card Fraud Detection
**Tech Stack:** PCA | Random Forest | Isolation Forest | Python | scikit-learn

Implemented an anomaly detection pipeline for identifying fraudulent transactions in highly imbalanced datasets using PCA dimensionality reduction and ensemble methods (Isolation Forest + Random Forest) with SMOTE oversampling and precision-recall optimization.

---

### Data Visualization

#### [Tableau Public Portfolio](https://public.tableau.com/app/profile/anees.saheba.guddi/vizzes)

Interactive dashboards for business intelligence, trend analysis, and KPI visualization showcasing storytelling with data.

---

## Education

**San José State University** | San Jose, CA  
*Master of Science in Applied Data Intelligence* | Jan 2025 – May 2027 | GPA: 3.5/4.0

**Relevant Coursework:** Gen AI LLMs, Agentic AI, Machine Learning, Deep Learning, Big Data Algorithms, Distributed Systems, Scalable Data Platforms

**Visvesvaraya Technological University** | Karnataka, India  
*Bachelor of Engineering in Information Science and Engineering* | Aug 2019 – Jun 2023 | GPA: 7.9/10.0

**Relevant Coursework:** Data Structures and Algorithms, Database Systems, Software Engineering

---

## GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=aneessaheba&show_icons=true&theme=radical&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub Stats" height="180"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=aneessaheba&layout=compact&theme=radical&hide_border=true&langs_count=10" alt="Top Languages" height="180"/>
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=aneessaheba&theme=radical&hide_border=true" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=aneessaheba&theme=radical&no-frame=true&no-bg=true&row=1&column=7" alt="GitHub Trophies" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=aneessaheba&theme=react-dark&hide_border=true&area=true" alt="Contribution Graph" />
</p>

## LeetCode Statistics

<p align="center">
  <img src="https://leetcard.jacoblin.cool/aneessaheba04?theme=dark&font=Ubuntu&ext=heatmap" alt="LeetCode Stats" />
</p>

---

## Connect With Me

<p align="center">
  <a href="mailto:aneessaheba.guddi@sjsu.edu">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/anees-saheba-guddi-215a97248/">
    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://aneessaheba.github.io">
    <img src="https://img.shields.io/badge/Portfolio-%2312100E.svg?style=for-the-badge&logo=Firefox&logoColor=white" alt="Portfolio" />
  </a>
  <a href="https://github.com/aneessaheba">
    <img src="https://img.shields.io/badge/GitHub-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.youtube.com/@BytAByte">
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="YouTube" />
  </a>
  <a href="https://leetcode.com/u/aneessaheba04/">
    <img src="https://img.shields.io/badge/LeetCode-FFA116.svg?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode" />
  </a>
  <a href="https://medium.com/@aneessaheba.guddi">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://public.tableau.com/app/profile/anees.saheba.guddi/vizzes">
    <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau" />
  </a>
</p>
