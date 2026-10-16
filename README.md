<h1 align="center">I'm Anees Saheba Guddi</h1>
<h3 align="center">LLMs & Agentic AI | Deep Learning | Data Engineering</h3>
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

I'm an MS student in Applied Data Intelligence at **San José State University** (graduating May 2027), focused on **large language models, agentic AI and deep learning**.

My recent work spans the LLM stack: making long-context inference cheaper through KV-cache compression, building tool-using agents that fix real GitHub issues, and training Transformers, Vision Transformers, LSTMs and GANs from scratch in PyTorch. I care about careful evaluation: fair baselines, held-out test sets, controlled ablations, and honest write-ups of what didn't work.

I also build the systems around the models, including RAG pipelines, Kafka and Spark streaming pipelines, data warehouses and microservices. Before grad school I spent a year as a Software Development Engineer at **HP**, building customer-support chatbots.

I write about Generative AI and data engineering on [Medium](https://medium.com/@aneessaheba.guddi) and [YouTube](https://www.youtube.com/@BytAByte).

**Open to:** ML / GenAI Engineer roles starting 2027  ·  San Jose, CA

---

## Currently Working On

- **[KV-Cache Compression for Long-Context LLM Inference](https://github.com/aneessaheba/298a-kv-cache-compression):** benchmarking token eviction, low-bit quantization and learned autoencoder compression on Llama-3.1-8B at matched memory budgets (50%, 25%, 12.5%)
- **[Gemma 4 Developer Agent (software-engineering agent)](https://github.com/aneessaheba/autonomous-software-engineering-agent-gemma4):** an autonomous Gemma 4 coding agent that explores real GitHub repos, finds faulty code and generates patches that pass the tests, with tool use, self-correction and LoRA fine-tuning
- **[Pokémon TCG AI Battle Challenge (game-playing agent)](https://github.com/aneessaheba/pokemon-tcg-ai-battle-agent-rl):** a game-playing agent that handles hidden information, moving from heuristics to Monte Carlo Tree Search to a PPO policy trained through self-play
- **[PatchVision: Vision Transformer from Scratch for Fine-Grained Bird Classification](https://github.com/aneessaheba/PatchVision-ViT-from-Scratch-for-Bird-Classification):** a ViT trained from scratch on 200 bird species (CUB-200-2011), compared against a CNN baseline with controlled ablations
- **[Enveda CASMI 2026 (molecule identification from mass spectra)](https://github.com/aneessaheba/ai-molecular-structure-identification-mass-spectra):** identifying unknown molecules from MS/MS spectra using spectrum transformers, graph neural networks and contrastive learning, with a learning-to-rank re-ranker

---

## Projects

### Large Language Models (LLMs)

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
        <b>KV-Cache Compression for Long-Context LLM Inference</b><br/>
        <sub>Python · PyTorch · Hugging Face Transformers · NVIDIA kvpress · CUDA · Llama-3.1-8B / Llama-3.2-3B · LongBench · RULER · NVIDIA RTX 5090</sub>
      </td>
      <td>Researched and benchmarked KV-cache compression techniques for long-context LLM inference on Llama-3.1-8B. Surveyed and selected methods across three families: token eviction (StreamingLLM, SnapKV, PyramidKV, H2O, AdaKV, KVzip), low-bit quantization (KIVI, TurboQuant) and learned autoencoder compression (KV-CAR). Designed a shared evaluation framework that compares every method at the same measured memory budget (50%, 25% and 12.5% of full KV memory) on LongBench, Needle-in-a-Haystack and RULER. Studied whether combining eviction and quantization makes errors compound. Profiled GPU memory, latency and concurrent-session capacity on an NVIDIA RTX 5090.</td>
      <td><a href="https://github.com/aneessaheba/298a-kv-cache-compression">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Agentic AI

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
        <b>Gemma 4 Developer Agent (software-engineering agent)</b><br/>
        <sub>Python · Gemma 4 · Hugging Face Transformers · PEFT / LoRA · PyTorch · vLLM · ReAct-style Tool Calling · Git / Unified Diffs · pytest · Docker · Kaggle Notebooks · Weights & Biases</sub>
        <br/><sub><i>Also: LLM Fine-Tuning</i></sub>
      </td>
      <td>Autonomous coding agent built on Google's Gemma 4 for the Kaggle Gemma 4 Developer Agent competition. Given a real GitHub repository and an issue report, the agent explores the codebase, finds the faulty code, reasons about a fix, and generates a patch that passes the repository's validation tests. Evolved from a single-shot prompting baseline into a multi-step, tool-using agent with file search, code navigation, test execution and self-correction loops, plus LoRA fine-tuning on issue-to-patch data. Controlled experiments compared prompting strategies, tool sets and adapter settings, backed by a full experiment log, error analysis and a write-up of approaches that didn't work.</td>
      <td><a href="https://github.com/aneessaheba/autonomous-software-engineering-agent-gemma4">GitHub</a></td>
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

### Retrieval-Augmented Generation (RAG)

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
  </tbody>
</table>

---

### Reinforcement Learning

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
        <b>Pokémon TCG AI Battle Challenge (game-playing agent)</b><br/>
        <sub>Python · PyTorch · Kaggle PTCG Simulator SDK · Gymnasium · PPO / Self-Play RL (Stable-Baselines3) · Monte Carlo Tree Search · NumPy · pandas · Matplotlib · Kaggle Agents Ladder</sub>
        <br/><sub><i>Domain: Game AI</i></sub>
      </td>
      <td>Autonomous agent that plays competitive Pokémon Trading Card Game matches, built for the Kaggle PTCG AI Battle Challenge. Decides under hidden information (unknown opponent hands and decks), plans several turns ahead and adapts to different opponent strategies. Progressed from a rule-based heuristic baseline to Monte Carlo Tree Search with determinization, then to a PPO-trained policy/value network trained through self-play in the official simulator. Strategies compared through local round-robin tournaments and the Kaggle ladder, with full experiment tracking and analysis of failed strategies.</td>
      <td><a href="https://github.com/aneessaheba/pokemon-tcg-ai-battle-agent-rl">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Natural Language Processing (NLP)

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
        <b>Character-Level GPT Language Model</b><br/>
        <sub>Python · PyTorch · CUDA · Hugging Face Datasets · NumPy · Matplotlib</sub>
        <br/><sub><i>Built from scratch · Also: LLMs</i></sub>
      </td>
      <td>Decoder-only Transformer built from scratch that predicts the next character of a story, trained on the TinyStories dataset. Multi-head self-attention, causal masking, feedforward blocks and positional embeddings are written with plain tensor operations, without <code>nn.Transformer</code>, <code>nn.MultiheadAttention</code> or PyTorch's built-in attention. 4 blocks, width 256, 4 heads, 128-character context, 3.2M parameters. Reached 1.0875 validation bits per character and 76.1% top-1 next-character accuracy. <i>(Team project, DATA 266)</i></td>
      <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task1_llm/anees_saheba">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Yelp Review Sentiment Classification</b><br/>
        <sub>Python · PyTorch · LSTM · Attention · scikit-learn · pandas</sub>
        <br/><sub><i>Built from scratch</i></sub>
      </td>
      <td>Three binary sentiment classifiers trained from scratch on 504K Yelp Polarity reviews, with no pretrained embeddings or language models. All three share the same vocabulary, preprocessing and training loop and differ only in how a review becomes a single vector (max pooling baseline, 2-layer LSTM, learned attention pooling), keeping the comparison controlled. Preprocessing keeps negation words so "not good" is never read as "good". Best model (LSTM) reached 95.02% test accuracy and 0.950 macro F1. <i>(Team project, DATA 266)</i></td>
      <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task2_sentiment/anees_saheba">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Computer Vision

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
        <b>PatchVision: Vision Transformer from Scratch for Fine-Grained Bird Classification</b><br/>
        <sub>Python · PyTorch · torchvision · NumPy · pandas · scikit-learn · Matplotlib · Seaborn · Jupyter · CUDA</sub>
        <br/><sub><i>Built from scratch</i></sub>
      </td>
      <td>Vision Transformer built from first principles in PyTorch and trained from scratch, with no pretraining, to classify 200 visually similar bird species in CUB-200-2011 (11,788 images), testing whether a compact ViT can compete with a CNN when data is limited. Implemented patch embedding (224×224 → 196 tokens), a learnable class token, positional embeddings, 6 encoder blocks with multi-head self-attention and a 200-class head. Compared against a CNN baseline under the same split, augmentation, budget and protocol. Controlled ablations over patch size (8×8 vs 16×16), depth (2/4/6 blocks) and regularization, with best configs repeated over 3 seeds (mean ± std). Evaluated with top-1 accuracy, macro F1, per-class precision/recall, parameter count, training time and latency, and interpreted with confusion matrices, per-class error analysis and attention maps.</td>
      <td><a href="https://github.com/aneessaheba/PatchVision-ViT-from-Scratch-for-Bird-Classification">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>CycleGAN Photo-to-Monet Style Transfer</b><br/>
        <sub>Python · PyTorch · CycleGAN · PatchGAN · SciPy · Pillow · Kaggle</sub>
        <br/><sub><i>Built from scratch</i></sub>
      </td>
      <td>CycleGAN trained from scratch to translate between photographs and Monet paintings in both directions using unpaired data. Two ResNet generators (6 residual blocks, 12.2M parameters), two PatchGAN discriminators, least-squares adversarial loss and cycle-consistency loss. Scored with FID and KID, entered in a Kaggle evaluation, and backed by a 30-sample human audit. FID 86.59, KID 0.0075, Kaggle score -52.84. <i>(Team project, DATA 266)</i></td>
      <td><a href="https://github.com/aneessaheba/DATA-266-Lab-1/tree/main/task3_gan/anees_saheba">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>EgoHomes: Egocentric Household Activity Dataset</b><br/>
        <sub>Python · MediaPipe · YOLOv8 · SAM 3 · Whisper · OpenCV · FFmpeg · MLX</sub>
        <br/><sub><i>Domain: Robotics</i></sub>
      </td>
      <td>Fully automated multimodal annotation pipeline for egocentric household activity video, producing synchronized hand pose, segmentation masks, depth maps, and narration transcripts per frame for robotics foundation model pretraining. Integrates MediaPipe HandLandmarker (21-point hand skeleton), YOLOv8 pose estimation, SAM 3 for segmentation, and Whisper for narration. JSON frame-level annotation schemas with automated quality control. Targeting open release alongside a VLA research paper.</td>
      <td><a href="https://github.com/aneessaheba/Egocentric_Homes">GitHub</a> · <a href="https://egocentric-homes.vercel.app/">Live</a></td>
    </tr>
    <tr>
      <td>
        <b>Face Mask Detection Using ML</b><br/>
        <sub>MobileNetV2 · OpenCV · TensorFlow · Python</sub>
      </td>
      <td>Real-time face mask detection using transfer learning with MobileNetV2, achieving 95%+ accuracy at 30+ FPS. OpenCV-based face detection with multi-face classification, optimized for edge deployment.</td>
      <td><a href="https://github.com/aneessaheba/Face-Mask-Detection-Using-ML">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>4DX Movie Technology Using ML</b><br/>
        <sub>TensorFlow · CNN · Python · OpenCV · Audio Processing</sub>
      </td>
      <td>CNN-based system processing synchronized audio-visual streams to detect dynamic movie events in real-time and trigger physical theater effects (water, wind, seat motion) with millisecond-level precision for immersive 4DX experiences.</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

---

### Deep Learning

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
        <b>Enveda CASMI 2026 (molecule identification from mass spectra)</b><br/>
        <sub>Python · PyTorch · PyTorch Geometric · RDKit · matchms · Transformers · Contrastive Learning · LightGBM (Learning-to-Rank) · NumPy · pandas · scikit-learn · Matplotlib · Kaggle Notebooks</sub>
        <br/><sub><i>Domain: AI for Science</i></sub>
      </td>
      <td>AI-for-science pipeline that identifies unknown small molecules from tandem mass spectrometry (MS/MS) data, built for the Kaggle Enveda CASMI 2026 competition. Cleans and normalizes spectra, combines evidence from multiple spectra of the same compound, and ranks candidate 2D structures using learned spectrum and molecule embeddings. Compared a cosine-similarity spectral-matching baseline against neural approaches (a spectrum transformer encoder, graph neural network molecule encoders, and a contrastive spectrum-to-structure model), with a learning-to-rank re-ranker combining their scores. Documented experiment log and error analysis.</td>
      <td><a href="https://github.com/aneessaheba/ai-molecular-structure-identification-mass-spectra">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Machine Learning

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
        <b>Hurricane Food Relief Priority: Predicting Food Aid Needs Before Landfall</b><br/>
        <sub>Python · pandas · GeoPandas · scikit-learn · XGBoost · Optuna · SHAP · Fairlearn · Streamlit · Folium · Matplotlib · pytest</sub>
        <br/><sub><i>Also: Explainable AI, Fairness · Domain: Disaster Response</i></sub>
      </td>
      <td>Built a machine learning system that predicts how badly each ZIP code will be damaged before a hurricane makes landfall, so relief teams can send food to the most vulnerable communities first. Combined 8 public data sources (FEMA, Census, CDC, USDA and NOAA) into a dataset covering 14 Atlantic hurricanes from 2016 to 2024. Trained an XGBoost model that reached a ROC-AUC of 0.78 and caught 82% of the most severely damaged areas on 5 storms it had never seen. Created a Food Relief Priority Index by combining the model's predictions with a food-access score. Ran a fairness audit showing the model works well for high-vulnerability communities, and built a Streamlit dashboard with maps and SHAP explanations. Wrote up the work as a paper for IEEE GHTC 2026.</td>
      <td><a href="https://github.com/aneessaheba/hurricane-food-relief-ml">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Credit Card Fraud Detection</b><br/>
        <sub>PCA · Random Forest · Isolation Forest · Python · scikit-learn</sub>
        <br/><sub><i>Also: Anomaly Detection · Domain: Finance</i></sub>
      </td>
      <td>Anomaly detection pipeline for fraudulent transactions in highly imbalanced datasets using PCA dimensionality reduction and ensemble methods (Isolation Forest + Random Forest) with SMOTE oversampling and precision-recall optimization.</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

---

### Big Data

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
        <b>Real-Time Flight Delay Prediction Pipeline</b><br/>
        <sub>Apache Kafka · Apache Spark · PySpark · HDFS · Apache Airflow · Docker</sub>
        <br/><sub><i>Also: Machine Learning</i></sub>
      </td>
      <td>End-to-end big data ML pipeline ingesting 19M+ flight records into HDFS, training GBT and Logistic Regression classifiers with Spark MLlib (3-fold CrossValidator), achieving AUC-ROC 0.94 and F1 0.90. Real-time streaming inference with Kafka + Spark Structured Streaming at 11,648 events/sec (23× above target). Serialized PipelineModels to HDFS eliminating training/serving feature skew across batch and streaming paths.</td>
      <td><a href="https://github.com/aneessaheba/realtime-flight-delay-predictor-bigdata">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Data Engineering

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
        <br/><sub><i>Also: Data Visualization</i></sub>
      </td>
      <td>ETL pipeline for stock market data integrating multiple sources and automating ingestion across 50,567 records with 9 daily Airflow DAGs. Star-schema dimensional data warehouse in TimescaleDB for structured financial analysis. Dockerized workflows for reproducible deployments. 13 analytics visualizations in Tableau and Apache Superset covering YoY trends, volatility analysis, ROE rankings, and correlation heatmaps.</td>
      <td><a href="https://github.com/aneessaheba/stock-data-etl-warehouse-pipelinee">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Spotify Data Analysis</b><br/>
        <sub>AWS Glue · Snowflake · Power BI</sub>
        <br/><sub><i>Also: Data Visualization</i></sub>
      </td>
      <td>ETL pipeline with Spotify API, AWS Glue, and Snowflake. Interactive Power BI dashboards delivering insights on peak listening hours, weekend patterns, and top artists/tracks.</td>
      <td><a href="https://github.com/aneessaheba/Spotify-Data-Analysis">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Data Analytics & Visualization

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
        <b>Comprehensive Public Health Analytics Dashboard</b><br/>
        <sub>Python · SQL · Tableau · Pandas · CDC Socrata API</sub>
        <br/><sub><i>Domain: Public Health</i></sub>
      </td>
      <td>Multi-source pipeline aggregating CDC PLACES, CDC BRFSS, SAMHSA, and WHO data across 721 US counties. Statistical analysis identifying a significant obesity–diabetes correlation (Pearson r=0.79, R²=0.63, p=1.56e-137) across 630 counties. Tableau dashboards with county-level choropleth maps, regional bar charts, and scatter analytics for non-technical stakeholders.</td>
      <td><a href="https://github.com/aneessaheba/Comprehensive-Public-Health-Analytics-Dashboard">GitHub</a></td>
    </tr>
    <tr>
      <td>
        <b>Retail Orders Analytics Project</b><br/>
        <sub>Python · Pandas · SQL Server</sub>
        <br/><sub><i>Also: Database Systems</i></sub>
      </td>
      <td>End-to-end data pipeline processing a retail orders dataset with Python and Pandas, loaded into SQL Server. Advanced analytics identifying top-performing products, regional sales patterns, monthly trends, and year-over-year growth metrics.</td>
      <td><a href="https://github.com/aneessaheba/Retail-Orders-Analytics-Project">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Distributed Systems

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
        <b>Distributed Kayak Travel Booking System</b><br/>
        <sub>FastAPI · Kafka · MySQL · MongoDB · Redis</sub>
      </td>
      <td>Distributed travel booking system supporting search, booking, billing, and analytics for flights, hotels, and cars. FastAPI microservices with Kafka and relational + NoSQL databases. AI-powered recommendation service for personalized travel deals and real-time updates with resilient, high-throughput infrastructure.</td>
      <td><a href="https://github.com/aneessaheba/kayak-travel-system">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Database Systems

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
        <b>Stock Analysis Application</b><br/>
        <sub>Python · OOP · GUI · SQLite</sub>
      </td>
      <td>Object-oriented stock tracking application with console and GUI interfaces. Embedded SQLite database for saving and retrieving stock data, historical price tracking from web APIs and CSV imports, profit/loss report generation, and interactive chart visualization.</td>
      <td><a href="https://github.com/aneessaheba/StockMarketAnalysis">GitHub</a></td>
    </tr>
  </tbody>
</table>

---

### Software Engineering

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
![vLLM](https://img.shields.io/badge/vLLM-30A2FF?style=flat)

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
![Reinforcement Learning](https://img.shields.io/badge/Reinforcement_Learning-8E24AA?style=flat)
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat)
![SHAP](https://img.shields.io/badge/SHAP-FF0D57?style=flat)
![Fairlearn](https://img.shields.io/badge/Fairlearn-2C6FAC?style=flat)

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
