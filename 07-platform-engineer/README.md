# Part 7: The Platform Engineer's AI Landscape: Infrastructure, Serving, and Cost Reality

> A curated map of model serving, GPU infrastructure, vector DBs, feature stores, developer experience, and cost management — graded by maturity, annotated by a practitioner

**Read the full article:** https://neerazz.hashnode.dev/platform-engineer-ai-landscape-infrastructure-serving-cost

---

## The Curated Resources

### Grading Key
- **Grade A (Essential):** Skip this and you'll have a real gap in your AI platform engineering capabilities.
- **Grade B (Highly Recommended):** Adds meaningful depth. Worth it for anyone serious about building AI infrastructure.
- **Grade C (Useful for Depth):** Only if you're going deep in a specific sub-domain.

### Beginner Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart.html) | docs | **A** | 1–2 hrs | The most popular open-source LLM serving engine. Covers installation, batched inference, and OpenAI-compatible API in one walkthrough. Start here for model serving. |
| [Feast Quickstart](https://docs.feast.dev/getting-started/quickstart) | docs | **A** | 1–2 hrs | Open-source feature store with the lowest barrier to entry. Repository setup, feature definition, materialization, and point-in-time joins in under two hours. |
| [FinOps for AI Overview](https://www.finops.org/wg/finops-for-ai-overview/) | framework | **A** | 20 min | The FinOps Foundation's working group overview — 98% of respondents now manage AI spend. Required context before making any GPU procurement decisions. |
| [Best Vector Databases in 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases) | article | **B** | 20 min | Accessible overview of the vector database landscape with practical selection criteria. Good starting point before diving into benchmarks. |
| [BentoML Getting Started](https://docs.bentoml.com/en/latest/get-started/hello-world.html) | docs | **B** | 2–3 hrs | ML model serving framework with adaptive batching, model composition, and BentoCloud managed option. Good complement to vLLM for non-LLM models. |
| [Modal Pricing](https://modal.com/pricing) | docs | **B** | 10 min | Per-second GPU billing with no idle charges. Understanding Modal's pricing model reframes how you think about GPU cost structures. |
| [Backstage: Why Build Plugins](https://backstage.io/docs/next/golden-path/plugins/why-build-plugins/) | docs | **B** | 15 min | The rationale for Backstage plugins — centralized tool access, reduced context-switching, modular architecture. Read before building AI golden paths. |

### Intermediate Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [State of AI in Platform Engineering 2025](https://platformengineering.org/reports/state-of-ai-in-platform-engineering-2025) | report | **A** | 45 min | The flagship report on AI + platform engineering: 59% face skill gaps, 88% use AI daily, two-track approach (AI for IDPs + Platforms for AI). Frames the entire domain. |
| [pgvector Performance & Optimization 2025](https://zylos.ai/research/pgvector-optimization-2025) | article | **A** | 25 min | Benchmarks showing pgvector with HNSW indexes at 15x faster than IVFFlat, 75% cost savings vs managed solutions for sub-50M vectors. The data behind the "pgvector is underrated" claim. |
| [BentoML: Benchmarking LLM Inference Backends](https://www.bentoml.com/blog/benchmarking-llm-inference-backends) | article | **A** | 30 min | Hands-on benchmarks of vLLM, LMDeploy, TGI, TensorRT-LLM across Llama 3 on A100 GPUs. The most useful comparison I found for model serving tool selection. |
| [Databricks Feature Store with Unity Catalog](https://docs.databricks.com/en/machine-learning/feature-store/index.html) | docs | **B** | 2–3 hrs | Any Delta table with a primary key auto-becomes a feature table. Worth understanding even if you're not on Databricks — the pattern of lakehouse-integrated features is spreading. |
| [AWS: Cost Optimizing AI Workloads](https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws) | article | **B** | 25 min | GPU cost optimization strategies from the largest cloud provider. Spot Instances (up to 90% savings), Savings Plans, and custom silicon options. |
| [Kubecost GPU Monitoring (v2.4)](https://blog.kubecost.com/blog/gpu-monitoring/) | article | **B** | 20 min | GPU-specific cost monitoring with per-workload allocation. If you run GPU workloads on Kubernetes and don't have this, you're flying blind on cost. |
| [Pinecone vs Weaviate vs Qdrant 2026](https://brlikhon.engineer/blog/pinecone-vs-weaviate-vs-qdrant-vector-database-wars-2026) | article | **B** | 25 min | P95 latency data, throughput benchmarks, and pricing analysis for the three purpose-built leaders. Essential for teams that have outgrown pgvector. |
| [Humanitec Platform Orchestrator v2](https://humanitec.com/blog/the-all-new-platform-orchestrator) | article | **B** | 20 min | AI-first platform redesign with brownfield compatibility. Worth evaluating if your IDP needs a graph-based orchestration backend. |

### Advanced Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [CNCF 2025 Cloud Native Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/) | report | **A** | 30 min | K8s at 82% production adoption, 44% don't run AI/ML on it, only 7% deploy models daily. Best data source for understanding where the industry actually stands vs where the marketing claims it stands. |
| [Comparative Analysis of vLLM and TGI (arXiv)](https://arxiv.org/abs/2511.17593) | paper | **B** | 1–2 hrs | Academic benchmark demonstrating vLLM's 24x throughput advantage under high concurrency. The data behind the "vLLM wins on throughput" consensus. |
| [Vector Database Benchmark 2026](https://www.salttechno.ai/datasets/vector-database-performance-benchmark-2026/) | article | **B** | 30 min | Standardized benchmark across 10 vector databases on 1M vectors/1536 dimensions. Closest you'll get to an apples-to-apples vector DB comparison. |
| [FinOps for AI Framework](https://www.finops.org/framework/scope/finops-for-ai/) | framework | **B** | 30 min | The official FinOps framework scope for AI workloads — governance, visibility, and value quantification. The structure for building your organization's AI cost management practice. |
| [Infracost FinOps Policies](https://infracost.io/docs/infracost_cloud/finops_policies) | docs | **C** | 30 min | 70+ AWS/Azure/GCP best practice policies that identify cost issues in pull requests. Useful for teams building IaC-level cost guardrails into their platform. |

---


## Where to Start (and What to Skip)

### This Week (2–3 hours)

- **Deploy a model with vLLM.** Follow the [quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart.html), spin up an OpenAI-compatible API server with an open-source model, and send it requests. The entire loop — install, deploy, query — takes under an hour. You'll understand the model serving abstraction better from 45 minutes of hands-on work than from reading five comparison articles.
- **Evaluate pgvector against your requirements.** If your team is discussing vector database options, spend an hour reading the [pgvector optimization benchmarks](https://zylos.ai/research/pgvector-optimization-2025) and the [2026 vector database benchmark](https://www.salttechno.ai/datasets/vector-database-performance-benchmark-2026/). For datasets under 50M vectors, pgvector on your existing Postgres infrastructure may eliminate the need for a new managed service entirely.

### This Month (10–15 hours)

- **Build a golden path template for AI projects.** Using [Backstage golden paths](https://backstage.io/docs/next/golden-path/plugins/backend/meta) or your existing IDP scaffolding, create a template that provisions: a vLLM deployment, a pgvector-enabled database, basic monitoring, and a cost budget alert. The template doesn't need to be perfect — the existence of a self-service starting point changes the conversation from "file an infra ticket" to "click and start."
- **Set up GPU cost monitoring.** Deploy [Kubecost](https://blog.kubecost.com/blog/gpu-monitoring/) on one cluster and configure [Infracost](https://www.infracost.io/glossary/ai-workload-cost-management/) on one IaC repository. Establish baseline visibility into what GPU workloads actually cost before the bill becomes a problem.
- **Read the State of AI in Platform Engineering report.** The [full 2025 report](https://platformengineering.org/reports/state-of-ai-in-platform-engineering-2025) takes 45 minutes and gives you the industry context to position AI platform work internally. The skill gap data (59% report gaps) is useful for justifying team investment.

### This Quarter (ongoing)

- **Build the full AI platform layer.** Model serving (vLLM behind an internal API gateway), vector storage (pgvector as default, migration path to purpose-built when needed), feature store (Feast for experimentation, Tecton or Databricks for production), evaluation infrastructure, and cost controls (Infracost + Kubecost + budget alerts). Each component is a discrete project; the platform value emerges when they're integrated and self-service.
- **Establish FinOps practices for AI workloads.** Work through the [FinOps for AI framework](https://www.finops.org/framework/scope/finops-for-ai/) and implement governance, visibility, and cost allocation specific to GPU compute. This means chargeback dashboards, budget alerts per team, and cost estimates in the deployment pipeline.

### What to Skip

- **Building custom model serving infrastructure.** vLLM and Triton exist. They handle continuous batching, PagedAttention, and GPU memory management better than anything you'll build in-house. Custom serving makes sense only for exotic model architectures or latency requirements that benchmarked tools can't meet — which is vanishingly rare.
- **Over-engineering vector DB selection for small datasets.** If your largest collection is under 10M vectors, the difference between Pinecone and pgvector is operational overhead, not performance. Start with pgvector. Migrate when you have the data volume that justifies the additional service.
- **Ignoring GPU costs until the bill arrives.** GPU instances cost 5–20x more per hour than equivalent CPU instances. A single misconfigured autoscaler or forgotten training job can cost more in a weekend than your entire monthly compute budget. Cost monitoring is not a phase-two optimization — it's a deployment prerequisite.
- **Deploying TGI for new projects.** TGI entered [maintenance mode in December 2025](https://huggingface.co/docs/text-generation-inference/quicktour). Hugging Face themselves recommend vLLM or SGLang for new deployments. Don't start a project on a platform the maintainers have moved on from.
- **Treating feature stores as a first priority.** If your organization doesn't have ML models in production yet, a feature store is premature infrastructure. Get model serving working first. Feature stores solve training-serving skew — a problem that only exists once you have both training pipelines and serving endpoints running against the same features.

---

*This is Part 7 of the [AI Role Upgrade Roadmap series](#). Each post maps the AI landscape for a specific software role — what matters, what doesn't, and where to invest your time.*

*Series: [Pillar](#) | [Foundation](#) | [DevOps](#) | [Security](#) | [Developer](#) | [Product](#) | [App Eng](#) | **Platform** | [Data](#) | [QA](#) | [Leaders](#)*

---

*[Neeraj Kumar](https://www.linkedin.com/in/neerajkumarsinghb/) is a Staff Security Infrastructure Engineer at Parafin with 15+ years across Meta, Wayfair, and JPMorgan Chase. He builds security infrastructure for an $8B+ fintech platform and writes about the intersection of AI, infrastructure, and practical platform engineering — what works in production, not what works in keynotes.*


## Labs

Hands-on examples for this part live in [`labs/`](labs/). (Coming soon — open an issue if you want a specific one first.)
