# Part 3: The Security Engineer's AI Landscape — Curated Resources

> Companion reference shelf for [the Part 3 article](../README.md#published-parts). The article is the map; this is the full graded path.

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


## Domain maturity matrices

**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | CrowdStrike Charlotte AI, Palo Alto Cortex XSIAM 3.0, Microsoft Security Copilot |
| Emerging | SentinelOne Purple AI, Google Chronicle Security AI |
| Experimental | Autonomous SOC agents, fully agentic incident response |

**Key references:**
--
**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | MITRE ATLAS framework, OWASP Top 10 for LLM Apps |
| Emerging | NVIDIA garak, Microsoft PyRIT, custom red teaming harnesses |
| Experimental | Automated adversarial ML pipelines, self-healing AI defenses |

**Key references:**
--
**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Google SAIF framework, OWASP LLM guidance, CISA AI playbook |
| Emerging | MCP security layers, LLM firewall/proxy products, interpretability-based monitoring |
| Experimental | Formal verification for LLM behavior, provably safe prompt processing |

**Key references:**
--
**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | NIST AI RMF, ISO/IEC 42001 |
| Emerging | EU AI Act compliance tooling, automated AI risk assessment |
| Experimental | Continuous AI compliance monitoring, real-time governance dashboards |

**Key references:**
--
**Current state:**

| Maturity | Tools/Approaches |
|----------|-----------------|
| Production-ready | Hugging Face malware scanning, Safetensors format |
| Emerging | OpenSSF Model Signing, Sigstore for ML, JFrog ML scanning |
| Experimental | End-to-end ML SBOM, dataset provenance verification |

**Key references:**

## Fresh threat intel (verified July 2026)

CVEs referenced in the article, all verified against NVD:

| CVE | What | Fix |
|-----|------|-----|
| [CVE-2026-4372](https://nvd.nist.gov/vuln/detail/CVE-2026-4372) | Critical RCE in Hugging Face Transformers < 5.3.0 — malicious `config.json` compromises the host on import | Upgrade to >= 5.3.0; enforce model signing |
| [CVE-2025-67644](https://nvd.nist.gov/vuln/detail/CVE-2025-67644) | LangGraph SQLite checkpoint SQL injection | Patch checkpoint-sqlite |
| [CVE-2026-28277](https://nvd.nist.gov/vuln/detail/CVE-2026-28277) | LangGraph SQLite checkpoint unsafe deserialization → code execution | Patch checkpoint-sqlite |
| [CVE-2026-27022](https://nvd.nist.gov/vuln/detail/CVE-2026-27022) | LangGraph Redis checkpoint query injection | Patch checkpoint-redis |
