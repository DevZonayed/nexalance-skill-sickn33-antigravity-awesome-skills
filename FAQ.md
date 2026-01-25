# ❓ Frequently Asked Questions (V3)

---

## 🔒 Security & Trust

### Q: What do the Risk Labels mean?

- ⚪ **Safe (White/Blue)**: Read-only, planning, or benign skills. Safe to run anywhere.
- 🔴 **Risk (Red)**: Skills that modify files, delete resources, or perform security scans. **Use with caution.**
- 🟣 **Official (Purple)**: Maintained by trusted vendors (Anthropic, DeepMind, etc.).

### Q: Can these skills hack my computer?

**No.** Skills are just text files (markdown instructions). However, they _instruct_ the AI to run commands.
If a skill says "delete all files", your AI might try to do it.
_Always review the code before creating a skill, and check the Risk label._

---

## 📦 Installation & Usage

### Q: Why shouldn't I just copy all files?

You can! But 250+ files might clutter your context window.
We recommend using **Starter Packs** (`docs/BUNDLES.md`) to install only what you need for your specific role.

### Q: Does this work with Windows?

**Yes**, but some "Official" skills use **symlinks** which Windows handles poorly by default.
Run git with:
`git clone -c core.symlinks=true ...`
Or enable "Developer Mode" in Windows Settings.

---

## 🛠️ Contribution

### Q: My PR failed "Quality Bar" check. Why?

V3 introduces automated quality control. Your skill might be missing:

1.  A valid `description` in the metadata.
2.  Usage examples.
    Or it might be triggering a security filter. Run `python3 scripts/validate_skills.py` locally to see the error.

### Q: Can I update an "Official" skill?

**No.** Official skills (in `skills/official/`) are mirrored from vendors.
Open an issue instead, and we will forward it to the maintainers.
