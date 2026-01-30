#!/usr/bin/env python3
"""
Count uncommitted skills by checking git status.
"""

import subprocess
import json
from pathlib import Path

def run_git_command(cmd):
    """Run git command and return output."""
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except Exception as e:
        print(f"Error running git command: {e}")
        return []

def main():
    base_dir = Path(__file__).parent.parent
    
    # Get all uncommitted files
    untracked = run_git_command("git ls-files --others --exclude-standard")
    modified = run_git_command("git diff --name-only HEAD")
    staged = run_git_command("git diff --cached --name-only")
    
    # Also check status
    status_output = run_git_command("git status --porcelain")
    
    print("Git status output:")
    for line in status_output[:20]:  # First 20 lines
        print(f"  {line}")
    print()
    
    # Filter for skill files
    skill_files = []
    for file_list in [untracked, modified, staged]:
        for file in file_list:
            if '/skills/' in file and file.endswith('SKILL.md'):
                skill_name = file.split('/skills/')[1].split('/SKILL.md')[0]
                if skill_name not in [s['name'] for s in skill_files]:
                    skill_files.append({
                        'name': skill_name,
                        'file': file,
                        'status': 'untracked' if file in untracked else ('staged' if file in staged else 'modified')
                    })
    
    # Load catalog to verify
    catalog_file = base_dir / "data" / "catalog.json"
    with open(catalog_file, 'r') as f:
        catalog = json.load(f)
    
    catalog_skills = {s['name']: s for s in catalog.get('skills', [])}
    
    print("=" * 70)
    print("SKILLS NON COMMITTATE")
    print("=" * 70)
    print(f"\nTotale skills trovate: {len(skill_files)}")
    print(f"Totale skills nel catalog: {catalog.get('total', 0)}")
    print()
    
    # Group by status
    untracked_skills = [s for s in skill_files if s['status'] == 'untracked']
    modified_skills = [s for s in skill_files if s['status'] == 'modified']
    staged_skills = [s for s in skill_files if s['status'] == 'staged']
    
    print(f"📝 Skills non tracciate (nuove): {len(untracked_skills)}")
    print(f"📝 Skills modificate: {len(modified_skills)}")
    print(f"📝 Skills staged: {len(staged_skills)}")
    print()
    
    if untracked_skills:
        print("Nuove skills (non tracciate):")
        for skill in sorted(untracked_skills, key=lambda x: x['name']):
            in_catalog = skill['name'] in catalog_skills
            print(f"  ✅ {skill['name']} {'(in catalog)' if in_catalog else '(NOT in catalog)'}")
    
    if modified_skills:
        print("\nSkills modificate:")
        for skill in sorted(modified_skills, key=lambda x: x['name']):
            print(f"  📝 {skill['name']}")
    
    if staged_skills:
        print("\nSkills staged:")
        for skill in sorted(staged_skills, key=lambda x: x['name']):
            print(f"  📦 {skill['name']}")
    
    # Check for VoltAgent skills specifically
    print("\n" + "=" * 70)
    print("VERIFICA SKILLS DA VOLTAGENT")
    print("=" * 70)
    
    voltagent_skills_phase1 = [
        'commit', 'create-pr', 'find-bugs', 'iterate-pr',
        'culture-index', 'fix-review', 'sharp-edges',
        'expo-deployment', 'upgrading-expo',
        'using-neon', 'vercel-deploy-claimable', 'design-md',
        'hugging-face-cli', 'hugging-face-jobs',
        'automate-whatsapp', 'observe-whatsapp', 'readme', 'screenshots',
        'deep-research', 'imagen', 'swiftui-expert-skill',
        'n8n-code-python', 'n8n-mcp-tools-expert', 'n8n-node-configuration'
    ]
    
    voltagent_skills_phase2 = [
        'frontend-slides', 'linear-claude-skill', 'skill-rails-upgrade',
        'context-fundamentals', 'context-degradation', 'context-compression',
        'context-optimization', 'multi-agent-patterns', 'tool-design',
        'evaluation', 'memory-systems', 'terraform-skill'
    ]
    
    all_voltagent = voltagent_skills_phase1 + voltagent_skills_phase2
    
    uncommitted_voltagent = []
    for skill_name in all_voltagent:
        skill_file = base_dir / "skills" / skill_name / "SKILL.md"
        if skill_file.exists():
            # Check if it's uncommitted
            if skill_file.relative_to(base_dir).as_posix() in untracked:
                uncommitted_voltagent.append(skill_name)
            elif skill_file.relative_to(base_dir).as_posix() in modified:
                uncommitted_voltagent.append(skill_name)
            elif skill_file.relative_to(base_dir).as_posix() in staged:
                uncommitted_voltagent.append(skill_name)
    
    print(f"\nSkills da VoltAgent non committate: {len(uncommitted_voltagent)}")
    print(f"  Fase 1 (49 skills): {len([s for s in voltagent_skills_phase1 if s in uncommitted_voltagent])}")
    print(f"  Fase 2 (12 skills): {len([s for s in voltagent_skills_phase2 if s in uncommitted_voltagent])}")
    
    print("\n" + "=" * 70)
    print("RIEPILOGO FINALE")
    print("=" * 70)
    print(f"Totale skills non committate: {len(skill_files)}")
    print(f"Skills da VoltAgent non committate: {len(uncommitted_voltagent)}")
    print(f"Altre skills non committate: {len(skill_files) - len(uncommitted_voltagent)}")
    
    return {
        'total_uncommitted': len(skill_files),
        'voltagent_uncommitted': len(uncommitted_voltagent),
        'voltagent_phase1': len([s for s in voltagent_skills_phase1 if s in uncommitted_voltagent]),
        'voltagent_phase2': len([s for s in voltagent_skills_phase2 if s in uncommitted_voltagent])
    }

if __name__ == "__main__":
    main()
