# Quantitative Signal Pipeline

## 📌 Overview

This project implements a simplified **end-to-end trading signal pipeline**, simulating a real-world workflow used in quantitative trading systems.

It covers:

* Strategy development (EMA crossover)
* Backtesting on historical market data
* Signal ingestion via webhook
* Mock trade execution
* Reporting and analytics

---

## 🧠 Architecture

```
API Layer → Service Layer → Core Logic → Data Layer
```

The system is designed with **modularity, clarity, and scalability** in mind.

---

## ⚙️ Tech Stack

* Python 3.11+
* FastAPI
* Pandas
* yfinance
* Pydantic

---

## 🚀 Features

### 1. 📊 Backtesting Engine

Implements a **9/21 EMA crossover strategy**:

* BUY when EMA(9) crosses above EMA(21)
* SELL when EMA(9) crosses below EMA(21)

#### Metrics Generated:

* Total Return
* Win Rate
* Max Drawdown
* Number of Trades

#### ▶️ Run Backtest

```bash
python -m scripts.run_backtest
```

#### 📁 Output

```
data/backtest_results.json
```

---

### 2. 🌐 Webhook Signal Ingestion

#### Endpoint:

```
POST /webhook
```

#### Sample Payload:

```json
{
  "symbol": "AAPL",
  "side": "BUY",
  "qty": 10,
  "price": 180
}
```

#### Features:

* Schema validation using Pydantic
* Duplicate signal detection
* Structured logging with unique IDs
* Mock execution engine

#### 📁 Logs

```
data/signals.log
```

---

### 3. 📈 Reporting API

#### Endpoint:

```
GET /report
```

#### Returns:

* Backtest results
* Total signals processed

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone <https://github.com/akhil-haridas/quantitative-signal-pipeline.git>
cd quantitative-signal-pipeline
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Application

```bash
uvicorn app.main:app --reload
```

---

### 5. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing the Webhook

Example using curl (Windows PowerShell):

```bash
curl -X POST http://127.0.0.1:8000/webhook `
-H "Content-Type: application/json" `
-d "{\"symbol\":\"AAPL\",\"side\":\"BUY\",\"qty\":10,\"price\":180}"
```

---

## 📁 Project Structure

```
quantitative-signal-pipeline/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── data/
├── scripts/
├── tests/
├── README.md
├── requirements.txt
```

---

## 🧩 Design Decisions

* **Layered Architecture** → Clear separation of concerns
* **Stateless Services** → Easy to scale and test
* **File-based Storage** → Lightweight and transparent
* **Deterministic Backtesting** → Reproducible results

---

## ⚡ Trade-offs

* No database used → Simplified for assessment scope
* Mock execution instead of real broker integration
* Limited strategy parameters (fixed EMA values)

---

## 🔮 Future Improvements

* Database integration (PostgreSQL / Redis)
* Real broker API integration (Binance / Alpaca)
* Strategy parameter optimization
* Advanced metrics (Sharpe Ratio, Sortino Ratio)
* Docker containerization

---

## 👨‍💻 Author

Developed as part of a full-stack technical assessment demonstrating:

* Backend system design
* API development
* Data processing
* Clean architecture principles

---

## ✅ Summary

This project demonstrates a **realistic trading pipeline**, balancing:

* Simplicity
* Maintainability
* Extensibility

Designed to reflect how production-grade systems are structured in quantitative trading environments.
