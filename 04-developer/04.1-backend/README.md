# Part 4.1: Backend developer — LangGraph, agents, and memory

> Hands-on track under [The Software Developer's AI Landscape](../README.md). This is the backend slice: you are putting probabilistic agents behind APIs, not just using a coding assistant.

Labs also resolve from [`../labs/04.1-backend/`](../labs/04.1-backend/).

## What is in this directory

| Path | What it is |
|------|------------|
| [`langchain-academy/`](langchain-academy/) | Snapshot of [langchain-ai/langchain-academy](https://github.com/langchain-ai/langchain-academy) (`UPSTREAM_SHA.txt`). Modules 0–6: setup, graphs, state, HITL, tools, **long-term memory**, deploy. |
| [`memory/`](memory/README.md) | The map this series adds on top of Academy: memory *types*, memory *products*, and a no-API lab that separates thread checkpoints from a cross-thread store. |

Academy is the LangGraph course. It does **not** by itself tell you when to use Hindsight vs Letta vs a Store. Read [`memory/README.md`](memory/README.md) before you treat chat history as "the memory system."

## Setup

From the **repository root** (the `pyproject.toml` there is the dependency owner):

```bash
uv sync
cp .env.example .env   # then set OPENAI_API_KEY, LANGSMITH_*, HINDSIGHT_*
uv run jupyter notebook 04-developer/04.1-backend/langchain-academy
```

Academy documents Python **3.11–3.13**. This repo allows `>=3.11`. If a notebook fails on 3.14, use 3.12.

Optional memory-vendor extras (Hindsight client, LangMem):

```bash
uv sync --extra memory
```

Studio graphs live in each module's `studio/` folder. With the venv active:

```bash
cd 04-developer/04.1-backend/langchain-academy/module-1/studio
uv run langgraph dev
```

## Suggested order

1. **This week:** Academy `module-0` + `module-1`. Then run [`memory/thread_vs_store.py`](memory/thread_vs_store.py) so "thread" and "store" are not the same word in your head.
2. **This month:** Academy `module-2` (state, trim, external checkpoint) then `module-5` (Store, profile vs collection, memory agent). Run [`memory/hindsight_memory.py`](memory/hindsight_memory.py) against your local Hindsight server.
3. **This quarter:** `module-3` (human-in-the-loop) and `module-4` (tools) before you put an agent on a write path. Deploy (`module-6`) last.

## Memory systems (read this)

Backend agents fail in production when one blob of "memory" is asked to do four jobs: this turn's messages, durable user facts, document knowledge, and the agent's own instructions. Split them.

| Plane | Scope | LangGraph primitive | Typical product |
|-------|--------|--------------------|-----------------|
| Working / short-term | One thread | State + **checkpointer** (`InMemorySaver`, Sqlite, Postgres) | The conversation you can resume |
| Long-term semantic | User / org, all threads | **Store** (`InMemoryStore`, PostgresStore, …) | "User prefers dark mode" |
| Episodic | Past runs as examples | Store or a dataset | Few-shot tool-call traces |
| Procedural | How the agent should behave | Store of prompts, or LangMem prompt rewrite | Skills / system prompt, not chat logs |
| Dedicated AI Memory | Multi-session, observations, reflection | Hindsight client (`retain`, `recall`, `reflect`) | Hindsight local instance (127.0.0.1:8890) or cloud |
| Knowledge (not memory) | Corpus | RAG index | Docs, tickets, code — see Part 4 RAG |

Hot path vs background: writing memories during the user turn is visible and slow; extracting them asynchronously is cheaper and easier to eval. Academy module-5 is the LangGraph version of this. Dedicated memory services like Hindsight implement observation consolidation, mental models, and deep reflection with low-latency local endpoints.

Full comparison, what to skip, and lab instructions: **[memory/README.md](memory/README.md)**.

## License

Academy notebooks remain under the upstream [LICENSE](langchain-academy/LICENSE). This repo's own labs and resource lists follow the root README (MIT for lab code, CC BY 4.0 for resource lists).
