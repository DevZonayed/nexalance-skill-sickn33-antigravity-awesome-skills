# 🤝 Contributing Guide - V3 Enterprise Edition

**Thank you for wanting to help!** This repository is built by the community, for the community.
With V3, we raised the bar for quality. This guide covers everything from your first Pull Request to our new Quality Standards.

---

## 🧐 The "Quality Bar" (V3 Standard)

**Critical for new skills:** Every skill submitted must pass our **5-Point Quality Check** (see `docs/QUALITY_BAR.md` for details):

1.  **Metadata**: Correct Frontmatter (`name`, `description`).
2.  **Safety**: No harmful commands without "Risk" labels.
3.  **Clarity**: Clear "When to use" section.
4.  **Examples**: At least one copy-paste usage example.
5.  **Actions**: Must define concrete steps, not just "thoughts".

---

## 🛠️ Ways to Contribute

You don't need to be an expert! Here are ways anyone can help:

### 1. Improve Documentation

- Fix typos or grammar
- Add examples to existing skills
- Translate documentation

### 2. Create New Skills

- Share your expertise as a skill
- Fill gaps in the current collection

### 3. Report Issues

- Found a bug? [Open an issue](https://github.com/sickn33/antigravity-awesome-skills/issues)

---

## 🚀 Step-by-Step: Create Your First Skill

### Step 1: Fork & Clone

```bash
git clone https://github.com/YOUR-USERNAME/antigravity-awesome-skills.git
cd antigravity-awesome-skills
```

### Step 2: Create the Folder

Skills live in `skills/`. Names must be `kebab-case`.

```bash
# Good
mkdir skills/my-new-skill

# Bad
mkdir skills/MyNewSkill
```

### Step 3: Write the Content (`SKILL.md`)

Every skill needs this basic structure. Copy this template:

```markdown
---
name: my-new-skill
description: One line description of what this does.
---

# My New Skill

## Overview

What problem does this solve?

## Usage Examples

> "@my-new-skill help me..."

## Core Instructions

[Detailed instructions for the AI]
```

### Step 4: Validate (CRITICAL)

Run the validation script locally. **We will not merge PRs that fail this check.**

```bash
# Soft mode (warnings only)
python3 scripts/validate_skills.py

# Hard mode (what CI runs)
python3 scripts/validate_skills.py --strict
```

### Step 5: Test & Submit

1.  Copy it to your local agent folder (`.agent/skills/`).
2.  Test it with your AI.
3.  Push and open a Pull Request!

---

## 💡 Best Practices for V3

- **Be Specific**: Don't say "Write code". Say "Write strict TypeScript code using these patterns...".
- **Use Examples**: The AI learns best from examples.
- **Keep it Atomic**: One skill, one job. Don't make "god skills".

---

## ⚖️ Code of Conduct

We adhere to the [Contributor Covenant](https://www.contributor-covenant.org).
**Rule #1**: Be kind.
**Rule #2**: No malware/harmful skills. (See `docs/SECURITY_GUARDRAILS.md`).

---

## 📦 Submission Checklist

- [ ] Folder name is `kebab-case`
- [ ] `SKILL.md` exists
- [ ] `scripts/validate_skills.py` passes
- [ ] You tested it in an actual AI session
