# 🚀 RELEASE NOTES: Antigravity Awesome Skills V3.0.0

**"The Governance Update"**

This release transforms the repository from a simple collection of scripts into a trusted, battle-tested platform for AI Agents.

## 🌟 Headline Features

### 1. Trusted Quality Bar (`docs/QUALITY_BAR.md`)

Every skill now undergoes a strict 5-point validation check.

- **Why?** No more broken scripts or vague instructions.
- **For You:** Look for the 🟣 **Official** or 🔵 **Safe** badges.

### 2. Security Guardrails (`docs/SECURITY_GUARDRAILS.md`)

We introduced "Risk Labels" to protect you.

- 🔴 **Offensive** skills (Pentesting) now require explicit authorization mechanisms.
- 🟢 **Safe** skills are guaranteed non-destructive.

### 3. Starter Packs (`docs/BUNDLES.md`)

Don't know where to start? We now have **9 Curated Bundles**:

- **Essentials Pack**: `concise-planning`, `clean-code`, `lint-and-validate`.
- **Web Wizard**: `react-patterns`, `tailwind-mastery`, `frontend-design`.
- **Agent Architect**: `mcp-builder`, `agent-evaluation`.
- ...plus **DevOps**, **Game Dev**, **Data Science**, **Testing**, and more.

## 🛠️ For Developers & Contributors

- **New CI/CD**: Pull Requests are now automatically validated (`.github/workflows/ci.yml`).
- **Strict Linting**: `scripts/validate_skills.py --strict` is the new sheriff in town.
- **Attribution**: We now have a clear ledger of sources in `docs/SOURCES.md`.

## 📦 How to Update

```bash
cd .agent/skills
git pull origin main
# (Optional) Verify your local skills
python3 scripts/validate_skills.py
```

_Built with ❤️ by the Antigravity Team._
