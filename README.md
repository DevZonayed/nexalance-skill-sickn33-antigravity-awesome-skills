<!-- registry-sync: version=7.0.1; skills=1272; stars=21193; updated_at=2026-03-07T09:42:47+00:00 -->
# 🌌 Antigravity Awesome Skills: 1,272+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **The Ultimate Collection of 1,272+ Universal Agentic Skills for AI Coding Assistants — Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, GitHub Copilot, Cursor, OpenCode, AdaL**

[![GitHub stars](https://img.shields.io/badge/⭐%2021%2C000%2B%20Stars-gold?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Kiro](https://img.shields.io/badge/Kiro-AWS-orange)](https://kiro.dev)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-VSCode-lightblue)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-DeepMind-red)](https://github.com/sickn33/antigravity-awesome-skills)
[![AdaL CLI](https://img.shields.io/badge/AdaL%20CLI-SylphAI-pink)](https://sylph.ai/)
[![ASK Supported](https://img.shields.io/badge/ASK-Supported-blue)](https://github.com/yeasy/ask)
[![Web App](https://img.shields.io/badge/Web%20App-Browse%20Skills-blue)](apps/web-app)
[![Buy Me a Book](https://img.shields.io/badge/Buy%20me%20a-book-d13610?logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/sickn33)

**Antigravity Awesome Skills** is a curated, battle-tested library of **1,272+ high-performance agentic skills** designed to work seamlessly across major AI coding assistants.

**Welcome to the V7.0.1 21k Stars Patch Release!** This repository gives your agent reusable playbooks for planning, coding, debugging, testing, security review, infrastructure work, product thinking, and much more.

> **🌟 21,000+ GitHub Stars Milestone!** Thank you to the community for turning this into one of the largest skill libraries in this category.

## Table of Contents

- [🚀 Quick Start](#quick-start)
- [📖 Complete Usage Guide](docs/USAGE.md)
- [🔌 Compatibility & Invocation](#compatibility--invocation)
- [🎁 Curated Collections (Bundles)](#curated-collections)
- [📦 Features & Categories](#features--categories)
- [📚 Browse 1,272+ Skills](#browse-1272-skills)
- [🤝 How to Contribute](#how-to-contribute)
- [🏆 Credits & Sources](#credits--sources)
- [👥 Repo Contributors](#repo-contributors)
- [⚖️ License](#license)

---

## Quick Start

**Welcome to the Interactive Web Edition.** This isn't just a list of scripts; it's a complete operating system for your AI Agent.

### 1. 🐣 Context: What is this?

AI Agents (like Claude Code, Cursor, or Gemini) are smart, but they lack **specific tools**. They don't know your company's "Deployment Protocol" or the specific syntax for "AWS CloudFormation". **Skills** are small markdown files that teach them how to do these specific tasks perfectly, every time.

### 2. ⚡️ Installation (1 minute)

Install once; then use Starter Packs in [docs/BUNDLES.md](docs/BUNDLES.md) to focus on your role.

```bash
# Default: ~/.gemini/antigravity/skills (Antigravity global)
npx antigravity-awesome-skills
```

### 3. 🧠 How to use

Once installed, just ask your agent naturally:

> "Use the **@brainstorming** skill to help me plan a SaaS."

👉 [**Complete Usage Guide - Read This First!**](docs/USAGE.md)

---

## Compatibility & Invocation

| Tool            | Type | Invocation Example          | Path                            |
| :-------------- | :--- | :-------------------------- | :------------------------------ |
| **Claude Code** | CLI  | `>> /skill-name help me...` | `.claude/skills/`               |
| **Gemini CLI**  | CLI  | `Use skill-name...`         | `.gemini/skills/`               |
| **Antigravity** | IDE  | `(Agent Mode) Use skill...` | `~/.gemini/antigravity/skills/` |
| **Cursor**      | IDE  | `@skill-name (in Chat)`     | `.cursor/skills/`               |
| **OpenCode**    | CLI  | `opencode run @skill-name`  | `.agents/skills/`               |

---

## Curated Collections

**Bundles** are groups of skills for a specific role (e.g., `Web Wizard`, `Security Engineer`).

1. **Install once** (you already have all skills).
2. **Browse bundles** in [docs/BUNDLES.md](docs/BUNDLES.md).
3. **Pick 3-5 skills** to start using in your prompts.

---

## Features & Categories

| Category       | Focus                          | Example skills                           |
| :------------- | :----------------------------- | :--------------------------------------- |
| Architecture   | System design, ADRs, patterns  | `architecture`, `senior-architect`       |
| Data & AI      | LLM apps, RAG, agents          | `rag-engineer`, `prompt-engineer`        |
| Development    | Frameworks, quality, languages | `typescript-expert`, `react-patterns`    |
| General        | Planning, docs, product ops    | `brainstorming`, `writing-plans`         |
| Infrastructure | DevOps, cloud, CI/CD           | `docker-expert`, `aws-serverless`        |
| Security       | AppSec, pentesting, compliance | `api-security`, `vulnerability-scanner`  |
| Testing        | TDD, fixes, QA workflows       | `test-driven-development`, `test-fixing` |

---

## Browse 1,272+ Skills

We have moved the full skill registry to a dedicated catalog to keep this README clean.

### 🌐 Interactive Skills Web App

A modern web interface to explore, search, and use the skills directly from your browser.

- Open the interactive browser in [`apps/web-app`](apps/web-app).
- Read the full catalog in [`CATALOG.md`](CATALOG.md).

---

## Documentation

| For Users                                                        | For Contributors                                                           | For Maintainers                                                              |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| [`docs/users/getting-started.md`](docs/users/getting-started.md) | [`CONTRIBUTING.md`](CONTRIBUTING.md)                                       | [`docs/maintainers/release-process.md`](docs/maintainers/release-process.md) |
| [`docs/users/usage.md`](docs/users/usage.md)                     | [`docs/contributors/skill-anatomy.md`](docs/contributors/skill-anatomy.md) | [`docs/maintainers/audit.md`](docs/maintainers/audit.md)                     |

---

## Contributing

- Add new skills under `skills/<skill-name>/SKILL.md`.
- Follow the template in [`docs/contributors/skill-template.md`](docs/contributors/skill-template.md).
- Validate with `npm run validate` before opening a PR.

---

## Credits & Sources

We stand on the shoulders of giants. 👉 [**View Full Attribution Ledger**](docs/sources/sources.md)

### Official Sources

- **Anthropic**: [anthropics/skills](https://github.com/anthropics/skills)
- **Vercel Labs**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- **OpenAI**: [openai/skills](https://github.com/openai/skills)
- **Microsoft**: [microsoft/skills](https://github.com/microsoft/skills)
- **Google**: [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills)

### Community Contributors

- **@rmyndharis**: For the massive contribution of 300+ Enterprise skills.
- **Jesse Vincent**: Original "Superpowers" inspiration.

---

## Repo Contributors

<a href="https://github.com/sickn33/antigravity-awesome-skills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sickn33/antigravity-awesome-skills" alt="Repository contributors" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sickn33/antigravity-awesome-skills&type=date&legend=top-left)](https://www.star-history.com/#sickn33/antigravity-awesome-skills&type=date&legend=top-left)

<!-- GitHub Topics: claude-code, gemini-cli, codex-cli, antigravity, cursor, github-copilot, opencode, agentic-skills, ai-coding, llm-tools, ai-agents, autonomous-coding, mcp, ai-developer-tools, ai-pair-programming, vibe-coding, skill, skills, SKILL.md, rules.md, CLAUDE.md, GEMINI.md, CURSOR.md -->
