# 🤝 Contributing Guide - V3 Enterprise Edition

**Thank you for wanting to help!** This repository is built by the community, for the community.
With V3, we raised the bar for quality. Here is how you can contribute effectively.

---

## 🧐 The "Quality Bar"

Every skill submitted must pass our **5-Point Quality Check** (see `docs/QUALITY_BAR.md` for details):

1.  **Metadata**: Correct Frontmatter (`name`, `description`).
2.  **Safety**: No harmful commands without "Risk" labels.
3.  **Clarity**: Clear "When to use" section.
4.  **Examples**: At least one copy-paste usage example.
5.  **Actions**: Must define concrete steps, not just "thoughts".

---

## 🛠️ How to Create a New Skill

### Step 1: Fork & Clone

```bash
git clone https://github.com/YOUR-USERNAME/antigravity-awesome-skills.git
cd antigravity-awesome-skills
```

### Step 2: Create the Folder

Skills live in `skills/`. Names must be `kebab-case`.

```bash
mkdir skills/my-new-skill
touch skills/my-new-skill/SKILL.md
```

### Step 3: Write the Content

Copy this template to start:

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
```

### Step 4: Validate (CRITICAL)

Run the validation script locally. **We will not merge PRs that fail this check.**

```bash
# Soft mode (warnings only)
python3 scripts/validate_skills.py

# Hard mode (what CI runs)
python3 scripts/validate_skills.py --strict
```

---

## 🧪 Testing Your Skill

Don't just write it—run it!

1.  Copy it to your local agent folder (`.agent/skills/`).
2.  Open your AI (Claude/Cursor).
3.  Type `@my-new-skill` and see if it behaves as expected.

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
