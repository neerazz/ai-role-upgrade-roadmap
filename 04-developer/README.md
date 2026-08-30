# Part 4: The Software Developer's AI Landscape — Curated Resources

> Companion reference shelf for [the Part 4 article](../README.md#the-complete-roadmap). The article is the map; this is the full graded path.

This is the widest and noisiest territory in the series. The job is not "learn every agent framework." It is to get good at six things that show up in production: **coding agents, RAG, tool use, memory, evaluation, and the architecture patterns** you need when a probabilistic agent is a real software component — not a demo.

Assumes you've read [Part 1: The AI Foundation](../01-foundation/README.md). Adjacent maps: [Security](../03-security/README.md) (prompt injection and tool-runtime risk) and [Data Engineering](../README.md) (the retrieval and embedding pipelines RAG sits on).

### Grading Key
- **Grade A (Essential):** Skip this and you'll have a real blind spot in AI-native software development.
- **Grade B (Highly Recommended):** Worth the time if you're shipping agents or RAG, not just using a coding assistant.
- **Grade C (Useful for Depth):** Only if you're going deep in a specific sub-domain.

### Beginner Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [Claude Code overview](https://code.claude.com/docs/en/overview) | docs | A | 45 min | The current production shape of a coding agent: read files, edit, run commands, use MCP, then verify. Install it on a repo you already know and watch how it searches. |
| [Cursor docs](https://docs.cursor.com) | docs | A | 45 min | The other dominant coding-agent surface: editor-native agent mode, repo indexing, and rules. Use this if your team lives in an IDE rather than a terminal. |
| [GitHub Copilot documentation](https://docs.github.com/en/copilot) | docs | B | 30 min | Still the default enterprise coding assistant. Know what it actually does (completion, chat, agent mode) before arguing about replacing it. |
| [Building effective agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents) | article | A | 40 min | The cleanest split in the field: workflows (you orchestrate) vs agents (the model orchestrates). Read this before you pick a framework. |
| [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) | docs | A | 20 min | Tool use has a standard now. MCP is how coding agents and custom agents attach to files, APIs, and internal systems without a one-off integration each time. |
| [LangGraph memory overview](https://docs.langchain.com/oss/python/concepts/memory) | docs | A | 40 min | Thread vs store, and semantic / episodic / procedural memory. Read this before you buy a "memory" vendor. Pair with the [04.1 memory lab](04.1-backend/memory/README.md). |
| [Hindsight Documentation](https://hindsight.vectorize.io) | docs | A | 20 min | Dedicated AI memory system (retain, recall, reflect, mental models, observations) across sessions/repos with local daemon/Docker support. |

### Intermediate Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | docs | A | 2 hrs | Durable execution, checkpointing, human-in-the-loop, and mixing deterministic steps with model-driven ones. This is the current production orchestration primitive for stateful agents. |
| [AI Agents in LangGraph (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | course | B | 1 hr | Short, hands-on intro to graph-based agents. Useful if the docs feel abstract until you draw a StateGraph. |
| [Anthropic contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) | article | A | 30 min | Why naive chunk-and-embed RAG fails, and the ingestion-time fix (contextual embeddings + BM25) that actually moves retrieval metrics. |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | docs | B | 2 hrs | A thinner agent loop than LangGraph: tools, handoffs, guardrails. Good comparison point so you don't treat one vendor's orchestration model as the only architecture. |
| [LlamaIndex documentation](https://docs.llamaindex.ai) | docs | B | 2 hrs | Strongest open toolkit for ingestion, indexing, and query-time retrieval. Use it when the hard problem is data, not agent choreography. |
| [Ragas](https://docs.ragas.io/en/stable/) | tool | A | 3 hrs | Stops "vibe checks." Faithfulness, context precision/recall, and experiment loops you can run against your own dataset. If you ship RAG without this (or an equivalent), you cannot tell if a change helped. |
| [Promptfoo](https://www.promptfoo.dev) | tool | B | 2 hrs | Prompt and RAG eval in CI. The right shape if you already think in test fixtures and want assertions next to the prompt, not a separate research notebook. |
| [LangSmith](https://docs.smith.langchain.com) | docs | B | 1 hr | Tracing + evaluation for agent runs. You cannot debug a multi-step agent from stdout. Pair with LangGraph if that's your runtime. |

### Advanced Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) | guide | A | 3 hrs | Production engineering for LLM software: own your prompts, own your context window, small focused agents, stateless reducers, compact errors. The closest thing this field has to 12-factor apps. |
| [METR: Changing the developer productivity experiment (Feb 2026)](https://metr.org/blog/2026-02-24-uplift-update/) | study | A | 30 min | The current METR write-up. The early-2025 RCT found a ~19% slowdown; the later sample is noisier and likely understates speedup because people now refuse AI-disallowed tasks. The durable lesson is not a single percentage — it is that perceived speed is not measured speed. |
| [Letta (MemGPT)](https://github.com/letta-ai/letta) | framework | B | 3 hrs | Memory as architecture, not a vector lookup: self-editing context, persistence, and a white-box agent runtime. Read after you understand why chat history is not memory. |
| [Anthropic: Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | article | B | 40 min | How a production agent harness actually splits "brain" from tools, credentials, and sandboxes. Useful even if you never use Anthropic's managed product. |
| [Chip Huyen — AI Engineering](https://huyenchip.com/books/) | book | B | 8–12 hrs | The systems book for this role: evaluation, RAG, agents, and the gap between a notebook and a service. Skim after the foundation post; go deep on the chapters that match what you're shipping. |
| [Langfuse](https://langfuse.com/docs) | tool | C | 2 hrs | Open-source tracing/eval alternative to LangSmith. Relevant if you need self-hosted observability. |
| [CrewAI](https://www.crewai.com/open-source) | framework | C | 2 hrs | Role-based multi-agent orchestration. Interesting for experiments; most production systems should start with a single agent plus tools and add a second agent only when a graph requires it. |

---

## Domain maturity matrices

### AI coding agents

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | GitHub Copilot, Cursor Agent, Claude Code |
| Emerging | Codex-style CLI agents, cloud/background agents, repo-wide agent review in CI |
| Experimental | Fully autonomous ticket-to-merge with no human review |

**Key references:** [Claude Code overview](https://code.claude.com/docs/en/overview), [METR Feb 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)

### Production RAG

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Hybrid search (lexical + vector), reranking, pgvector / managed vector DBs, citation-backed answers |
| Emerging | Contextual retrieval, agentic RAG (retrieve → critique → retrieve again) |
| Experimental | Self-improving indexes with no human-labeled eval set |

**Key references:** [Anthropic contextual retrieval](https://www.anthropic.com/news/contextual-retrieval), [Ragas](https://docs.ragas.io/en/stable/)

### Tool use and MCP

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Native function/tool calling, MCP clients in Claude Code / Cursor / VS Code |
| Emerging | Internal MCP servers for company systems, skills / progressive disclosure |
| Experimental | Unrestricted production-system tool access with no allowlist or approval gate |

**Key references:** [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro), [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

### Agent memory

The backend lab is [04.1](04.1-backend/README.md) — Academy modules 2 and 5 plus the [memory systems map](04.1-backend/memory/README.md). Chat history is not a memory system.

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Thread state + checkpointers; LangGraph Store for cross-thread facts; explicit working-memory trim/summarize |
| Emerging | LangMem, Hindsight, Letta, Zep (temporal), Trustcall-style collection updates |
| Experimental | Autonomous lifelong memory with no curation, expiry, or conflict resolution |

**Key references:** [LangGraph memory overview](https://docs.langchain.com/oss/python/concepts/memory), [Hindsight Documentation](https://hindsight.vectorize.io), [memory systems lab](04.1-backend/memory/README.md)

### Evaluation and AI-native architecture

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Golden datasets, tracing, prompt/RAG tests in CI (Promptfoo, Ragas, LangSmith) |
| Emerging | LLM-as-judge in the developer loop, 12-factor agent patterns, human-in-the-loop graphs |
| Experimental | Agents as a first-class runtime with no eval gate and no human confirmation on side effects |

**Key references:** [12-Factor Agents](https://github.com/humanlayer/12-factor-agents), [Ragas](https://docs.ragas.io/en/stable/)

---

## Where to Start (and What to Skip)

### This Week (1–2 hours)

- **Install one coding agent on a repo you already own.** [Claude Code](https://code.claude.com/docs/en/overview) if you live in the terminal; [Cursor](https://docs.cursor.com) if you live in the editor. Give it a real bug or a small refactor, then review the diff as if a new teammate wrote it. The skill is review, not generation.
- **Read Building effective agents.** Forty minutes with [Anthropic's essay](https://www.anthropic.com/engineering/building-effective-agents) will stop you from reaching for a multi-agent framework when a single tool-using loop would do.

### This Month (10–15 hours)

- **Build a tiny RAG system against your own docs, then evaluate it.** Use [LlamaIndex](https://docs.llamaindex.ai) or a raw vector store plus hybrid search. Before you add agents, run [Ragas](https://docs.ragas.io/en/stable/) (or Promptfoo) on 20–50 real questions. If you cannot measure faithfulness, you are not ready to put it behind an API.
- **Connect one MCP server to your coding agent.** Follow the [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) and attach something you already use (repo search, issue tracker, internal docs). The point is to feel tool use as an interface, not a library.
- **Read 12-Factor Agents.** Work through [the factors](https://github.com/humanlayer/12-factor-agents) and mark which ones your current prototype already violates. Own-your-prompts and small-focused-agents are the usual first failures.
- **Separate thread memory from long-term memory.** Run [`thread_vs_store.py`](04.1-backend/memory/thread_vs_store.py), then Academy module-5. If a fact should survive a new chat, it does not belong only in the checkpointer.

### This Quarter (ongoing)

- **Ship one agentic workflow with a human gate.** Using [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) (or the OpenAI Agents SDK if you want a thinner loop), persist state, add a tool, and require approval before any write to production systems. Scope it to a non-critical path first.
- **Put evals in CI.** A prompt change or retrieval tweak that is not scored against a frozen dataset is a vibe. Treat evaluation datasets the way you already treat unit tests.

### What to Skip

- **Multi-agent frameworks as the first architecture.** Crews, swarms, and role-playing agents hide the actual loop. Start with one model, typed tools, and explicit state. Add a second agent when a graph requires a hard boundary, not because a tutorial had four personas.
- **Fine-tuning to "make the model know your codebase."** RAG, rules files (`CLAUDE.md`, Cursor rules), and evals cover almost every product case. Fine-tuning is a platform/ML problem unless you have measured a retrieval/prompting ceiling.
- **Treating coding-agent output as reviewed code.** [METR](https://metr.org/blog/2026-02-24-uplift-update/) is the warning: perceived speed is not measured speed, and unreviewed agent diffs are unreviewed diffs. Keep the PR, the tests, and the human.
- **Unbounded tools against production.** A coding agent with shell and MCP is powerful because it can act. That is also why [the Security landscape](../03-security/README.md) exists. Allowlists, sandboxes, and approval gates are part of the developer architecture, not a later hardening pass.
- **Chat history as long-term memory.** Logs are not a memory system. If the agent must remember users, decisions, or facts across sessions, design storage, conflict resolution, and expiry on purpose.

---

*This is Part 4 of the [AI Role Upgrade Roadmap series](../README.md). Each post maps the AI landscape for a specific software role. What matters, what doesn't, and where to invest your time.*

*Series: [Pillar](../00-pillar/) | [Foundation](../01-foundation/) | [DevOps](../02-devops/) | [Security](../03-security/) | **Developer** | Product | App Eng | Platform | Data | QA | Leaders*

---

*Neeraj Singh is a Staff Security Infrastructure Engineer with 15+ years of experience at Meta, Wayfair, JPMorgan Chase, and Parafin. He writes about AI and infrastructure: what works in production, not what works in demos.*


## Labs

Hands-on examples live in [`labs/`](labs/).

- **[04.1 Backend](04.1-backend/README.md)** — [LangChain Academy](https://github.com/langchain-ai/langchain-academy) LangGraph modules, installed from the root `pyproject.toml`, plus a dedicated [memory systems](04.1-backend/memory/README.md) track (checkpointer vs store, semantic/episodic/procedural, Hindsight/Letta/Zep).
