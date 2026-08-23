# BatteryGuard — AI Battery Health Analysis Assistant

BatteryGuard is a full-stack AI-powered battery health analysis assistant. It processes battery cycle telemetry (voltage, current, temperature, charge cycles), estimates State-of-Charge (SoC), computes capacity fade trends, flags anomalous behavior using statistical detection, and provides grounded maintenance recommendations via **RAG (Retrieval-Augmented Generation)** over battery engineering literature using **NVIDIA NIM API** and **ChromaDB**.

---

## 🌟 Key Features

1. **Synthetic Battery Cycle Dataset**: 5 battery units over 500 charge cycles (2,500 total records) with realistic degradation curves and injected anomalies.
2. **State-of-Charge (SoC) Estimation**: Dual-method estimation using OCV lookup tables and Coulomb counting integration.
3. **Interactive Visualizations (Recharts)**:
   - Capacity Fade Area Chart with 80% EOL reference line
   - Dual-Axis Charge/Discharge CC-CV Curve Chart
   - Animated SVG State-of-Charge Radial Gauge
   - Internal Resistance Growth Chart
   - Anomaly Timeline Scatter Plot
4. **Statistical Anomaly Detection**: Z-score thresholding (|Z| > 2.5/3.0) for thermal spikes (>50°C), voltage sags/overvoltages, current surges, and capacity drops.
5. **RAG Knowledge Base**: 5 battery maintenance and electrochemistry manuals ingested into **ChromaDB** using **NVIDIA NIM `nvidia/nv-embedqa-e5-v5`** embeddings.
6. **AI Recommendations**: Powered by **NVIDIA NIM `meta/llama-3.1-70b-instruct`**, generating actionable maintenance schedules grounded in retrieved RAG context.

---

## 🛠️ Tech Stack

- **Frontend**: React (Vite), Tailwind CSS, Recharts, Framer Motion, Lucide Icons, React Markdown
- **Backend**: Python Flask, REST API, Pandas, NumPy, SciPy
- **Vector DB**: ChromaDB (Local persistent vector store)
- **AI Models (NVIDIA NIM)**:
  - Generation: `meta/llama-3.1-70b-instruct`
  - Embeddings: `nvidia/nv-embedqa-e5-v5`
  - Base URL: `https://integrate.api.nvidia.com/v1`

---

## 📁 Project Structure

```
Battery IQ/
├── data/
│   └── battery_cycles.csv         # Synthetic battery cycle dataset (2,500 rows)
├── backend/
│   ├── app.py                      # Flask REST API entry point
│   ├── requirements.txt            # Backend Python dependencies
│   ├── .env.example                # Template for environment variables
│   ├── data/
│   │   ├── generate_data.py        # Data generator script
│   │   └── battery_cycles.csv      # Generated dataset
│   ├── knowledge_base/             # Battery technical docs
│   │   ├── battery_basics.md
│   │   ├── charging_best_practices.md
│   │   ├── degradation_factors.md
│   │   ├── temperature_effects.md
│   │   └── maintenance_guide.md
│   ├── routes/                     # Flask REST Blueprints
│   │   ├── battery.py              # Battery status endpoints
│   │   ├── analysis.py             # Degradation analysis & trends
│   │   ├── anomaly.py              # Anomaly detection & timeline
│   │   └── rag.py                  # Ingestion & AI recommendations
│   └── services/
│       ├── data_loader.py          # Data caching & loader
│       ├── soc_estimator.py        # SoC & charge curve algorithms
│       ├── anomaly_detector.py     # Statistical anomaly detector
│       ├── embeddings.py           # NVIDIA NIM embedding service
│       ├── rag_service.py          # ChromaDB vector store manager
│       └── llm_service.py          # NVIDIA NIM LLM service
├── frontend/
│   ├── src/
│   │   ├── components/             # Reusable UI & Chart components
│   │   ├── pages/                  # Overview, Analysis, Anomalies, Assistant
│   │   ├── api/client.js           # Axios API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── README.md
└── .gitignore
```

---

## ⚡ Quick Start & Setup

### 1. Prerequisites
- Python 3.10+
- Node.js 18+

### 2. Backend Setup
```bash
# Navigate to project root
cd "Battery IQ"

# Install Python requirements
py -m pip install -r backend/requirements.txt

# Create .env file in backend/ with your NVIDIA API Key
# Copy backend/.env.example to backend/.env and set NVIDIA_API_KEY
```

### 3. Generate Data & Ingest Knowledge Base
```bash
# Generate synthetic dataset
py backend/data/generate_data.py

# Start Flask backend server (Port 5000)
py backend/app.py
```

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 🌐 Live Demo & Deployment

- **Frontend**: [BatteryGuard Vercel App](https://batteryguard-ai.vercel.app) *(Placeholder)*
- **Backend API**: [BatteryGuard Render Web Service](https://batteryguard-api.onrender.com) *(Placeholder)*
