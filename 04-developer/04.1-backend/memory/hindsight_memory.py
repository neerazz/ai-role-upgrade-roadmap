"""Hindsight AI Memory lab for backend agents.

Loads configuration from .env and exercises retain, recall, and reflect
against your configured Hindsight instance.

Run from repo root:
    uv run python 04-developer/04.1-backend/memory/hindsight_memory.py
"""

from __future__ import annotations

import os
import sys
from dotenv import load_dotenv
from hindsight_client import Hindsight

# Pull configuration from .env
load_dotenv()

API_URL = os.getenv("HINDSIGHT_API_URL")
BANK_ID = os.getenv("HINDSIGHT_BANK_ID")

def _build_hindsight_client() -> Hindsight:
    clinet = Hindsight(base_url=API_URL)
    return clinet


def main() -> None:

    client = _build_hindsight_client()

    try:
        # 1. Health check
        version = client.get_version()
        print(f"Connected to Hindsight v{version.api_version} ({API_URL})")
        print(f"Using memory bank: '{BANK_ID}'\n")

        # 2. Retain: write facts with tags
        print("1. Retaining sample memories...")
        sample_memories = [
            ("User prefers Python with uv for package management.", ["user:preference", "topic:tooling"]),
            ("Backend agents require Human-in-the-loop gates for write operations.", ["policy:guardrails"]),
        ]
        for text, tags in sample_memories:
            client.retain(bank_id=BANK_ID, content=text, tags=tags)
            print(f"   ✓ Retained: {text}")

        # 3. Recall: semantic retrieval
        print("\n2. Recalling memories...")
        query = "What package manager and guardrail policies does the user follow?"
        print(f"   Query: '{query}'")
        recall_resp = client.recall(bank_id=BANK_ID, query=query)
        for idx, item in enumerate(getattr(recall_resp, "results", []), 1):
            print(f"   [{idx}] {item.text}")

        # 4. Reflect: synthesized reasoning over the bank
        print("\n3. Reflecting (synthesis)...")
        reflect_resp = client.reflect(bank_id=BANK_ID, query=query, budget="low")
        text = getattr(reflect_resp, "text", None) or getattr(reflect_resp, "response", "")
        if text:
            print(f"   Synthesis: {text.strip()}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
