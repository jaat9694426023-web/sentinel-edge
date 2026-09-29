from src.app import Event, score

def test_high_risk():
    r = score(Event(failed_logins=8, outbound_connections=30, unusual_port=True, dns_entropy=5.1, process_spike=3))
    assert r["label"] == "high-risk"
    assert r["risk_score"] == 100
