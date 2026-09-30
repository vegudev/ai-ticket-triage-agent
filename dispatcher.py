"""
Automated Dispatcher & Integrations Engine
Dispatches triaged tickets to Slack/Teams Webhooks, Jira Ticketing API, and Automated Email Responses.
Target Domain: Proglite Managed IT Services
Author: Vegupathirajan Gothandaraman
"""

import sys
import json
import time
from datetime import datetime

# Windows console unicode fix
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def send_slack_webhook_alert(channel: str, ticket_id: str, summary: str, priority: str):
    """Simulates sending an urgent alert payload to Slack / Microsoft Teams Webhook API."""
    payload = {
        "channel": channel,
        "username": "Proglite-AI-Triage-Bot",
        "attachments": [
            {
                "color": "#D32F2F" if "P1" in priority else "#FFA000",
                "title": f"🚨 [{priority}] New Triage Alert: {ticket_id}",
                "text": summary,
                "timestamp": datetime.now().isoformat()
            }
        ]
    }
    # In production, this calls: requests.post(WEBHOOK_URL, json=payload, timeout=5)
    print(f"    📢 [WEBHOOK SENT -> {channel}] Alerting duty on-call engineer for {ticket_id}")
    return {"status": "DELIVERED", "channel": channel}

def auto_generate_resolution_email(recipient: str, ticket_id: str, troubleshooting_steps: str):
    """Simulates sending an automated fix/troubleshooting guide directly to user's inbox."""
    email_body = f"""
    Hello,
    
    This is an automated quick-resolution from Proglite IT AI Support regarding Ticket {ticket_id}.
    
    Recommended fix:
    {troubleshooting_steps}
    
    If this resolves your issue, please reply with 'RESOLVED'. Otherwise, a technician is assigned.
    """
    print(f"    ✉️  [AUTO-EMAIL SENT -> {recipient}] Instant self-service instructions dispatched")
    return {"status": "DISPATCHED_TO_USER", "recipient": recipient}

def create_jira_service_ticket(ticket_id: str, category: str, priority: str):
    """Simulates creating an issue in Jira / Confluence Service Management REST API."""
    jira_payload = {
        "fields": {
            "project": {"key": "ITSD"},
            "summary": f"[{category}] Automated Triage from {ticket_id}",
            "priority": {"name": priority.split(" - ")[0]}
        }
    }
    print(f"    🎫 [JIRA API -> ITSD] Issue created and placed into queue for category: {category}")
    return {"status": "JIRA_LOGGED", "queue": category}

def run_dispatch_pipeline():
    """Reads triaged results and executes automated actions."""
    print("=" * 65)
    print("⚡ PROGLITE AUTOMATION ENGINE: SYSTEM DISPATCH & INTEGRATIONS")
    print("=" * 65)

    try:
        with open("triaged_results.json", "r", encoding="utf-8") as f:
            triaged_tickets = json.load(f)
    except FileNotFoundError:
        print("[!] triaged_results.json not found. Run triage_agent.py first!")
        return

    audit_logs = []

    for item in triaged_tickets:
        t_id = item["ticket_id"]
        meta = item["triage_metadata"]
        priority = meta["priority"]
        channel = meta["routing_channel"]
        can_auto_resolve = meta["can_auto_resolve"]
        sender = item["sender"]

        print(f"\n[🚀 Dispatching Action] {t_id} ({priority})")
        time.sleep(0.4)

        actions_taken = []

        # Action 1: If Critical/High, alert team via Webhook
        if "P1" in priority or "P2" in priority:
            wb_result = send_slack_webhook_alert(channel, t_id, meta["suggested_troubleshooting"], priority)
            actions_taken.append(wb_result)

        # Action 2: If self-serviceable, immediately email resolution to user
        if can_auto_resolve:
            email_result = auto_generate_resolution_email(sender, t_id, meta["suggested_troubleshooting"])
            actions_taken.append(email_result)

        # Action 3: Log in Jira ticketing system
        jira_result = create_jira_service_ticket(t_id, meta["category"], priority)
        actions_taken.append(jira_result)

        audit_logs.append({
            "ticket_id": t_id,
            "priority": priority,
            "actions": actions_taken,
            "dispatched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # Save audit report
    with open("dispatch_audit_log.json", "w", encoding="utf-8") as f:
        json.dump(audit_logs, f, indent=2)

    print("\n" + "=" * 65)
    print("🎯 ALL AUTOMATIONS EXECUTED: Saved to 'dispatch_audit_log.json'!")
    print("=" * 65)

if __name__ == "__main__":
    run_dispatch_pipeline()
