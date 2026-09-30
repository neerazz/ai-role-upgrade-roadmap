# AI Role Upgrade Roadmap — Companion Repo

Code, curated resources, and infographic prompts for the
**AI Role Upgrade Roadmap** blog series: role-specific maps for how AI is
changing every software discipline — with graded resources and honest
assessments instead of hype.

## Why This Roadmap Exists

I kept trying to learn AI engineering by following the vocabulary: prompting,
embeddings, RAG, agents, vector databases, orchestration, MCP, memory, and then
the next framework that appeared. The more material I collected, the less clear
the path became.

The problem was not a shortage of courses or tools. It was that the market mixes
three different things into one feed:

1. **Foundations** that transfer across tools.
2. **Role-specific engineering work** that depends on what you actually build.
3. **Framework choices** that should come last, after the problem is clear.

This repository separates them. Learn the shared foundation once, choose the
role closest to your work, and use frameworks only when their trade-offs solve a
problem you can name. It is a learning path, not a weekly buzzword checklist.

## The Complete Roadmap

The roadmap has one shared foundation followed by nine role-specific upgrades. Start
with Part 1, then jump to the role closest to the work you do or the role you want
next.

| # | Module | For whom | What it covers | Status |
|---|--------|----------|----------------|--------|
| 0 | [The Role Upgrade Map](00-pillar/README.md) | Everyone | Why a single "learn AI" roadmap fails, how the landscape splits by engineering role, and how to choose the path with the highest value for your work. | [Hashnode](https://neerazz.hashnode.dev/stop-learning-ai-start-upgrading-your-role-a-guide-for-every-software-discipline) · [dev.to](https://dev.to/neerazz/stop-learning-ai-start-upgrading-your-role-a-guide-for-every-software-discipline-4pkm) · [Medium](https://neerazz.medium.com/stop-learning-ai-start-upgrading-your-role-b8e87fd48061) |
| 1 | [The AI Foundation Every Engineer Needs](01-foundation/README.md) | All engineers | The shared vocabulary behind the rest of the series: transformers, embeddings, prompting, RAG, agents, evaluation, and the topics most engineers can safely skip. | [Hashnode](https://neerazz.hashnode.dev/the-ai-foundation-every-engineer-needs-and-what-to-skip) · [dev.to](https://dev.to/neerazz/the-ai-foundation-every-engineer-needs-and-what-to-skip-3njl) · [Medium](https://neerazz.medium.com/the-ai-foundation-every-engineer-needs-and-what-to-skip-8c70be966f25) |
| 2 | [The DevOps Engineer's AI Landscape](02-devops/README.md) | DevOps engineers and SREs | AIOps, anomaly detection, root-cause analysis, self-healing infrastructure, LLM-assisted IaC, agentic operations, and FinOps for AI workloads. | [Hashnode](https://neerazz.hashnode.dev/the-devops-engineer-s-ai-landscape-aiops-self-healing-and-what-s-actually-production-ready) · [dev.to](https://dev.to/neerazz/the-devops-engineers-ai-landscape-aiops-self-healing-and-whats-actually-production-ready-285c) · [LinkedIn](https://www.linkedin.com/feed/update/urn:li:share:7452544753876762625/) |
| 3 | [The Security Engineer's AI Landscape](03-security/README.md) | Security engineers and AppSec teams | Defending AI systems against prompt injection, model poisoning, adversarial attacks, and supply-chain risk; using AI in security operations; and governing AI deployments. | Resource shelf started; article drafted, not yet published |
| 4 | [The Application Developer's AI Learning Roadmap](04-developer/README.md) | Backend, frontend, and full-stack developers | One shared AI foundation, then separate backend and frontend paths for building reliable AI features end to end. | [Published article](https://neerazz.hashnode.dev/i-followed-the-vocabulary-instead-of-the-work) · [04.1 backend labs](04-developer/04.1-backend/README.md) · [04.2 frontend learning path](04-developer/04.2-frontend/README.md) |
| 5 | The Product Engineer's AI Landscape | Product engineers | Product evaluation for non-deterministic output, LLM-as-judge, human-in-the-loop scoring, trust and safety, AI product metrics, and learning what users will actually pay for. | Planned — module details to be added |
| 6 | The Application Integration Engineer's AI Landscape | Enterprise application engineers and integrators | Adding AI to existing systems through gateways, middleware, caching, routing, fallbacks, observability, and migrations that contain probabilistic failure. Unlike Part 4, this track is about integration ownership rather than building the product experience itself. | Planned — module details to be added |
| 7 | The Platform Engineer's AI Landscape | Platform and ML infrastructure engineers | Model serving, GPU infrastructure, inference reliability, workload scheduling, quantization, intelligent model routing, developer platforms, and cost control at scale. | Planned — module details to be added |
| 8 | The Data Engineer's AI Landscape | Data and analytics engineers | The data infrastructure AI depends on: feature stores, vector databases, RAG ingestion, embedding pipelines, lineage, data quality, and monitoring for drift. | Planned — module details to be added |
| 9 | The QA/SDET's AI Landscape | QA engineers, SDETs, and test leads | Testing systems whose output changes on every run through evaluation datasets, statistical thresholds, LLM-as-judge pipelines, prompt regression tests, and adversarial testing. | Planned — module details to be added |
| 10 | Engineering Leaders: The AI Team Upgrade | Engineering managers, directors, VPs, and CTOs | Team readiness, centralized versus embedded AI ownership, build-versus-buy decisions, governance, skills planning, operating-model changes, and measuring ROI beyond shipping a chatbot. | Planned — module details to be added |

Parts 5–10 are deliberate placeholders. Their scope is fixed here; the detailed
resource lists, maturity assessments, labs, and weekly/monthly/quarterly plans will
be added one module at a time.


## What's Here

- **`README.md`** — the complete 11-part map and the scope of every module.
- **`pyproject.toml`** — Python dependencies for Part 4 labs (LangChain Academy stack; `uv sync --extra memory` for LangMem/Hindsight).
- **`<part>/README.md`** — the detailed, graded resource list for modules that
  have been started, plus a "where to start" plan where available.
- **`<part>/labs/`** — runnable examples referenced from published articles.
- **`04-developer/04.1-backend/`** — backend track: APIs, retrieval, tools, agents, memory, evaluation, and reliability.
- **`04-developer/04.2-frontend/`** — frontend track: streaming UI, state, trust, approval, accessibility, and failure recovery.
- **`assets/prompts/`** — the infographic-generation prompts used to create
  each article's landscape map (reusable for your own diagrams).

## License

Resource lists and prompts: CC BY 4.0. Code in `labs/`: MIT.
