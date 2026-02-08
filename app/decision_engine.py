def decide_action(classification: dict) -> str:
    return "escalate" if classification["risk"] == "high" else "auto_reply"

