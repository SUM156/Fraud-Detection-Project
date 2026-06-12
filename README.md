# Assignment 1 — AI System Specification
## PEAS Framework & Task Environment Analysis

**Student:** Sumair Ahmed  
**Roll No:** 2k24/AIE/62  
**Department:** Artificial Intelligence  
**University:** University of Sindh  
**Course:** Introduction to Artificial Intelligence  
**Email:** sumairahmedero@gmail.com  

---

## Selected System
**Option G — Fraud Detection System for Digital Payments & Banking Transactions**

---

## Repository Structure

```
fraud_detection_assignment/
│
├── README.md                          # This file
├── fraud_detection_peas.json          # Task 4: Structured JSON representation
└── peas_analysis.py                   # Python script to load and display PEAS spec
```

---

## Assignment Overview

### Task 1: PEAS Specification
- **Performance Measures:** 6 metrics including Transaction Accuracy Rate (≥99.5%), False Positive Rate, False Negative Rate, Avg. Detection Latency (<200ms), Financial Loss Prevented, Customer Disruption Score
- **Environment:** Real-time digital financial ecosystem (Online Banking, Card Networks, Interbank Settlement, Digital Wallets, ATMs)
- **Actuators:** Transaction Blocking Engine, Account Freeze Module, Risk-Based Auth Trigger, Customer Notification System, Case Management API, Model Feedback Writer
- **Sensors:** Transaction Data Stream, Geolocation & IP Intelligence, Behavioural Biometric Analyser, Device Fingerprinting Sensor, Historical Transaction DB API, Threat Intelligence Feed, Card Velocity Counter

### Task 2: Environment Classification
| Dimension | Classification |
|---|---|
| Observability | Partially Observable |
| Agent Type | Multi-Agent |
| Determinism | Stochastic |
| Temporal Structure | Sequential |
| Dynamism | Dynamic |
| State Space | Continuous |

### Task 3: Critical Analysis
- **Greatest Challenge:** Partial Observability — cardholder intent is never directly observable at decision time
- **Utility Function:** `U = α × Recall_fraud − β × FalsePositiveRate − γ × DetectionLatency`  
  Default weights: α=0.6, β=0.3, γ=0.1

### Task 4: Structured JSON
See `fraud_detection_peas.json` for the complete machine-readable PEAS specification.

---

## How to Run

```bash
python peas_analysis.py
```

Requirements: Python 3.x (no external libraries needed)
