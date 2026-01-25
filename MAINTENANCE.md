# Repository Maintenance Protocol

> [!URGENT]
> **READ THIS FIRST**: The single most critical rule of this repository is: **IF YOU DO NOT PUSH YOUR CHANGES, THEY DO NOT EXIST.**
>
> **ALWAYS** run `git push` immediately after committing. No exceptions.

To ensure consistency and quality, the following steps MUST be performed for **every single request** involving skills or documentation.

## 1. Analysis & Pre-Flight (Planner Role)

Before writing any code:

- [ ] **Analyze Request**: Understand if it's a new skill, a fix, or a tool link.
- [ ] **Check Duplicates**: Run `grep -r "search_term" skills_index.json` to ensure the skill doesn't already exist.
- [ ] **Plan Integration**: Decide on the folder name and category.

## 2. Implementation & Standardization (Executor Role)

- [ ] **Folder Structure**: Create `skills/<skill-name>/`.
- [ ] **SKILL.md**: Create the file with valid frontmatter. **strict format**:

  ```markdown
  ---
  name: Skill Name
  description: Brief description (max 100 chars).
  ---
  ```

- [ ] **Content**: Ensure the skill instructions are clear and the `code` is functional.

## 3. Validation Chain (MANDATORY & BLOCKING)

You **MUST** run these scripts in order. If _any_ script fails, **STOP** and fix it.

1. **Validate Structure**:

   ```bash
   python3 scripts/validate_skills.py
   ```

2. **Update Index**:

   ```bash
   python3 scripts/generate_index.py
   ```

3. **Sync Documentation**:

   ```bash
   python3 scripts/update_readme.py
   ```

## 4. Documentation & Credits (CRITICAL)

- [ ] **Update README Credits**: Manually add the source link in the `## Credits & Sources` section of `README.md`.
  - Format: `- **[Repo Name](Url)**: Description of usage.`

## 5. Finalization (The "Antigravity" Standard)

- [ ] **Git Status**: Check what you are about to commit.
- [ ] **Git Add**: `git add .`
- [ ] **Commit**: `git commit -m "feat: add [skill-name] skill"`.
- [ ] **PUSH**:

  > [!CRITICAL]
  > **EXECUTE THIS IMMEDIATELY**: `git push`
  >
  > Do not wait. Do not "batch" later. Push NOW.

## 6. Release (If Applicable)

If this is a consolidated release:

- [ ] `git tag -a vX.Y.Z -m "Release X.Y.Z"`
- [ ] `git push origin vX.Y.Z`
- [ ] `gh release create vX.Y.Z --generate-notes`
