from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="SentinelEdge", version="0.1.0")

class Event(BaseModel):
    failed_logins: int = 0
    outbound_connections: int = 0
    unusual_port: bool = False
    dns_entropy: float = 0.0
    process_spike: float = 0.0

def score(e: Event):
    risk = 0
    reasons = []
    if e.failed_logins >= 5:
        risk += 25; reasons.append("Repeated failed logins")
    if e.outbound_connections >= 20:
        risk += 20; reasons.append("High outbound connection volume")
    if e.unusual_port:
        risk += 25; reasons.append("Unusual destination port")
    if e.dns_entropy >= 4.0:
        risk += 20; reasons.append("High DNS entropy")
    if e.process_spike >= 2.0:
        risk += 10; reasons.append("Process activity spike")
    label = "benign" if risk < 30 else ("suspicious" if risk < 60 else "high-risk")
    return {"risk_score": min(risk,100), "label":label, "reasons":reasons}

@app.get("/")
def root():
    return {"project":"SentinelEdge","message":"Local-first cyber threat detection prototype"}

@app.post("/analyze")
def analyze(event: Event):
    return score(event)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
