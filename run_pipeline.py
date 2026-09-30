"""
Main Execution Entry Point for Proglite IT AI Automation Agent
Chains ingestion, AI triage reasoning, and automated multi-channel dispatch.
"""

from triage_agent import run_triage_pipeline
from dispatcher import run_dispatch_pipeline

def main():
    print("\n>>> STARTING END-TO-END AUTOMATION PIPELINE <<<\n")
    run_triage_pipeline()
    print()
    run_dispatch_pipeline()
    print("\n>>> PIPELINE EXECUTION COMPLETED SUCCESSFULLY <<<\n")

if __name__ == "__main__":
    main()
