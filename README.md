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

## Projects

### Generative AI & Agentic Systems

<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Details</th>
      <th>Repository Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b>RAG Tax Advisory System for International Students</b><br/>
        <sub>Python · LangChain · ChromaDB · Elasticsearch · BM25 · PyMuPDF · sentence-transformers · LLaMA · Google Gemini</sub>
      </td>
      <td>RAG-based chatbot answering U.S. tax questions for international students, grounded in 41 real IRS documents (publications, forms, tax treaties, university guides) extracted page-by-page with PyMuPDF and split into 2,247 chunks. Hybrid retrieval (vector search + BM25 via Reciprocal Rank Fusion) boosted hit rate from 70% to 100%. Dual safety guards, personalized answers conditioned on 7 student profile attributes, and a 5-metric evaluation framework achieving a final LLM-as-a-Judge score of 0.770.</td>
      <td><a href="https://github.com/aneessaheba/RAG-Tax-Advisory-System-for-Intl-Students">GitHub</a> · <a href="https://rag-tax-advisory-system-for-students.onrender.com/">Live</a></td>
    </tr>
    <tr>
      <td>
        <b>Multi-Agent Blog System</b><br/>
        <sub>Ollama · Docker · AWS ECS · HTML/CSS/JS</sub>
      </td>
      <td>Multi-agent workflow using Ollama LLMs (Planner, Reviewer, Finalizer) for automated blog content creation. Web front-end for blog submission with HTML, CSS, and JavaScript. Deployed on Docker + AWS ECS integrating lightweight local LLMs (smollm:1.7b, Phi3:mini). Automated outputs include tags, summaries, and a publishable content package.</td>
      <td><a href="https://github.com/aneessaheba/ollama-agentic-ai">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>AI Memory Chatbot Agent</b><br/>
        <sub>FastAPI · MongoDB · Google Gemini · Motor</sub>
      </td>
      <td>Intelligent chatbot with multi-tiered memory architecture: short-term conversational memory, session-based summaries, lifetime user context condensation, and episodic memory retrieval with vector embeddings. Automatic memory consolidation, importance-weighted fact extraction, and context-aware responses using Google Generative AI.</td>
      <td><a href="https://github.com/aneessaheba/Chat-agentic-ai">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Bike-Share Pass Optimizer</b><br/>
        <sub>ReAct · MRKL · DuckDB · Express</sub>
      </td>
      <td>Single-agent ReAct + MRKL workflow analyzing Divvy bike-share trip data to recommend membership vs pay-per-ride pricing. Custom tools (CSV SQL via DuckDB, policy retrieval with web scraping, calculator) with transparent Thought → Action → Observation traces and policy citations for decision justification.</td>
      <td><a href="https://github.com/aneessaheba/auth-route-and-bike-share-analysis">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Career Counseling Agent</b><br/>
        <sub>Streamlit · Gemini · LangChain</sub>
      </td>
      <td>AI-powered career planning assistant with Skills Gap Analyzer, Resume Scorer with improvement suggestions (0–10 scale), Salary Estimator, and Interview Question Generator for personalized career guidance.</td>
      <td><a href="https://github.com/aneessaheba/streamlit-career-agent-gemini">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Airbnb Prototype with Agentic AI</b><br/>
        <sub>LangChain · FastAPI · React · MySQL</sub>
      </td>
      <td>Full-stack Airbnb-style platform with property listings, bookings, and secure authentication. Agentic AI Concierge using LangChain to generate personalized travel plans and recommendations. LLM-driven workflows integrated with backend APIs for context-aware, goal-oriented user interactions.</td>
      <td><a href="https://github.com/aneessaheba/airbnb-agentic-ai">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Data Engineering & Analytics

<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Details</th>
      <th>Repository Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b>Stock Data ETL & Data Warehouse Pipeline</b><br/>
        <sub>PostgreSQL · Docker · ETL · Dimensional Modeling · Apache Airflow · Kafka · TimescaleDB</sub>
      </td>
      <td>ETL pipeline for stock market data integrating multiple sources and automating ingestion across 50,567 records with 9 daily Airflow DAGs. Star-schema dimensional data warehouse in TimescaleDB for structured financial analysis. Dockerized workflows for reproducible deployments. 13 analytics visualizations in Tableau and Apache Superset covering YoY trends, volatility analysis, ROE rankings, and correlation heatmaps.</td>
      <td><a href="https://github.com/aneessaheba/stock-data-etl-warehouse-pipelinee">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Real-Time Flight Delay Prediction Pipeline</b><br/>
        <sub>Apache Kafka · Apache Spark · PySpark · HDFS · Apache Airflow · Docker</sub>
      </td>
      <td>End-to-end big data ML pipeline ingesting 19M+ flight records into HDFS, training GBT and Logistic Regression classifiers with Spark MLlib (3-fold CrossValidator), achieving AUC-ROC 0.94 and F1 0.90. Real-time streaming inference with Kafka + Spark Structured Streaming at 11,648 events/sec (23× above target). Serialized PipelineModels to HDFS eliminating training/serving feature skew across batch and streaming paths.</td>
      <td><a href="https://github.com/aneessaheba/realtime-flight-delay-predictor-bigdata">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Comprehensive Public Health Analytics Dashboard</b><br/>
        <sub>Python · SQL · Tableau · Pandas · CDC Socrata API</sub>
      </td>
      <td>Multi-source pipeline aggregating CDC PLACES, CDC BRFSS, SAMHSA, and WHO data across 721 US counties. Statistical analysis identifying a significant obesity–diabetes correlation (Pearson r=0.79, R²=0.63, p=1.56e-137) across 630 counties. Tableau dashboards with county-level choropleth maps, regional bar charts, and scatter analytics for non-technical stakeholders.</td>
      <td><a href="https://github.com/aneessaheba/Comprehensive-Public-Health-Analytics-Dashboard">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Spotify Data Analysis</b><br/>
        <sub>AWS Glue · Snowflake · Power BI</sub>
      </td>
      <td>ETL pipeline with Spotify API, AWS Glue, and Snowflake. Interactive Power BI dashboards delivering insights on peak listening hours, weekend patterns, and top artists/tracks.</td>
      <td><a href="https://github.com/aneessaheba/Spotify-Data-Analysis">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Retail Orders Analytics Project</b><br/>
        <sub>Python · Pandas · SQL Server</sub>
      </td>
      <td>End-to-end data pipeline processing a retail orders dataset with Python and Pandas, loaded into SQL Server. Advanced analytics identifying top-performing products, regional sales patterns, monthly trends, and year-over-year growth metrics.</td>
      <td><a href="https://github.com/aneessaheba/Retail-Orders-Analytics-Project">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Machine Learning & Computer Vision

<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Details</th>
      <th>Repository Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b>EgoHomes: Egocentric Household Activity Dataset</b><br/>
        <sub>Python · MediaPipe · YOLOv8 · SAM 3 · Whisper · OpenCV · FFmpeg · MLX</sub>
      </td>
      <td>Fully automated multimodal annotation pipeline for egocentric household activity video, producing synchronized hand pose, segmentation masks, depth maps, and narration transcripts per frame for robotics foundation model pretraining. Integrates MediaPipe HandLandmarker (21-point hand skeleton), YOLOv8 pose estimation, SAM 3 for segmentation, and Whisper for narration. JSON frame-level annotation schemas with automated quality control. Targeting open release alongside a VLA research paper.</td>
      <td><a href="https://github.com/aneessaheba/Egocentric_Homes">GitHub</a> · <a href="https://egocentric-homes.vercel.app/">Live</a></td>
    </tr>
    <tr>
      <td>
        <b>4DX Movie Technology Using ML</b><br/>
        <sub>TensorFlow · CNN · Python · OpenCV · Audio Processing</sub>
      </td>
      <td>CNN-based system processing synchronized audio-visual streams to detect dynamic movie events in real-time and trigger physical theater effects (water, wind, seat motion) with millisecond-level precision for immersive 4DX experiences.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>
        <b>Face Mask Detection Using ML</b><br/>
        <sub>MobileNetV2 · OpenCV · TensorFlow · Python</sub>
      </td>
      <td>Real-time face mask detection using transfer learning with MobileNetV2, achieving 95%+ accuracy at 30+ FPS. OpenCV-based face detection with multi-face classification, optimized for edge deployment.</td>
      <td>—</td>
    </tr>
    <tr>
      <td>
        <b>Credit Card Fraud Detection</b><br/>
        <sub>PCA · Random Forest · Isolation Forest · Python · scikit-learn</sub>
      </td>
      <td>Anomaly detection pipeline for fraudulent transactions in highly imbalanced datasets using PCA dimensionality reduction and ensemble methods (Isolation Forest + Random Forest) with SMOTE oversampling and precision-recall optimization.</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

---

### Software Engineering & Data Structures

<table>
  <thead>
    <tr>
      <th>Project Name</th>
      <th>Details</th>
      <th>Repository Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b>CheckMyGrade OOP Python</b><br/>
        <sub>Python · OOP · CSV · Encryption</sub>
      </td>
      <td>Console-based student grade management using OOP and CSV persistence. CRUD, search, sort with timing analysis, data encryption, academic reports, and statistical analytics. Array and linked-list backends with role-based menus and comprehensive unit tests for performance validation.</td>
      <td><a href="https://github.com/aneessaheba/CheckMyGrade-OOP-Python">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Stock Analysis Application</b><br/>
        <sub>Python · OOP · GUI · SQLite</sub>
      </td>
      <td>Object-oriented stock tracking application with console and GUI interfaces. Embedded SQLite database for saving and retrieving stock data, historical price tracking from web APIs and CSV imports, profit/loss report generation, and interactive chart visualization.</td>
      <td><a href="https://github.com/aneessaheba/StockMarketAnalysis">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Distributed Kayak Travel Booking System</b><br/>
        <sub>FastAPI · Kafka · MySQL · MongoDB · Redis</sub>
      </td>
      <td>Distributed travel booking system supporting search, booking, billing, and analytics for flights, hotels, and cars. FastAPI microservices with Kafka and relational + NoSQL databases. AI-powered recommendation service for personalized travel deals and real-time updates with resilient, high-throughput infrastructure.</td>
      <td><a href="https://github.com/aneessaheba/kayak-travel-system">GitHub</a></td>
    </tr>
  </tbody>
</table>

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
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
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
![ElasticSearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat&logo=elasticsearch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat&logo=amazonaws&logoColor=white)
![AWS SageMaker](https://img.shields.io/badge/SageMaker-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/S3-569A31?style=flat&logo=amazons3&logoColor=white)
![Amazon EC2](https://img.shields.io/badge/EC2-FF9900?style=flat&logo=amazonec2&logoColor=white)
![AWS ECS](https://img.shields.io/badge/ECS-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)

### Data Engineering & Big Data

![Apache Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apacheairflow&logoColor=white)
![Apache Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=flat&logo=apachehadoop&logoColor=black)
![ETL](https://img.shields.io/badge/ETL-00897B?style=flat)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat&logo=snowflake&logoColor=white)
![AWS Glue](https://img.shields.io/badge/AWS_Glue-FF9900?style=flat&logo=amazonaws&logoColor=white)
![TimescaleDB](https://img.shields.io/badge/TimescaleDB-FDB515?style=flat)

### Data Analysis & Visualization

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Apache Superset](https://img.shields.io/badge/Apache_Superset-FF0000?style=flat)

### Tools & Development

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat&logo=jira&logoColor=white)

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
