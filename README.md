# VisionRetail AI: CCTV-Powered Store Intelligence

## Overview

VisionRetail AI is an AI-powered Store Intelligence System designed to transform raw CCTV footage into actionable retail analytics.

The system processes multi-camera retail surveillance feeds, detects and tracks customers in real time, generates behavioral events, stores analytics data, and exposes production-ready APIs for store performance monitoring.

Built as a solution for the Purplle Tech Challenge 2026, the platform combines Computer Vision, Event Processing, Analytics, and Backend Engineering into a unified retail intelligence pipeline.

---

## Problem Statement

Retail stores generate large amounts of CCTV footage every day, but most of this data remains unused.

Store managers often lack visibility into:

* Customer footfall
* Zone popularity
* Customer movement patterns
* Funnel drop-offs
* Conversion opportunities
* Store anomalies

VisionRetail AI converts raw CCTV streams into structured business intelligence.

---

## Key Features

### Customer Detection & Tracking

* YOLOv8-based person detection
* Multi-frame tracking using ByteTrack
* Persistent visitor identities across frames

### Event Generation

The system automatically generates events such as:

* ENTRY
* EXIT
* REENTRY
* ZONE_ENTER
* ZONE_DWELL

### Store Analytics

* Unique visitor count
* Average dwell time
* Zone popularity analysis
* Customer funnel analysis
* Conversion monitoring
* Operational anomaly detection

### Heatmap Analytics

Identify high-engagement areas inside the store.

Examples:

* Skincare section engagement
* Makeup section engagement

### Production APIs

REST APIs expose:

* Metrics
* Funnel Analytics
* Heatmaps
* Anomalies
* Health Monitoring

### Dashboard

Live dashboard for visualizing store performance metrics.

---

## Architecture

```text
CCTV Videos
      │
      ▼
YOLOv8 Detection
      │
      ▼
ByteTrack Tracking
      │
      ▼
Event Generation
      │
      ▼
events.jsonl
      │
      ▼
FastAPI Ingestion
      │
      ▼
SQLite Database
      │
      ▼
Analytics Services
      │
      ├── Metrics API
      ├── Funnel API
      ├── Heatmap API
      └── Anomaly API
      │
      ▼
Dashboard
```

---

## Camera Configuration

| Camera | Purpose        |
| ------ | -------------- |
| CAM1   | Skincare Zone  |
| CAM2   | Makeup Zone    |
| CAM3   | Store Entrance |
| CAM4   | Staff Area     |
| CAM5   | Billing Area   |

---

## Technology Stack

### Computer Vision

* YOLOv8
* OpenCV
* NumPy
* Supervision
* ByteTrack

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Analytics

* Custom Event Processing
* Funnel Analytics
* Heatmap Analytics
* Anomaly Detection

### Testing

* Pytest

---

## Project Structure

```text
store-intelligence-system/

├── app/
│   ├── anomalies.py
│   ├── database.py
│   ├── funnel.py
│   ├── heatmap.py
│   ├── ingestion.py
│   ├── main.py
│   ├── metrics.py
│   └── models.py
│
├── pipeline/
│   ├── detect.py
│   ├── tracker.py
│   ├── entry_exit_detector.py
│   ├── queue_detector.py
│   ├── reentry_detector.py
│   ├── run_pipeline.py
│   └── session_manager.py
│
├── dashboard/
│   └── live_dashboard.py
│
├── scripts/
│   └── ingest_events.py
│
├── tests/
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## API Endpoints

### Health

```http
GET /health
```

### Ingest Events

```http
POST /events/ingest
```

### Store Metrics

```http
GET /stores/{store_id}/metrics
```

### Funnel Analytics

```http
GET /stores/{store_id}/funnel
```

### Heatmap Analytics

```http
GET /stores/{store_id}/heatmap
```

### Anomaly Detection

```http
GET /stores/{store_id}/anomalies
```

---

## Example Metrics Output

```json
{
  "store_id": "ST1008",
  "unique_visitors": 52,
  "purchase_count": 0,
  "conversion_rate": 0,
  "average_dwell_ms": 1000,
  "queue_depth": 0,
  "abandonment_rate": 0
}
```

---

## How To Run

### 1. Clone Repository

```bash
git clone https://github.com/Sindhu-987/store-intelligence-system.git
cd store-intelligence-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start API

```bash
uvicorn app.main:app --reload
```

### 6. Run Video Processing Pipeline

```bash
python -m pipeline.run_pipeline
```

### 7. Ingest Generated Events

```bash
python scripts/ingest_events.py
```

### 8. Launch Dashboard

```bash
python dashboard/live_dashboard.py
```

---

## Screenshots

### Swagger API

(Add Screenshot)

### Metrics Endpoint

(Add Screenshot)

### Funnel Analytics

(Add Screenshot)

### Heatmap Analytics

(Add Screenshot)

### Dashboard

(Add Screenshot)

---

## Future Enhancements

* Real-time RTSP stream support
* Multi-store analytics
* POS integration
* Queue prediction
* Customer re-identification
* Cloud deployment
* Real-time alerting

---

## Repository

GitHub Repository:

https://github.com/Sindhu-987/store-intelligence-system
