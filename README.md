# 🤖 AI-Powered IT Helpdesk Triage & Automation Agent

An end-to-end autonomous triage and automation engine designed for modern IT Managed Service Providers (MSPs). Built specifically to automate recurring IT helpdesk operations, triage urgent incidents (M365 access, network/VPN outages, security phishing alerts), and execute automated multi-channel routing.

---

## 🎯 Project Overview & Problem Statement

IT Managed Service teams waste hundreds of hours manually categorizing tickets, routing issues, and typing standard resolution steps. 

This project solves this by:
1. **Intelligent AI Ingestion & Analysis:** Ingests unformatted, raw incoming tickets and leverages Generative AI (LLMs) to classify Category, Priority (P1–P4), Root Cause, and Recommended Troubleshooting steps.
2. **Automated Multi-System Dispatch:** Automatically routes emergency tickets to Slack/Teams channels via Webhooks, generates instant self-service email responses to users, and synchronizes tickets with Jira Service Management REST APIs.

---

## 🏗️ Architecture & Pipeline Flow

```text
[ Incoming Tickets (JSON / API) ]
                 │
                 ▼
[ Triage AI Agent (triage_agent.py) ]
    ├─ Contextual Intent & Sentiment Analysis
    ├─ Dynamic Priority (P1 Critical - P4 Low)
    ├─ Root Cause Hypothesis
    └─ Generates Actionable Troubleshooting Plan
                 │
                 ▼
[ Automated Integrations Engine (dispatcher.py) ]
    ├─ High-Priority P1/P2 Alerts  --->  📢 Slack / Teams Emergency Webhook
    ├─ Self-Serviceable Issues     --->  ✉️ Instant Troubleshooting Email
    └─ All Service Requests        --->  🎫 Jira Service Management API
```

---

## 🛠️ Tech Stack & Skills Demonstrated

- **Language:** Python 3
- **AI & Reasoning:** Google Gemini API / Claude API integration with robust contextual fallback engine
- **Integration Protocols:** REST APIs, HTTP Webhooks, JSON Data Interchange
- **Automation Targets:** Microsoft 365 Operations, Jira Service Desk, Slack / Teams
- **Development Best Practices:** Structured modular code, Unicode cross-platform compatibility, clean audit logging

---

## 📁 Repository Structure

```text
ai-ticket-triage-agent/
│
├── tickets.json             # Sample incoming raw enterprise IT support tickets
├── triage_agent.py          # Core AI Triage reasoning pipeline
├── dispatcher.py            # Automated multi-channel dispatch & integrations
├── run_pipeline.py          # Unified end-to-end execution runner
├── triaged_results.json     # Enriched structured data output from AI
├── dispatch_audit_log.json  # Comprehensive audit history of automated actions
└── README.md                # Project architecture & documentation
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure Python 3.9+ is installed:
```bash
python --version
```

### 2. Run the End-to-End Pipeline
Execute the master runner:
```bash
python run_pipeline.py
```

### 3. Optional: Enable Live Gemini LLM API
Set your Gemini API key in your environment:
```bash
set GEMINI_API_KEY="your-api-key-here"
python run_pipeline.py
```
*(If no API key is provided, the agent automatically runs on its built-in offline contextual reasoning engine).*

---

## 📋 Sample Execution Output

```text
>>> STARTING END-TO-END AUTOMATION PIPELINE <<<

🤖 PROGLITE AI AGENT: IT SUPPORT TICKET TRIAGE & DISPATCH
[*] Reading incoming tickets from tickets.json...

[🔄 Processing] Ticket: INC-1001 | From: sarah.finance@proglite-demo.com
  ├─ Category: M365 / Cloud Operations
  ├─ Priority: P1 - Critical
  ├─ Suggested Fix: Grant temporary elevated scope 'User.ReadWrite.All' via Microsoft Entra ID admin portal.
  └─ Route To: #m365-admins (Auto-resolve: False)

[🔄 Processing] Ticket: INC-1002 | From: rajesh.dev@proglite-demo.com
  ├─ Category: Network / VPN
  ├─ Priority: P2 - High
  ├─ Suggested Fix: Push refreshed client ovpn configuration bundle with TCP 443 fallback via Intune.
  └─ Route To: #network-team (Auto-resolve: True)

⚡ PROGLITE AUTOMATION ENGINE: SYSTEM DISPATCH & INTEGRATIONS
[🚀 Dispatching Action] INC-1001 (P1 - Critical)
    📢 [WEBHOOK SENT -> #m365-admins] Alerting duty on-call engineer for INC-1001
    🎫 [JIRA API -> ITSD] Issue created and placed into queue for category: M365 / Cloud Operations

>>> PIPELINE EXECUTION COMPLETED SUCCESSFULLY <<<
```

---

## 👨‍💻 Author

**Vegupathirajan Gothandaraman**  
- **Email:** vegupathi666@gmail.com  
- **LinkedIn:** [Vegupathirajan Gothandaraman](https://www.linkedin.com/in/vegupathi-gothandaraman-voimedu/)  
- **Portfolio:** [vegudev.github.io/portfolio](https://vegudev.github.io/portfolio/)
