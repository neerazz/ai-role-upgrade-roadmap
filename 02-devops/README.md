# Part 2: The DevOps Engineer's AI Landscape: AIOps, Self-Healing, and What's Actually Production-Ready

> A curated map of AI tools, platforms, and frameworks transforming DevOps — graded by maturity, annotated by a practitioner

**Read the article:** [Hashnode (canonical)](https://neerazz.hashnode.dev/the-devops-engineer-s-ai-landscape-aiops-self-healing-and-what-s-actually-production-ready) · [dev.to](https://dev.to/neerazz/the-devops-engineers-ai-landscape-aiops-self-healing-and-whats-actually-production-ready-285c)

---

## The Curated Resources

### Grading Key
- **Grade A (Essential):** Skip this and you'll have a real blind spot in AI for DevOps.
- **Grade B (Highly Recommended):** Adds real depth. Worth it if you're serious about this space.
- **Grade C (Useful for Depth):** Only if you're going deep in a specific sub-domain.

### Beginner Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [What is AIOps?](https://datadoghq.com/knowledge-center/aiops) | article | A | 15 min | Clear, vendor-neutral-ish explanation of AIOps concepts. Solid starting point for anyone who hasn't formalized their mental model of where AI fits in monitoring. |
| [AI Observability vs Traditional Monitoring](https://insightfinder.com/blog/ai-observability-vs-traditional-monitoring/) | article | B | 20 min | Useful framing of what AI-based monitoring actually changes versus traditional threshold alerting. Good for calibrating expectations before evaluating tools. |
| [FinOps for AI Overview](https://www.finops.org/wg/finops-for-ai-overview/) | framework | A | 30 min | The FinOps Foundation's working group framework for AI cost management. Required reading for any DevOps team running GPU workloads or managing AI infrastructure budgets. |
| [Shoreline.io Documentation](https://docs.shoreline.io/what-is-shoreline) | docs | B | 30 min | Well-documented auto-remediation platform. Even if you don't adopt it, the architecture patterns for fleet-wide self-healing are worth studying. |

### Intermediate Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [Datadog Bits AI Documentation](https://docs.datadoghq.com/bits_ai) | docs | A | 1 hr | If you run Datadog, this is table stakes. SRE, Developer, and Security agents for natural-language incident investigation and code-level analysis. |
| [Dynatrace Davis AI Platform](https://www.dynatrace.com/platform/artificial-intelligence/) | docs | A | 1 hr | Hypermodal AI combining predictive, causal, and generative AI. The causal root cause analysis is the differentiator worth understanding even if you're on a different platform. |
| [Terraform MCP Server](https://developer.hashicorp.com/terraform/mcp-server/deploy) | tool | A | 2 hrs | MCP integration that connects AI agents to Terraform Registry documentation, provider schemas, and module search. Hands-on setup is straightforward. |
| [Kubernetes Self-Healing AI Operators](https://markaicode.com/kubernetes-self-healing-ai-operators-2025/) | guide | B | 45 min | Practical walkthrough of AI-enhanced K8s operators. Take the 87% downtime reduction claim with appropriate skepticism, but the patterns are sound. |
| [Infracost](https://www.infracost.io/) | tool | A | 2 hrs | Cloud cost estimates directly in PRs, used by 3,000+ companies. The PR-level cost visibility alone changes how teams think about infrastructure changes. |
| [FinOps Foundation State of FinOps 2025](https://data.finops.org/2025-report/) | report | B | 1 hr | The definitive industry report on cloud spend management. The AI adoption data (63% using AI for cost management, doubled YoY) gives you benchmarks for where your org stands. |
| [Pulumi 2025 Product Launches](https://www.pulumi.com/blog/2025-product-launches/) | article | B | 30 min | Overview of Pulumi AI, Neo, and the copilot ecosystem. Worth reading for the direction IaC is heading, especially if you're evaluating alternatives to Terraform. |
| [Docker MCP Server](https://docker.com/blog/build-to-prod-mcp-servers-with-docker) | article | B | 30 min | MCP integration for container lifecycle. Early but well-documented pattern for AI-assisted container operations. |

### Advanced Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [Kelsey Hightower: Beyond the Hype](https://civo.com/navigate/san-francisco/2025/talks/kelsey-hightower-beyond-the-hype-video) | talk | A | 45 min | Kelsey cuts through the noise on what AI tools actually deliver versus what the keynotes promise. The best vendor-free reality check I've found. |
| [Kelsey Hightower on LLMs in the Enterprise](https://www.union.ai/blog-post/dollars-to-data-kelsey-hightower-talks-llms-in-the-enterprise) | interview | B | 30 min | Practical perspective on LLM integration costs, enterprise readiness, and where the real value sits for infrastructure teams. |
| [LangGraph Platform GA](https://blog.langchain.com/langgraph-platform-ga) | article | B | 45 min | Durable execution for AI agents with failure recovery. If you're building multi-agent operational workflows, this is the current production-grade option. |
| [CrewAI Open Source](https://www.crewai.com/open-source) | framework | B | 3 hrs | Multi-agent orchestration framework for building coordinated AI workflows. The role-based agent design maps naturally to DevOps team structures. |
| [Gartner Peer Insights: AIOps Platforms](https://www.gartner.com/reviews/market/aiops-platforms) | reviews | C | 1 hr | Enterprise peer reviews across AIOps vendors. Most useful for building a vendor evaluation shortlist or validating your current platform choice. |
| [Infracost AI for FinOps](https://www.infracost.io/blog/ai-for-finops-fix-cloud-cost-issues-faster/) | case study | C | 20 min | Detailed case study on AI-accelerated cost optimization. The "300 issues fixed in 2 weeks" number is from a single customer, but the workflow patterns generalize. |

---


## Where to Start (and What to Skip)

### This Week (1–2 hours)

- **Explore your existing platform's AI features.** If you're on Datadog, walk through [Bits AI](https://docs.datadoghq.com/bits_ai). try a natural-language incident investigation on a recent alert. If you're on Dynatrace, explore [Davis AI](https://www.dynatrace.com/platform/artificial-intelligence/) causal analysis on a recent root cause analysis. Most teams are paying for AI capabilities they haven't activated.
- **Read the FinOps for AI overview.** 30 minutes with the [FinOps for AI working group framework](https://www.finops.org/wg/finops-for-ai-overview/) will reframe how you think about GPU and inference costs. Especially relevant if your team is provisioning AI workloads and applying CPU-era cost assumptions.

### This Month (10–15 hours)

- **Set up the Terraform MCP server.** Follow the [deployment guide](https://developer.hashicorp.com/terraform/mcp-server/deploy), connect it to your editor's AI agent, and use it for a week of normal IaC work. You'll know within a few days whether it fits your workflow.
- **Configure anomaly detection on 3 key metrics.** Pick your three highest-signal SLI metrics and set up AI-based anomaly detection (available in Datadog, Dynatrace, and New Relic). Compare the alert quality against your existing static thresholds over 30 days.
- **Read through the Kelsey Hightower materials.** [Beyond the Hype](https://civo.com/navigate/san-francisco/2025/talks/kelsey-hightower-beyond-the-hype-video) and [LLMs in the Enterprise](https://www.union.ai/blog-post/dollars-to-data-kelsey-hightower-talks-llms-in-the-enterprise) are the best available calibration on where AI tools deliver real value versus where the industry is still figuring things out.
- **Set up Infracost on one repository.** [Infracost](https://www.infracost.io/) in a CI pipeline takes under an hour and gives immediate visibility into cost impact of infrastructure PRs. Start with one repo, evaluate for a sprint, then decide on wider rollout.

### This Quarter (ongoing)

- **Build a multi-agent ops workflow.** Using either [CrewAI](https://www.crewai.com/open-source) or [LangGraph](https://blog.langchain.com/langgraph-platform-ga), build a coordinated agent workflow for a specific operational task: incident triage, deployment validation, or cost anomaly investigation. Start with two agents and a human-in-the-loop approval gate. Scope it to a non-critical service first.
- **Evaluate AIOps platform capabilities end-to-end.** Run a 90-day evaluation of your monitoring platform's AI features across detection, correlation, and suggested remediation. Document what works and where human judgment is still required. This becomes your team's internal playbook for AI-assisted operations.

### What to Skip

- **Building custom AIOps from scratch.** Your monitoring platform already has AI features. Most teams haven't fully activated what they're paying for. Evaluate platform capabilities before building bespoke ML pipelines for anomaly detection. The platforms have more training data than you do.
- **Kubernetes AI operators without solid baseline automation.** If your liveness probes, readiness checks, and HPA configurations aren't dialed in, an AI operator will inherit your reliability debt, not fix it. Get the fundamentals right first.
- **AI-powered CI/CD before having reliable CI/CD.** AI can optimize a working pipeline. It can't fix a broken one. If your CI/CD is flaky or non-deterministic, adding AI optimization on top creates a more complex version of the same problem. Fix the foundation, then optimize.
- **Autonomous remediation without approval gates.** The marketing says "self-healing." Production reality says "self-healing with a human confirming the heal." Skip any tool that doesn't support explicit approval workflows for remediation actions. The constraint is trust: the risk/reward math on autonomous production changes doesn't work yet.

---

*This is Part 2 of the [AI Role Upgrade Roadmap series](https://neerazz.hashnode.dev/stop-learning-ai-start-upgrading-your-role-a-guide-for-every-software-discipline). Each post maps the AI landscape for a specific software role. What matters, what doesn't, and where to invest your time.*

*Series: [Pillar](https://neerazz.hashnode.dev/stop-learning-ai-start-upgrading-your-role-a-guide-for-every-software-discipline) | [Foundation](https://neerazz.hashnode.dev/ai-foundation-every-engineer-needs) | **DevOps** | Security (coming soon) | Developer | Product | App Eng | Platform | Data | QA | Leaders*

---

*Neeraj is a Staff Security Infrastructure Engineer at a fintech company with 15+ years across Meta, Wayfair, and JPMorgan Chase. He writes about AI and infrastructure: what works in production, not what works in demos.*


## Labs

Hands-on examples for this part live in [`labs/`](labs/). (Coming soon — open an issue if you want a specific one first.)
