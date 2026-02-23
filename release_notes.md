## v6.1.0 - Issues Fix & Community Expansion

**Bugfixes for #116 and #120, plus Game Dev bundle, Android skills, Workflow Bundles, LibreOffice, Data Structure Protocol, and Kiro IDE support.**

This release fixes the YAML syntax error in database-migrations-sql-migrations (issue #116), adds a typo alias so `shopify—development` (em dash) resolves to `shopify-development` (issue #120), and ships a large set of community PRs: Game Development Expansion (Bevy ECS, GLSL, Godot 4), Android Modern Development (Compose + Coroutines), Workflow Bundles and LibreOffice skills, Data Structure Protocol, and Kiro CLI/IDE support.

### New Skills

- **Game Development Expansion** (PR #121): `bevy-ecs-expert`, `shader-programming-glsl`, `godot-4-migration`.
- **Android Modern Development** (PR #118): `android-jetpack-compose-expert`, `kotlin-coroutines-expert`.
- **Workflow Bundles & LibreOffice** (PR #113): Workflow bundles readme, LibreOffice skills (Base, Calc, Draw, Impress, Writer), plus office-productivity, WordPress suite, and many domain skills.
- **Data Structure Protocol** (PR #114): `data-structure-protocol`.
- **Kiro CLI and Kiro IDE** (PR #122): Documentation and support for Kiro.

### Improvements

- **YAML fix** (PR #119, fixes #116): Resolved invalid YAML in `database-migrations-sql-migrations/SKILL.md`.
- **Skill matching** (fixes #120): Added typo alias `shopify—development` → `shopify-development`.
- **Registry**: Now tracking 925 skills.

### Credits

- **@nikolasdehor** for YAML fix (PR #119), Game Development Expansion (PR #121), Android Modern Development (PR #118)
- **@ssumanbiswas** for Kiro CLI and Kiro IDE support (PR #122)
- **@munir-abbasi** for Workflow Bundles and LibreOffice Skills (PR #113)
- **@k-kolomeitsev** for Data Structure Protocol (PR #114)

---

_Upgrade: `git pull origin main` or `npx antigravity-awesome-skills`_
