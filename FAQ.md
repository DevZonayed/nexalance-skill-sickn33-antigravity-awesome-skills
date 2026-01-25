# ❓ Frequently Asked Questions (V3)

**Got questions?** Here are answers to the most common questions about Antigravity Awesome Skills.

---

## 🔒 Security & Trust (V3)

### Q: What do the Risk Labels mean?

In V3, we classify skills so you know what you're running:

- ⚪ **Safe (White/Blue)**: Read-only, planning, or benign skills. Safe to run anywhere.
- 🔴 **Risk (Red)**: Skills that modify files, delete resources, or perform security scans. **Use with caution.**
- 🟣 **Official (Purple)**: Maintained by trusted vendors (Anthropic, DeepMind, etc.).

### Q: Can these skills hack my computer?

**No.** Skills are just text files (markdown instructions). However, they _instruct_ the AI to run commands.
If a skill says "delete all files", your AI might try to do it.
_Always review the code before creating a skill, and check the Risk label._

---

## 📦 Installation & Setup

### Q: Do I need to install all 250+ skills?

**No!** When you clone the repository, all skills are available, but your AI only loads them when you explicitly invoke them with `@skill-name`.
It's like having a library - all the books are there, but you only read the ones you need.
_Pro Tip: Use [Starter Packs](docs/BUNDLES.md) to install only what matches your role._

### Q: Where should I install the skills?

The universal path is `.agent/skills/`:

```bash
git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills
```

### Q: Does this work with Windows?

**Yes**, but some "Official" skills use **symlinks** which Windows handles poorly by default.
Run git with:
`git clone -c core.symlinks=true ...`
Or enable "Developer Mode" in Windows Settings.

---

## 🛠️ Usage & Troubleshooting

### Q: How do I invoke a skill?

In your AI chat (Claude, Cursor, etc.), just use the `@` mention:

```
@brainstorming help me design a todo app
```

### Q: My AI assistant doesn't recognize skills. Why?

1.  **Wrong Path**: Did you clone to `.agent/skills/`? Check your tool's settings.
2.  **Restart Needed**: Some tools (like Cursor) need a restart to index new files.
3.  **Typos**: Check `ls .agent/skills/` to see the exact folder name.

### Q: What if a skill gives bad code?

Please [Open an Issue](https://github.com/sickn33/antigravity-awesome-skills/issues)!
Describe what happened and which skill was responsible. We update skills regularly to fix hallucinations.

---

## 🤝 Contribution

### Q: My PR failed "Quality Bar" check. Why?

V3 introduces automated quality control. Your skill might be missing:

1.  A valid `description` in the metadata.
2.  Usage examples.
    Or it might be triggering a security filter. Run `python3 scripts/validate_skills.py` locally to see the error.

### Q: Can I update an "Official" skill?

**No.** Official skills (in `skills/official/`) are mirrored from vendors.
Open an issue instead, and we will forward it to the maintainers.

### Q: Can I make my own skills?

**Absolutely!** Check out the **@skill-creator** skill or read [CONTRIBUTING.md](CONTRIBUTING.md).
