# Memory systems for backend agents

Chat history is a log. A memory system is storage, a schema, a write policy, and a recall policy. If you cannot name those four, you do not have memory — you have a growing prompt.

This lab sits on [LangChain Academy module-2 and module-5](../langchain-academy/) and on LangGraph's own split: [short-term vs long-term](https://docs.langchain.com/oss/python/concepts/memory).

## 1. Two planes (do this first)

Run from the repo root after `uv sync`:

```bash
uv run python 04-developer/04.1-backend/memory/thread_vs_store.py
```

You should see: a second turn in the **same** `thread_id` still has the first user message; a **new** thread does not. Facts in the **store** are still there when you look up the user namespace, because they were never tied to a thread.

| Plane | Question it answers | Dies when | LangGraph API |
|-------|---------------------|-----------|----------------|
| **Thread / working memory** | What happened in *this* conversation? | You start a new thread (unless you copy state) | Checkpointer on `compile(checkpointer=...)` |
| **Long-term / store** | What is true about this *user or app* across conversations? | You delete the namespace/key | `BaseStore` (`put` / `get` / `search`) |

RAG is a third plane: **what do the documents say?** It is not user memory. See Part 4's RAG shelf.

## 2. Types of long-term memory

LangGraph (and the CoALA-style mapping) uses three content types. Academy module-5 implements the first two as **profile** vs **collection**.

| Type | Stores | Backend example | Failure mode if you skip it |
|------|--------|-----------------|-----------------------------|
| **Semantic** | Facts | `user.timezone = America/Los_Angeles` | Agent re-asks, or invents a profile |
| **Episodic** | Experiences / traces | Last successful refund tool sequence | Agent "knows" the policy but cannot replay how it did the task |
| **Procedural** | Instructions | System prompt, skills, tool-choice rules | You fine-tune or stuff more RAG instead of editing the prompt |

Two shapes for semantic memory:

- **Profile** — one JSON document you patch each turn. Coherent, but large profiles get lossy updates.
- **Collection** — many small memories you insert/update/delete. Higher recall, harder writes (Trustcall in Academy exists for this).

Two write policies:

- **Hot path** — the agent decides to save during the user turn (visible, adds latency).
- **Background** — extract after the turn (better latency; other threads can be stale until the job runs).

## 3. Systems you will actually choose among

These are not interchangeable "memory databases." They sit on different planes.

| System | Plane it owns | Use it when | Skip when |
|--------|---------------|-------------|-----------|
| **LangGraph checkpointer** | Thread state | You need resume, HITL, and replay of one graph run | You need facts to follow the user to a new chat |
| **LangGraph Store** (+ [LangMem](https://github.com/langchain-ai/langmem)) | Cross-thread JSON + optional semantic search; LangMem adds manage/search tools and prompt rewrite | You already run LangGraph and want memory as graph infrastructure | You need a productized conflict-resolution layer today |
| **Hindsight** | Dedicated AI memory service (retain, recall, reflect, mental models, knowledge pages, observations) | Multi-agent long-term memory across sessions/repos with local daemon/Docker or cloud API | You only have one thread and a checkpointer would do |
| **Letta (MemGPT)** | Memory as the agent runtime (self-editing context, persistence) | You want a memory-first agent OS, not "LangGraph + a store" | You already have a graph and only need a Store |
| **Zep** | Temporal / graph memory | "When they said it" changes the answer | You only need the latest preference, not history-of-beliefs |
| **RAG index** (pgvector, etc.) | Knowledge | Grounding in a corpus | User preferences, session decisions, or "remember I said X yesterday" |

Academy coverage:

| Academy notebook | Memory topic |
|------------------|--------------|
| `module-2/chatbot-external-memory.ipynb` | Checkpointer / external thread state |
| `module-2/trim-filter-messages.ipynb` | Working memory that does not blow the context window |
| `module-2/chatbot-summarization.ipynb` | Compress thread history (still thread-scoped) |
| `module-5/memory_store.ipynb` | Store namespaces, put/get/search |
| `module-5/memoryschema_profile.ipynb` | Semantic memory as a profile |
| `module-5/memoryschema_collection.ipynb` | Semantic memory as a collection |
| `module-5/memory_agent.ipynb` | Agent that reads/writes long-term memory |

## 4. Running the Hindsight Memory Lab

This repository connects directly to your local Hindsight instance (`http://127.0.0.1:8890`).

Install optional memory dependencies and run the lab:

```bash
uv sync --extra memory
uv run python 04-developer/04.1-backend/memory/hindsight_memory.py
```

The script demonstrates:
1. **Connectivity & version check** against your local Hindsight server.
2. **Retain** (`retain`): Ingesting semantic facts, user preferences, and observations with provenance tags.
3. **Semantic recall** (`recall`): Retrieving relevant memory units and entity context for a query.
4. **Deep reflection** (`reflect`): Synthesizing beliefs and operational profiles across the memory bank.

## 5. What to skip

- **Dumping the full transcript into every request and calling it long-term memory.** That is an unbounded working set. Trim, summarize, or checkpoint; put durable facts in a store.
- **One vector DB for docs and user facts.** Retrieval that was tuned for PDFs will not do conflict resolution, expiry, or "the user changed their name."
- **Adding dedicated memory services before understanding thread vs store.** Get thread vs store right in LangGraph. Add a vendor/service like Hindsight when you have a write policy and an eval (wrong memory is worse than no memory).
- **Autonomous lifelong memory with no delete/expiry.** That is still experimental in this series' maturity matrix.

## 6. This month

1. Run `thread_vs_store.py`.
2. Run `hindsight_memory.py` against your local Hindsight instance.
3. Work Academy module-2, then module-5, with LangSmith tracing on (`LANGSMITH_TRACING_V2=true`).
4. Write five memories you would actually persist for *your* product. Label each semantic / episodic / procedural. If you cannot label it, it does not belong in the store.

