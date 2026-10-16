"""Generates the light/dark SVG assets used by the profile README.

Run from the repo root:  python3 assets/build.py
Edit the content lists below, re-run, and commit the regenerated SVGs.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
W = 840

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": dict(panel="#f6f8fa", base="#ffffff", border="#d0d7de", text="#1f2328",
                  muted="#59636e", faint="#8c959f", accent="#5b4bdb", accent_soft="#ece9ff",
                  ok="#1a7f37", dot="#d0d7de"),
    "dark": dict(panel="#161b22", base="#0d1117", border="#30363d", text="#e6edf3",
                 muted="#9198a1", faint="#6e7681", accent="#a99cff", accent_soft="#2a2550",
                 ok="#3fb950", dot="#30363d"),
}

# ---------------------------------------------------------------- content

NOW = [
    "KV-cache compression · capstone",
    "Gemma 4 coding agent",
    "Pokémon TCG RL agent",
    "ViT from scratch · CUB-200",
    "CASMI 2026 · mass spectra",
]

BUTTONS = ["Email", "LinkedIn", "Portfolio", "Medium", "YouTube", "LeetCode", "Tableau"]

SECTIONS = [
    ("about", "01", "About Me", "whoami"),
    ("projects", "02", "Projects", "27 projects · 13 areas"),
    ("experience", "03", "Experience", "2 roles"),
    ("skills", "04", "Technical Skills", "12 areas"),
    ("education", "05", "Education", "2 degrees"),
    ("stats", "06", "GitHub & LeetCode", "activity"),
]

SKILLS = [
    ("LLMs & GenAI", "Hugging Face Transformers · PEFT / LoRA · Fine-tuning · vLLM · LLM inference optimization · Llama · Gemma · Gemini · OpenAI · Ollama · Prompt engineering"),
    ("Agentic AI & RAG", "LangChain · LangGraph · ReAct · Tool calling · Multi-agent systems · RAG · Hybrid search (BM25 + vector) · ChromaDB · Elasticsearch · sentence-transformers · LLM-as-a-Judge"),
    ("Deep Learning", "PyTorch · TensorFlow · Keras · CUDA · Transformers · Vision Transformers · CNNs · LSTMs / RNNs · GANs · GNNs (PyTorch Geometric) · Contrastive learning · Transfer learning"),
    ("Computer Vision", "OpenCV · YOLOv8 · MediaPipe · Segment Anything (SAM) · Whisper"),
    ("Reinforcement Learning", "PPO · Self-play · Monte Carlo Tree Search · Stable-Baselines3 · Gymnasium"),
    ("Machine Learning", "scikit-learn · XGBoost · LightGBM · Optuna · Learning-to-rank · Anomaly detection · SMOTE · Feature engineering · SHAP · Fairlearn"),
    ("Data Engineering", "Kafka · Spark / PySpark · Spark MLlib · Hadoop / HDFS · Airflow · ETL · Dimensional modeling · Snowflake · AWS Glue"),
    ("Databases", "PostgreSQL · TimescaleDB · MySQL · SQL Server · MongoDB · Redis · SQLite · DuckDB"),
    ("Cloud & DevOps", "Docker · AWS (S3, EC2, ECS, SageMaker) · GCP · Kubernetes · Terraform"),
    ("Analysis & Viz", "pandas · NumPy · GeoPandas · Matplotlib · Seaborn · Plotly · Folium · Tableau · Power BI · Apache Superset"),
    ("Languages & Frameworks", "Python · SQL · JavaScript · TypeScript · Go · FastAPI · Streamlit · Flask · Node.js · Express · React · HTML / CSS"),
    ("Tools", "Git · GitHub · Weights & Biases · pytest · Jupyter · Colab · Kaggle · LaTeX · VS Code · Postman · Jira"),
]

# ---------------------------------------------------------------- helpers

def e(s):
    return escape(s, {'"': "&quot;"})


def text_w(s, size, bold=False):
    """Rough rendered width; errs wide so nothing clips."""
    w = 0.0
    for ch in s:
        if ch in "il.,:;'|!·()[] ":
            w += 0.32
        elif ch in "mwMW@":
            w += 0.86
        elif ch.isupper() or ch.isdigit():
            w += 0.66
        else:
            w += 0.55
    return w * size * (1.06 if bold else 1.0)


def mono_w(s, size):
    return len(s) * 0.602 * size


def svg(width, height, title, body, style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t">\n'
            f'<title id="t">{e(title)}</title>\n'
            f'<style>text{{font-family:{SANS}}} .m{{font-family:{MONO}}}'
            f'@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}{style}</style>\n'
            f'{body}\n</svg>\n')


def write(name, theme, content):
    (OUT / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")

# ---------------------------------------------------------------- pieces

def hero(t):
    c = THEMES[t]
    H = 272
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.1" fill="{c["dot"]}"/>'
                   for x in range(470, 836, 16) for y in range(12, H - 6, 16))
    wx, wy, ww, wh = 494, 34, 314, 204
    lines = [f'<text class="m" x="{wx+18}" y="{wy+56}" font-size="12.5" fill="{c["faint"]}">$ cat now.txt</text>']
    for i, item in enumerate(NOW):
        y = wy + 56 + 22 * (i + 1)
        lines.append(f'<g>'
                     f'<text class="m" x="{wx+18}" y="{y}" font-size="12.5" fill="{c["accent"]}">▸</text>'
                     f'<text class="m" x="{wx+34}" y="{y}" font-size="12.5" fill="{c["text"]}">{e(item)}</text></g>')
    ylast = wy + 56 + 22 * (len(NOW) + 1)
    lines.append(f'<text class="m" x="{wx+18}" y="{ylast}" font-size="12.5" fill="{c["faint"]}">$</text>'
                 f'<rect class="cur" x="{wx+32}" y="{ylast-11}" width="7.5" height="14" fill="{c["accent"]}"/>')
    pill_label = "Open to ML / GenAI Engineer roles · 2027"
    pw = mono_w(pill_label, 12.5) + 50
    body = f'''<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>
{dots}
<text class="m" x="36" y="64" font-size="13" fill="{c["accent"]}">~/anees · san jose, ca</text>
<text x="34" y="114" font-size="40" font-weight="700" fill="{c["text"]}" letter-spacing="-0.5">Hi, I'm Anees</text>
<text x="36" y="148" font-size="14.5" font-weight="600" fill="{c["text"]}">LLMs &amp; Agentic AI · Deep Learning · Data Engineering</text>
<text x="36" y="176" font-size="13.5" fill="{c["muted"]}">MS in Applied Data Intelligence @ San José State University</text>
<rect x="36" y="206" width="{pw:.0f}" height="30" rx="15" fill="{c["base"]}" stroke="{c["border"]}"/>
<circle class="pulse" cx="55" cy="221" r="7" fill="{c["ok"]}" opacity="0.25"/>
<circle cx="55" cy="221" r="4" fill="{c["ok"]}"/>
<text class="m" x="70" y="225.5" font-size="12.5" fill="{c["muted"]}">{e(pill_label)}</text>
<rect x="{wx}.5" y="{wy}.5" width="{ww}" height="{wh}" rx="10" fill="{c["base"]}" stroke="{c["border"]}"/>
<line x1="{wx}" y1="{wy+30}" x2="{wx+ww}" y2="{wy+30}" stroke="{c["border"]}"/>
<circle cx="{wx+18}" cy="{wy+15}" r="4.5" fill="#ff5f57"/><circle cx="{wx+33}" cy="{wy+15}" r="4.5" fill="#febc2e"/><circle cx="{wx+48}" cy="{wy+15}" r="4.5" fill="#28c840"/>
<text class="m" x="{wx+ww/2}" y="{wy+19}" font-size="11" fill="{c["faint"]}" text-anchor="middle">now.txt</text>
{"".join(lines)}'''
    style = ('.cur{animation:b 1.1s steps(1) infinite}@keyframes b{50%{opacity:0}}'
             '.pulse{transform-origin:55px 221px;animation:p 2.4s ease-in-out infinite}'
             '@keyframes p{0%,100%{transform:scale(1);opacity:.25}50%{transform:scale(1.6);opacity:0}}')
    alt = ("Hi, I'm Anees. LLMs & Agentic AI, Deep Learning, Data Engineering. MS in Applied Data Intelligence "
           "at San José State University, San Jose, CA. Open to ML / GenAI Engineer roles starting 2027. "
           "Now working on: " + "; ".join(NOW) + ".")
    return svg(W, H, alt, body, style)


def button(t, label):
    c = THEMES[t]
    w = int(text_w(label, 13, True) + 58)
    body = f'''<rect x="0.5" y="0.5" width="{w-1}" height="35" rx="8" fill="{c["panel"]}" stroke="{c["border"]}"/>
<circle cx="16" cy="18" r="3.5" fill="{c["accent"]}"/>
<text x="27" y="22.5" font-size="13" font-weight="600" fill="{c["text"]}">{e(label)}</text>
<text class="m" x="{w-14}" y="22.5" font-size="12" fill="{c["faint"]}" text-anchor="end">↗</text>'''
    return svg(w, 36, label, body), w


def header(t, num, title, note):
    c = THEMES[t]
    H = 64
    tx = 44
    tend = tx + text_w(title, 22, True) + 16
    nw = mono_w(note, 11.5) + 8
    body = f'''<text class="m" x="2" y="40" font-size="13" fill="{c["accent"]}">{num}</text>
<text x="{tx}" y="41" font-size="22" font-weight="700" fill="{c["text"]}" letter-spacing="-0.2">{e(title)}</text>
<line x1="{tend:.0f}" y1="35.5" x2="{W - nw - 14:.0f}" y2="35.5" stroke="{c["border"]}"/>
<text class="m" x="{W-2}" y="39.5" font-size="11.5" fill="{c["faint"]}" text-anchor="end">{e(note)}</text>'''
    return svg(W, H, f"{num} {title}", body)


def skills(t):
    c = THEMES[t]
    x0, x1 = 214, W - 24
    ch_h, gap, lgap = 26, 6, 8
    y = 24
    parts = []
    for gi, (label, items) in enumerate(SKILLS):
        if gi:
            parts.append(f'<line x1="24" y1="{y - 9}" x2="{W-24}" y2="{y - 9}" stroke="{c["border"]}" stroke-dasharray="2 4"/>')
        parts.append(f'<text class="m" x="24" y="{y + 17}" font-size="11.5" fill="{c["accent"]}">{e(label.upper())}</text>')
        x = x0
        for item in items.split(" · "):
            w = text_w(item, 12.5) + 22
            if x + w > x1:
                x = x0
                y += ch_h + lgap
            parts.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{ch_h}" rx="6" fill="{c["base"]}" stroke="{c["border"]}"/>'
                         f'<text x="{x + w/2:.1f}" y="{y + 17.5}" font-size="12.5" fill="{c["text"]}" text-anchor="middle">{e(item)}</text>')
            x += w + gap
        y += ch_h + 22
    H = y - 4
    body = (f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>\n'
            + "\n".join(parts))
    alt = "Technical skills. " + " ".join(f"{l}: {i}." for l, i in SKILLS)
    return svg(W, H, alt, body)


def footer(t):
    c = THEMES[t]
    H = 150
    mail = "aneessaheba.guddi@sjsu.edu"
    bw = mono_w(mail + "  ↗", 13) + 40
    body = f'''<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{c["panel"]}" stroke="{c["border"]}"/>
<text class="m" x="36" y="50" font-size="12.5" fill="{c["accent"]}">$ echo "thanks for stopping by"</text>
<text x="34" y="92" font-size="28" font-weight="700" fill="{c["text"]}" letter-spacing="-0.3">Let's build something.</text>
<rect class="cur" x="{36 + mono_w('$ echo "thanks for stopping by"', 12.5) + 6:.0f}" y="39" width="7.5" height="14" fill="{c["accent"]}"/>
<text x="36" y="122" font-size="13.5" fill="{c["muted"]}">Open to ML / GenAI Engineer roles starting 2027 · email is fastest</text>
<rect x="{W - 36 - bw:.0f}" y="57" width="{bw:.0f}" height="36" rx="18" fill="{c["accent_soft"]}" stroke="{c["accent"]}" stroke-opacity="0.5"/>
<text class="m" x="{W - 36 - bw + 20:.0f}" y="80" font-size="13" fill="{c["accent"]}">{mail}  ↗</text>'''
    style = '.cur{animation:b 1.1s steps(1) infinite}@keyframes b{50%{opacity:0}}'
    return svg(W, H, f"Let's build something. Open to ML / GenAI Engineer roles starting 2027. Email {mail}.", body, style)

# ---------------------------------------------------------------- build

if __name__ == "__main__":
    widths = {}
    for t in THEMES:
        write("hero", t, hero(t))
        for label in BUTTONS:
            s, w = button(t, label)
            write(f"btn-{label.lower()}", t, s)
            widths[label] = w
        for key, num, title, note in SECTIONS:
            write(f"h-{key}", t, header(t, num, title, note))
        write("skills", t, skills(t))
        write("footer", t, footer(t))
    print("button widths:", widths)
