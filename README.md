# SentinelEdge — On-Device AI Cyber Threat Detection

SentinelEdge is a student-friendly cybersecurity prototype that demonstrates how lightweight machine learning can identify suspicious endpoint/network behaviour while keeping raw telemetry on the device.

## Problem
Traditional monitoring pipelines often send telemetry to a central server, increasing latency and privacy exposure. Students need a practical way to understand detection, explainability, and response without building a large SOC stack.

## Solution
SentinelEdge extracts compact behavioural features, calculates a risk score, classifies events as benign/suspicious/high-risk, and presents an explainable alert locally.

## Core Features
- Lightweight anomaly/risk scoring
- Explainable alert reasons
- Local-first processing
- Mock telemetry generator for demonstrations
- REST API prototype
- Snapdragon-ready architecture: inference can be replaced with an ONNX/TFLite model optimized for ARM/Qualcomm hardware

## Demo
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/app.py
```
Then open http://127.0.0.1:8000

## Snapdragon note
This repository is an architecture/prototype and does not claim that inference has already been benchmarked on a Snapdragon laptop. Hardware benchmarking should be performed on an eligible Snapdragon-powered laptop before making performance claims.

## Suggested future work
- Export a trained model to ONNX/TFLite
- Quantize to INT8
- Add real packet metadata ingestion
- Benchmark latency, RAM and battery impact on Snapdragon hardware
- Add signed alert logs and a small local dashboard
