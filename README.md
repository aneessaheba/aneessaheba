<h1 align="center">Hi, I'm Anees</h1>
<h3 align="center">LLMs & Agentic AI · Deep Learning · Data Engineering</h3>
<p align="center">MS in Applied Data Intelligence @ San José State University · San Jose, CA</p>

<p align="center">
  <a href="mailto:aneessaheba.guddi@sjsu.edu"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://www.linkedin.com/in/anees-saheba-guddi-215a97248/"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://aneessaheba.github.io"><img src="https://img.shields.io/badge/Portfolio-%2312100E.svg?style=for-the-badge&logo=Firefox&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.youtube.com/@BytAByte"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="YouTube" /></a>
  <a href="https://medium.com/@aneessaheba.guddi"><img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" /></a>
  <a href="https://leetcode.com/u/aneessaheba04/"><img src="https://img.shields.io/badge/LeetCode-FFA116.svg?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode" /></a>
  <a href="https://public.tableau.com/app/profile/anees.saheba.guddi/vizzes"><img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau" /></a>
</p>

<p align="center">
  <a href="#about-me">About</a> ·
  <a href="#all-projects">All Projects</a> ·
  <a href="#experience">Experience</a> ·
  <a href="#technical-skills">Skills</a> ·
  <a href="#education">Education</a>
</p>

## About Me

I'm an MS student in Applied Data Intelligence at **San José State University** (graduating May 2027), focused on **large language models, agentic AI and deep learning**.

My recent work spans the LLM stack: making long-context inference cheaper through KV-cache compression, building tool-using agents that fix real GitHub issues, and training Transformers, Vision Transformers, LSTMs and GANs from scratch in PyTorch. I care about careful evaluation: fair baselines, held-out test sets, controlled ablations, and honest write-ups of what didn't work.

I also build the systems around the models, including RAG pipelines, Kafka and Spark streaming pipelines, data warehouses and microservices. Before grad school I spent a year as a Software Development Engineer at **HP**, building customer-support chatbots.

**Open to:** ML / GenAI Engineer roles starting 2027

## All Projects

### Large Language Models (LLMs)

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>KV-Cache Compression for Long-Context LLM Inference</b><br/><sub>Python · PyTorch · Hugging Face Transformers · NVIDIA kvpress · CUDA · Llama-3.1-8B / Llama-3.2-3B · LongBench · RULER · NVIDIA RTX 5090</sub></td>
    <td>Researched and benchmarked KV-cache compression techniques for long-context LLM inference on Llama-3.1-8B. Surveyed and selected methods across three families: token eviction (StreamingLLM, SnapKV, PyramidKV, H2O, AdaKV, KVzip), low-bit quantization (KIVI, TurboQuant) and learned autoencoder compression (KV-CAR). Designed a shared evaluation framework that compares every method at the same measured memory budget (50%, 25% and 12.5% of full KV memory) on LongBench, Needle-in-a-Haystack and RULER. Studied whether combining eviction and quantization makes errors compound. Profiled GPU memory, latency and concurrent-session capacity on an NVIDIA RTX 5090.</td>
    <td><a href="https://github.com/aneessaheba/298a-kv-cache-compression">GitHub</a></td>
  </tr>
</table>

### Agentic AI

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Gemma 4 Developer Agent</b><br/><sub>Python · Gemma 4 · Hugging Face Transformers · PEFT / LoRA · PyTorch · vLLM · ReAct-style Tool Calling · Git / Unified Diffs · pytest · Docker · Kaggle · Weights & Biases</sub><br/><sub><i>Also: LLM Fine-Tuning</i></sub></td>
    <td>Autonomous coding agent built on Google's Gemma 4 for the Kaggle Gemma 4 Developer Agent competition. Given a real GitHub repository and an issue report, the agent explores the codebase, finds the faulty code, reasons about a fix, and generates a patch that passes the repository's validation tests. Evolved from a single-shot prompting baseline into a multi-step, tool-using agent with file search, code navigation, test execution and self-correction loops, plus LoRA fine-tuning on issue-to-patch data. Controlled experiments compared prompting strategies, tool sets and adapter settings, backed by a full experiment log, error analysis and a write-up of approaches that didn't work.</td>
    <td><a href="https://github.com/aneessaheba/autonomous-software-engineering-agent-gemma4">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Multi-Agent Blog System</b><br/><sub>Ollama · Docker · AWS ECS · HTML/CSS/JS</sub></td>
    <td>Multi-agent workflow using Ollama LLMs (Planner, Reviewer, Finalizer) for automated blog content creation. Web front-end for blog submission. Deployed on Docker + AWS ECS with lightweight local LLMs (smollm:1.7b, Phi3:mini). Outputs include tags, summaries and a publishable content package.</td>
    <td><a href="https://github.com/aneessaheba/ollama-agentic-ai">GitHub</a></td>
  </tr>
  <tr>
    <td><b>AI Memory Chatbot Agent</b><br/><sub>FastAPI · MongoDB · Google Gemini · Motor</sub></td>
    <td>Chatbot with a multi-tiered memory architecture: short-term conversational memory, session summaries, lifetime user context condensation, and episodic memory retrieval with vector embeddings. Automatic memory consolidation and importance-weighted fact extraction.</td>
    <td><a href="https://github.com/aneessaheba/Chat-agentic-ai">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Bike-Share Pass Optimizer</b><br/><sub>ReAct · MRKL · DuckDB · Express</sub></td>
    <td>Single-agent ReAct + MRKL workflow analyzing Divvy bike-share trip data to recommend membership vs pay-per-ride pricing. Custom tools (CSV SQL via DuckDB, policy retrieval with web scraping, calculator) with transparent Thought → Action → Observation traces and policy citations.</td>
    <td><a href="https://github.com/aneessaheba/auth-route-and-bike-share-analysis">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Career Counseling Agent</b><br/><sub>Streamlit · Gemini · LangChain</sub></td>
    <td>Career planning assistant with a Skills Gap Analyzer, Resume Scorer with improvement suggestions (0–10 scale), Salary Estimator and Interview Question Generator.</td>
    <td><a href="https://github.com/aneessaheba/streamlit-career-agent-gemini">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Airbnb Prototype with Agentic AI</b><br/><sub>LangChain · FastAPI · React · MySQL</sub></td>
    <td>Full-stack Airbnb-style platform with listings, bookings and secure authentication. A LangChain AI concierge generates personalized travel plans, integrated with backend APIs for context-aware interactions.</td>
    <td><a href="https://github.com/aneessaheba/airbnb-agentic-ai">GitHub</a></td>
  </tr>
</table>

### Retrieval-Augmented Generation (RAG)

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>RAG Tax Advisory System for International Students</b><br/><sub>Python · LangChain · ChromaDB · Elasticsearch · BM25 · PyMuPDF · sentence-transformers · LLaMA · Google Gemini</sub></td>
    <td>RAG-based chatbot answering U.S. tax questions for international students, grounded in 41 real IRS documents (publications, forms, tax treaties, university guides) extracted page-by-page with PyMuPDF and split into 2,247 chunks. Hybrid retrieval (vector search + BM25 via Reciprocal Rank Fusion) boosted hit rate from 70% to 100%. Dual safety guards, personalized answers conditioned on 7 student profile attributes, and a 5-metric evaluation framework achieving a final LLM-as-a-Judge score of 0.770.</td>
    <td><a href="https://github.com/aneessaheba/RAG-Tax-Advisory-System-for-Intl-Students">GitHub</a><br/><a href="https://rag-tax-advisory-system-for-students.onrender.com/">Live</a></td>
  </tr>
</table>

### Reinforcement Learning

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Pokémon TCG AI Battle Challenge</b><br/><sub>Python · PyTorch · Kaggle PTCG Simulator SDK · Gymnasium · PPO / Self-Play RL (Stable-Baselines3) · Monte Carlo Tree Search · NumPy · pandas · Matplotlib</sub><br/><sub><i>Domain: Game AI</i></sub></td>
    <td>Autonomous agent that plays competitive Pokémon Trading Card Game matches, built for the Kaggle PTCG AI Battle Challenge. Decides under hidden information (unknown opponent hands and decks), plans several turns ahead and adapts to different opponent strategies. Progressed from a rule-based heuristic baseline to Monte Carlo Tree Search with determinization, then to a PPO-trained policy/value network trained through self-play in the official simulator. Strategies compared through local round-robin tournaments and the Kaggle ladder, with full experiment tracking and analysis of failed strategies.</td>
    <td><a href="https://github.com/aneessaheba/pokemon-tcg-ai-battle-agent-rl">GitHub</a></td>
  </tr>
</table>

### Natural Language Processing (NLP)

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Character-Level GPT Language Model</b><br/><sub>Python · PyTorch · CUDA · Hugging Face Datasets · NumPy · Matplotlib</sub><br/><sub><i>Built from scratch · Also: LLMs</i></sub></td>
    <td>Decoder-only Transformer built from scratch that predicts the next character of a story, trained on TinyStories. Multi-head self-attention, causal masking, feedforward blocks and positional embeddings are written with plain tensor operations, without <code>nn.Transformer</code>, <code>nn.MultiheadAttention</code> or PyTorch's built-in attention. 4 blocks, width 256, 4 heads, 128-character context, 3.2M parameters. Reached 1.0875 validation bits per character and 76.1% top-1 next-character accuracy.</td>
    <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task1_llm/anees_saheba">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Yelp Review Sentiment Classification</b><br/><sub>Python · PyTorch · LSTM · Attention · scikit-learn · pandas</sub><br/><sub><i>Built from scratch</i></sub></td>
    <td>Three binary sentiment classifiers trained from scratch on 504K Yelp Polarity reviews, with no pretrained embeddings or language models. All three share the same vocabulary, preprocessing and training loop and differ only in how a review becomes a single vector (max pooling baseline, 2-layer LSTM, learned attention pooling). Preprocessing keeps negation words so "not good" is never read as "good". Best model (LSTM) reached 95.02% test accuracy and 0.950 macro F1.</td>
    <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task2_sentiment/anees_saheba">GitHub</a></td>
  </tr>
</table>

### Computer Vision

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>PatchVision: Vision Transformer from Scratch</b><br/><sub>Python · PyTorch · torchvision · NumPy · pandas · scikit-learn · Matplotlib · Seaborn · CUDA</sub><br/><sub><i>Built from scratch</i></sub></td>
    <td>Vision Transformer built from first principles and trained from scratch, with no pretraining, to classify 200 visually similar bird species in CUB-200-2011 (11,788 images), testing whether a compact ViT can compete with a CNN when data is limited. Implemented patch embedding (224×224 → 196 tokens), a learnable class token, positional embeddings, 6 encoder blocks with multi-head self-attention and a 200-class head. Compared against a CNN baseline under the same split, augmentation, budget and protocol. Controlled ablations over patch size (8×8 vs 16×16), depth (2/4/6 blocks) and regularization, with best configs repeated over 3 seeds (mean ± std). Interpreted with confusion matrices, per-class error analysis and attention maps.</td>
    <td><a href="https://github.com/aneessaheba/PatchVision-ViT-from-Scratch-for-Bird-Classification">GitHub</a></td>
  </tr>
  <tr>
    <td><b>CycleGAN Photo-to-Monet Style Transfer</b><br/><sub>Python · PyTorch · CycleGAN · PatchGAN · SciPy · Pillow · Kaggle</sub><br/><sub><i>Built from scratch</i></sub></td>
    <td>CycleGAN trained from scratch to translate between photographs and Monet paintings in both directions using unpaired data. Two ResNet generators (6 residual blocks, 12.2M parameters), two PatchGAN discriminators, least-squares adversarial loss and cycle-consistency loss. Scored with FID and KID, entered in a Kaggle evaluation, and backed by a 30-sample human audit. FID 86.59, KID 0.0075, Kaggle score -52.84.</td>
    <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task3_gan/anees_saheba">GitHub</a></td>
  </tr>
  <tr>
    <td><b>EgoHomes: Egocentric Household Activity Dataset</b><br/><sub>Python · MediaPipe · YOLOv8 · SAM 3 · Whisper · OpenCV · FFmpeg · MLX</sub><br/><sub><i>Domain: Robotics</i></sub></td>
    <td>Fully automated multimodal annotation pipeline for egocentric household activity video, producing synchronized hand pose, segmentation masks, depth maps and narration transcripts per frame for robotics foundation model pretraining. Integrates MediaPipe HandLandmarker (21-point hand skeleton), YOLOv8 pose estimation, SAM 3 for segmentation and Whisper for narration. JSON frame-level annotation schemas with automated quality control. Targeting open release alongside a VLA research paper.</td>
    <td><a href="https://github.com/aneessaheba/Egocentric_Homes">GitHub</a><br/><a href="https://egocentric-homes.vercel.app/">Live</a></td>
  </tr>
  <tr>
    <td><b>Face Mask Detection</b><br/><sub>MobileNetV2 · OpenCV · TensorFlow · Python</sub></td>
    <td>Real-time face mask detection using transfer learning with MobileNetV2, achieving 95%+ accuracy at 30+ FPS. OpenCV-based face detection with multi-face classification, optimized for edge deployment.</td>
    <td><a href="https://github.com/aneessaheba/Face-Mask-Detection-Using-ML">GitHub</a></td>
  </tr>
  <tr>
    <td><b>4DX Movie Technology</b><br/><sub>TensorFlow · CNN · Python · OpenCV · Audio Processing</sub></td>
    <td>CNN-based system processing synchronized audio-visual streams to detect dynamic movie events in real time and trigger physical theater effects (water, wind, seat motion) with millisecond-level precision for immersive 4DX experiences.</td>
    <td>—</td>
  </tr>
</table>

### Deep Learning

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Enveda CASMI 2026: Molecule Identification from Mass Spectra</b><br/><sub>Python · PyTorch · PyTorch Geometric · RDKit · matchms · Transformers · Contrastive Learning · LightGBM (Learning-to-Rank) · scikit-learn · Kaggle</sub><br/><sub><i>Domain: AI for Science</i></sub></td>
    <td>Pipeline that identifies unknown small molecules from tandem mass spectrometry (MS/MS) data, built for the Kaggle Enveda CASMI 2026 competition. Cleans and normalizes spectra, combines evidence from multiple spectra of the same compound, and ranks candidate 2D structures using learned spectrum and molecule embeddings. Compared a cosine-similarity spectral-matching baseline against neural approaches (a spectrum transformer encoder, graph neural network molecule encoders, and a contrastive spectrum-to-structure model), with a learning-to-rank re-ranker combining their scores. Documented experiment log and error analysis.</td>
    <td><a href="https://github.com/aneessaheba/ai-molecular-structure-identification-mass-spectra">GitHub</a></td>
  </tr>
</table>

### Machine Learning

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Hurricane Food Relief Priority: Predicting Food Aid Needs Before Landfall</b><br/><sub>Python · pandas · GeoPandas · scikit-learn · XGBoost · Optuna · SHAP · Fairlearn · Streamlit · Folium · pytest</sub><br/><sub><i>Also: Explainable AI, Fairness · Domain: Disaster Response</i></sub></td>
    <td>Predicts how badly each ZIP code will be damaged before a hurricane makes landfall, so relief teams can send food to the most vulnerable communities first. Combined 8 public data sources (FEMA, Census, CDC, USDA and NOAA) into a dataset covering 14 Atlantic hurricanes from 2016 to 2024. An XGBoost model reached a ROC-AUC of 0.78 and caught 82% of the most severely damaged areas on 5 storms it had never seen. A Food Relief Priority Index combines the model's predictions with a food-access score. A fairness audit shows the model works well for high-vulnerability communities, and a Streamlit dashboard shows maps and SHAP explanations. Written up as a paper for IEEE GHTC 2026.</td>
    <td><a href="https://github.com/aneessaheba/hurricane-food-relief-ml">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Credit Card Fraud Detection</b><br/><sub>PCA · Random Forest · Isolation Forest · Python · scikit-learn</sub><br/><sub><i>Also: Anomaly Detection · Domain: Finance</i></sub></td>
    <td>Anomaly detection pipeline for fraudulent transactions in highly imbalanced data, using PCA dimensionality reduction and ensemble methods (Isolation Forest + Random Forest) with SMOTE oversampling and precision-recall optimization.</td>
    <td>—</td>
  </tr>
</table>

### Big Data

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Real-Time Flight Delay Prediction Pipeline</b><br/><sub>Apache Kafka · Apache Spark · PySpark · HDFS · Apache Airflow · Docker</sub><br/><sub><i>Also: Machine Learning</i></sub></td>
    <td>End-to-end big data ML pipeline ingesting 19M+ flight records into HDFS, training GBT and Logistic Regression classifiers with Spark MLlib (3-fold CrossValidator), achieving AUC-ROC 0.94 and F1 0.90. Real-time streaming inference with Kafka + Spark Structured Streaming at 11,648 events/sec (23× above target). Serialized PipelineModels to HDFS, eliminating training/serving feature skew across batch and streaming paths.</td>
    <td><a href="https://github.com/aneessaheba/realtime-flight-delay-predictor-bigdata">GitHub</a></td>
  </tr>
</table>

### Data Engineering

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Stock Data ETL & Data Warehouse Pipeline</b><br/><sub>PostgreSQL · Docker · ETL · Dimensional Modeling · Apache Airflow · Kafka · TimescaleDB</sub><br/><sub><i>Also: Data Visualization</i></sub></td>
    <td>ETL pipeline for stock market data integrating multiple sources and automating ingestion across 50,567 records with 9 daily Airflow DAGs. Star-schema dimensional data warehouse in TimescaleDB. Dockerized workflows for reproducible deployments. 13 analytics visualizations in Tableau and Apache Superset covering YoY trends, volatility analysis, ROE rankings and correlation heatmaps.</td>
    <td><a href="https://github.com/aneessaheba/stock-data-etl-warehouse-pipelinee">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Spotify Data Analysis</b><br/><sub>AWS Glue · Snowflake · Power BI</sub><br/><sub><i>Also: Data Visualization</i></sub></td>
    <td>ETL pipeline with the Spotify API, AWS Glue and Snowflake. Interactive Power BI dashboards on peak listening hours, weekend patterns and top artists/tracks.</td>
    <td><a href="https://github.com/aneessaheba/Spotify-Data-Analysis">GitHub</a></td>
  </tr>
</table>

### Data Analytics & Visualization

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Comprehensive Public Health Analytics Dashboard</b><br/><sub>Python · SQL · Tableau · Pandas · CDC Socrata API</sub><br/><sub><i>Domain: Public Health</i></sub></td>
    <td>Multi-source pipeline aggregating CDC PLACES, CDC BRFSS, SAMHSA and WHO data across 721 US counties. Statistical analysis identifying a significant obesity–diabetes correlation (Pearson r=0.79, R²=0.63, p=1.56e-137) across 630 counties. Tableau dashboards with county-level choropleth maps, regional bar charts and scatter analytics for non-technical stakeholders.</td>
    <td><a href="https://github.com/aneessaheba/Comprehensive-Public-Health-Analytics-Dashboard">GitHub</a></td>
  </tr>
  <tr>
    <td><b>Retail Orders Analytics</b><br/><sub>Python · Pandas · SQL Server</sub><br/><sub><i>Also: Database Systems</i></sub></td>
    <td>End-to-end data pipeline processing a retail orders dataset with Python and Pandas, loaded into SQL Server. Analytics identifying top-performing products, regional sales patterns, monthly trends and year-over-year growth.</td>
    <td><a href="https://github.com/aneessaheba/Retail-Orders-Analytics-Project">GitHub</a></td>
  </tr>
</table>

### Distributed Systems

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Distributed Kayak Travel Booking System</b><br/><sub>FastAPI · Kafka · MySQL · MongoDB · Redis</sub></td>
    <td>Distributed travel booking system supporting search, booking, billing and analytics for flights, hotels and cars. FastAPI microservices with Kafka and relational + NoSQL databases. AI-powered recommendation service for personalized travel deals and real-time updates.</td>
    <td><a href="https://github.com/aneessaheba/distributed-kayak-booking-system">GitHub</a></td>
  </tr>
</table>

### Database Systems & Software Engineering

<table>
  <tr><th>Project</th><th>Details</th><th>Link</th></tr>
  <tr>
    <td><b>Stock Analysis Application</b><br/><sub>Python · OOP · GUI · SQLite</sub></td>
    <td>Object-oriented stock tracking application with console and GUI interfaces. Embedded SQLite database for stock data, historical price tracking from web APIs and CSV imports, profit/loss reports and interactive charts.</td>
    <td><a href="https://github.com/aneessaheba/StockMarketAnalysis">GitHub</a></td>
  </tr>
  <tr>
    <td><b>CheckMyGrade OOP Python</b><br/><sub>Python · OOP · CSV · Encryption</sub></td>
    <td>Console-based student grade management using OOP and CSV persistence. CRUD, search, sort with timing analysis, data encryption, academic reports and statistics. Array and linked-list backends with role-based menus and unit tests.</td>
    <td><a href="https://github.com/aneessaheba/CheckMyGrade-OOP-Python">GitHub</a></td>
  </tr>
</table>

## Experience

**Software Development Engineer** · Hewlett Packard (HP), Bengaluru · *Jul 2023 – Aug 2024*
- Built rule-based customer-support chatbots for HP printers, mapping user queries to intents using data from support transcripts and troubleshooting documents
- Designed conversation flows with conditional logic and fallbacks, integrated with backend APIs to fetch device status and recommended fixes
- Evaluated early LLM tools for improving response quality and coverage

**Software Engineer Intern** · Pheuna Technologies, Bengaluru · *May 2022 – Aug 2022*
- Built RESTful APIs with Node.js, Express and Sequelize, plus Kafka producers and consumers for real-time event processing
- Built a cross-platform React + Ionic dashboard for real-time monitoring

## Technical Skills

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,opencv,fastapi,react,nodejs,kafka,postgres,mysql,mongodb,redis,docker,aws,gcp,kubernetes,git&perline=9" alt="Skill icons" />
</p>

| Area | Skills |
|---|---|
| **LLMs & Generative AI** | Hugging Face Transformers · PEFT / LoRA · Fine-tuning · vLLM · LLM inference optimization · Llama · Gemma · Gemini · OpenAI · Ollama · Prompt engineering |
| **Agentic AI & RAG** | LangChain · LangGraph · ReAct · Tool calling · Multi-agent systems · RAG · Hybrid search (BM25 + vector) · ChromaDB · Elasticsearch · sentence-transformers · LLM-as-a-Judge |
| **Deep Learning** | PyTorch · TensorFlow · Keras · CUDA · Transformers · Vision Transformers · CNNs · LSTMs / RNNs · GANs · GNNs (PyTorch Geometric) · Contrastive learning · Transfer learning |
| **Computer Vision** | OpenCV · YOLOv8 · MediaPipe · Segment Anything (SAM) · Whisper |
| **Reinforcement Learning** | PPO · Self-play · Monte Carlo Tree Search · Stable-Baselines3 · Gymnasium |
| **Machine Learning** | scikit-learn · XGBoost · LightGBM · Optuna · Learning-to-rank · Anomaly detection · SMOTE · Feature engineering · SHAP · Fairlearn |
| **Data Engineering** | Kafka · Spark / PySpark · Spark MLlib · Hadoop / HDFS · Airflow · ETL · Dimensional modeling · Snowflake · AWS Glue |
| **Databases** | PostgreSQL · TimescaleDB · MySQL · SQL Server · MongoDB · Redis · SQLite · DuckDB |
| **Cloud & DevOps** | Docker · AWS (S3, EC2, ECS, SageMaker) · GCP · Kubernetes · Terraform |
| **Analysis & Visualization** | pandas · NumPy · GeoPandas · Matplotlib · Seaborn · Plotly · Folium · Tableau · Power BI · Apache Superset |
| **Languages & Frameworks** | Python · SQL · JavaScript · TypeScript · Go · FastAPI · Streamlit · Flask · Node.js · Express · React · HTML / CSS |
| **Tools** | Git · GitHub · Weights & Biases · pytest · Jupyter · Colab · Kaggle · LaTeX · VS Code · Postman · Jira |

## Education

| | |
|---|---|
| **San José State University** · San Jose, CA<br/>MS, Applied Data Intelligence · *Jan 2025 – May 2027* · GPA 3.5/4.0 | Gen AI LLMs · Agentic AI · Machine Learning · Deep Learning · Big Data Algorithms · Distributed Systems · Scalable Data Platforms |
| **Visvesvaraya Technological University** · Karnataka, India<br/>BE, Information Science and Engineering · *Aug 2019 – Jun 2023* · GPA 7.9/10.0 | Data Structures and Algorithms · Database Systems · Software Engineering |

## GitHub & LeetCode

<p align="center">
  <img src="https://streak-stats.demolab.com?user=aneessaheba&hide_border=true&background=00000000" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=aneessaheba&show_icons=true&hide_border=true&bg_color=00000000&count_private=true&include_all_commits=true" alt="GitHub Stats" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=aneessaheba&layout=compact&hide_border=true&bg_color=00000000&langs_count=8" alt="Top Languages" height="165"/>
</p>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/aneessaheba04?theme=light&font=Ubuntu&border=0" alt="LeetCode Stats" />
</p>

<p align="center"><sub>Thanks for stopping by. Feel free to reach out through any of the links at the top.</sub></p>
