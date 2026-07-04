# Part 3: The Security Engineer's AI Landscape: Threats, Defenses, and the Tools That Matter

> A practitioner's map of AI-powered security — from threat detection to governance — with graded resources and honest assessments

**Read the full article:** https://neerazz.hashnode.dev/security-engineer-ai-landscape-threats-defenses-tools

---

## The Curated Resources

### Grading Key
- **Grade A (Essential):** Skip this and you'll have a real blind spot in your AI security knowledge.
- **Grade B (Highly Recommended):** Worth the time if you're serious about this domain.
- **Grade C (Useful for Depth):** Only if you're going deep in a specific sub-domain.

### Beginner Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) | guide | A | 2 hrs | The baseline vulnerability taxonomy for LLM security. Read this before anything else. Community-vetted by 600+ experts. |
| [Google SAIF Self-Assessment](https://www.saif.google/why-saif) | framework | A | 3 hrs | Structured risk assessment you can run against your own AI deployments. Practical from day one. |
| [CISA AI Cybersecurity Playbook](https://www.cisa.gov/resources-tools/resources/ai-cybersecurity-collaboration-playbook) | playbook | B | 2 hrs | Government-backed guidance. Useful for regulated industries and as a conversation starter with compliance teams. |
| [MITRE ATLAS](https://atlas.mitre.org/) | framework | A | 3 hrs | If you know ATT&CK, ATLAS is the ML extension. Real-world adversarial tactics, not theoretical exercises. |
| [UK NCSC AI Cyber Security Code](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice) | guidance | B | 1.5 hrs | More prescriptive than NIST or SAIF. Good for building concrete policy requirements. |

### Intermediate Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [NVIDIA garak](https://github.com/NVIDIA/garak) | tool | A | 4 hrs setup + ongoing | Hands-on LLM vulnerability scanning. Install it, point it at a model, and see what breaks. Learning-by-doing beats reading about prompt injection. |
| [Microsoft PyRIT](https://github.com/Azure/PyRIT) | tool | B | 3 hrs setup + ongoing | Complements garak with a more modular, pipeline-oriented red teaming approach. Better for teams that need repeatable, automated test suites. |
| [NIST AI Risk Management Framework](https://nist.gov/itl/ai-risk-management-framework) | framework | A | 4 hrs | The governance baseline. Even if you never implement it fully, understanding its four functions (Govern, Map, Measure, Manage) shapes how you think about AI risk. |
| [SANS SEC598: Security Automation and AI](https://www.sans.org/cyber-security-courses/ai-security-automation) | course | B | 5 days | Hands-on SANS training for integrating AI into security operations. The lab exercises are worth the tuition if your employer is paying. |
| [Simon Willison: Prompt Injection Attacks on AI Systems](https://simonwillison.net/2025/Jan/29/prompt-injection-attacks-on-ai-systems) | blog | A | 1 hr | The single best explanation of why prompt injection is fundamentally unsolved. Changes how you think about LLM application boundaries. |
| [Trail of Bits: Prompt Injection to RCE](https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/) | research | A | 1.5 hrs | Demonstrates real attack chains from prompt injection to code execution. Required reading for anyone reviewing AI agent architectures. |
| [NIST to ISO 42001 Crosswalk](https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf) | mapping | B | 2 hrs | Saves weeks of manual mapping if you need both frameworks. |

### Advanced Resources

| Resource | Type | Grade | Time | Why It's Here |
|----------|------|-------|------|---------------|
| [SANS SEC545: GenAI & LLM Application Security](https://www.sans.org/cyber-security-courses/genai-llm-application-security-5day) | course | B | 5 days | Deep technical training on LLM application security. More specialized than SEC598 — take this after you've already built some intuition from the beginner/intermediate resources. |
| [Anthropic: Tracing Thoughts in Language Models](https://www.anthropic.com/research/tracing-thoughts-language-model) | research | B | 2 hrs | Interpretability research with long-term security implications. Understanding model internals changes how you think about monitoring and detection. |
| [Black Hat / DEF CON 2025 AI Security Recap](https://wwt.com/blog/the-ai-security-crossroads-black-hat-and-defcon-2025-show-whats-next) | recap | B | 1 hr | Concentrated summary of the latest offensive AI research and defense techniques from the security community's flagship conferences. |
| [OpenSSF Model Signing v1.0](https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain) | spec | C | 2 hrs | Deep cut for supply chain security specialists. Read if you're building model provenance controls. |
| [ML Supply Chain Attack Analysis (arXiv)](https://www.arxiv.org/abs/2502.04484) | paper | C | 3 hrs | Academic depth on ML supply chain threats. Pair with the OpenSSF model signing work for a complete picture. |
| [EU AI Act + ISO + NIST Integration](https://cloudsecurityalliance.org/blog/2025/01/29/how-can-iso-iec-42001-nist-ai-rmf-help-comply-with-the-eu-ai-act) | guide | C | 2 hrs | Only relevant if your organization operates in the EU or sells to EU customers. Dense but saves significant compliance mapping effort. |
| [AI Security Vendor Scorecard](https://www.aegisintel.ai/post/signal-vs-noise-the-cio-scorecard-for-ai-security-vendor-evaluation-for-2025) | framework | C | 1 hr | Procurement-focused. Useful when evaluating vendor AI claims — helps cut through marketing noise. |

---


## Where to Start (and What to Skip)

### This Week (2-3 hours)

- **Read:** The [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/). Read it cover to cover, not just the titles. Pay attention to LLM01 (Prompt Injection) and LLM02 (Insecure Output Handling). These are the ones you'll see in production.
- **Install and run:** [NVIDIA garak](https://github.com/NVIDIA/garak) against one model. Doesn't matter if it's a local model or an API endpoint you control. The point is to see what automated LLM vulnerability scanning looks like and what it finds. Thirty minutes of running garak teaches more than three hours of reading about prompt injection.

### This Month (10-15 hours)

1. Deep dive into [MITRE ATLAS](https://atlas.mitre.org/). map the tactics and techniques to your organization's AI deployments. Even if you have zero ML models in production, someone in your org is using an LLM API. ATLAS gives you the threat model vocabulary for that conversation.
2. Read the [NIST AI RMF overview](https://nist.gov/itl/ai-risk-management-framework) and the [companion resources](https://airc.nist.gov/airmf-resources/airmf). Don't try to implement it yet: just understand the four functions and start thinking about which AI systems in your environment you'd map first.
3. Read both Simon Willison pieces on [MCP prompt injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) and [prompt injection estimation](https://simonwillison.net/2025/Jan/29/prompt-injection-attacks-on-ai-systems). These change how you reason about LLM application trust boundaries.
4. Read the [Trail of Bits prompt injection to RCE writeup](https://blog.trailofbits.com/2025/10/22/prompt-injection-to-rce-in-ai-agents/). Bring it to your next architecture review for any AI agent deployment.

### This Quarter (ongoing)

Build a security review process for AI/LLM applications in your organization. This means:

- An inventory of every AI/ML system (production and experimental)
- A lightweight threat model template based on OWASP LLM Top 10 + MITRE ATLAS
- A review checklist that covers prompt injection, output handling, tool/API access controls, and data exfiltration
- Integration into your existing SDLC security review process. Not a separate workflow

This is the highest-leverage thing a security engineer can do right now. Most organizations have zero formal review process for AI systems. Building it puts you ahead of the field.

### What to Skip

- **Skip:** Generic cybersecurity certifications that don't cover AI (CISSP, CEH, Security+). They're fine for foundational knowledge, but they won't teach you anything about LLM attack surfaces, adversarial ML, or AI governance. If you already have them, great. If you're deciding where to invest certification time, prioritize AI-specific training.
- **Skip:** Vendor-specific AI security training (CrowdStrike University, Palo Alto Beacon, etc.) until you understand the frameworks. Learning a vendor's tool before understanding OWASP LLM Top 10 and MITRE ATLAS is like learning a SIEM before understanding log analysis. Framework knowledge transfers across vendors; vendor training doesn't transfer across frameworks.
- **Skip:** Building custom LLM security tools from scratch before understanding the threat model. I've seen teams spend months building prompt injection classifiers that garak could have exposed as inadequate in an afternoon. Use existing tools first, understand what they find, then build custom tooling for the gaps.
- **Skip:** AI doomer content and AGI safety research (unless that's specifically your field). Existential AI risk and practical AI security engineering are different disciplines with different timelines and different actions. The vulnerabilities in your AI systems today are mundane: injection, access control, supply chain. Not alignment failures.

---

*This is Part 3 of the [AI Role Upgrade Roadmap series](#). Each post maps the AI landscape for a specific software role. What matters, what doesn't, and where to invest your time.*

*Series: [Pillar](#) | [Foundation](#) | [DevOps](#) | **Security** | [Developer](#) | [Product](#) | [App Eng](#) | [Platform](#) | [Data](#) | [QA](#) | [Leaders](#)*

---

*Written by Neeraj Singh. Staff Security Infrastructure Engineer building security at scale in fintech. 15 years across JPMorgan Chase, Wayfair, Meta, and Parafin. I write about the intersection of security, infrastructure, and AI, from the perspective of someone who has to make these tools work in production, not just evaluate them in a lab.*


## Labs

Hands-on examples for this part live in [`labs/`](labs/). (Coming soon — open an issue if you want a specific one first.)
