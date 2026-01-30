#!/usr/bin/env python3
"""
Implement the 12 new skills from similar skills analysis.
9 recommended + 3 verified (evaluation, memory-systems, terraform-skill)
"""

import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from typing import Dict, Optional

def normalize_skill_name(name: str) -> str:
    """Normalize skill name to kebab-case."""
    name = re.sub(r'[^a-z0-9-]', '-', name.lower())
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def download_file(url: str) -> Optional[str]:
    """Download content from URL."""
    try:
        req = Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; AntigravitySkillsDownloader/1.0)')
        with urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"    ❌ Error downloading {url}: {e}")
        return None

def parse_frontmatter(content: str) -> Optional[Dict]:
    """Parse YAML frontmatter."""
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None
    
    fm_text = fm_match.group(1)
    metadata = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            metadata[key.strip()] = val.strip().strip('"').strip("'")
    return metadata

def ensure_frontmatter_compliance(content: str, skill_name: str, source_url: str, description: str) -> str:
    """Ensure SKILL.md has compliant frontmatter."""
    metadata = parse_frontmatter(content)
    
    if not metadata:
        # No frontmatter, add it
        frontmatter = f"""---
name: {skill_name}
description: {description}
source: {source_url}
risk: safe
---

"""
        return frontmatter + content
    
    # Update existing frontmatter
    metadata['name'] = skill_name
    metadata['description'] = description
    metadata['source'] = source_url
    if 'risk' not in metadata:
        metadata['risk'] = 'safe'
    
    # Rebuild frontmatter
    frontmatter_lines = ['---']
    for key, value in metadata.items():
        if isinstance(value, str) and (' ' in value or ':' in value):
            frontmatter_lines.append(f'{key}: "{value}"')
        else:
            frontmatter_lines.append(f'{key}: {value}')
    frontmatter_lines.append('---\n')
    
    # Replace frontmatter in content
    content_without_fm = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    return '\n'.join(frontmatter_lines) + content_without_fm

def ensure_when_to_use_section(content: str, description: str) -> str:
    """Ensure 'When to Use' section exists."""
    if re.search(r'##\s+When\s+to\s+Use', content, re.IGNORECASE):
        return content
    
    # Add section after frontmatter
    when_to_use = f"""
## When to Use This Skill

{description}

Use this skill when working with {description.lower()}.
"""
    
    # Insert after frontmatter
    content = re.sub(r'(---\s*\n.*?\n---\s*\n)', r'\1' + when_to_use, content, flags=re.DOTALL)
    return content

def main():
    base_dir = Path(__file__).parent.parent
    
    # Load similar skills analysis
    analysis_file = base_dir / "similar_skills_analysis.json"
    with open(analysis_file, 'r') as f:
        analysis = json.load(f)
    
    # Skills to implement: 9 recommended + 3 verified
    skills_to_implement = [
        # 9 Recommended
        {
            'name': 'frontend-slides',
            'url': 'https://github.com/zarazhangrui/frontend-slides',
            'raw_url': 'https://github.com/zarazhangrui/frontend-slides/raw/main/SKILL.md',
            'description': 'Generate animation-rich HTML presentations with visual style previews',
            'org': 'zarazhangrui',
            'category': 'Community Skills'
        },
        {
            'name': 'linear-claude-skill',
            'url': 'https://github.com/wrsmith108/linear-claude-skill',
            'raw_url': 'https://github.com/wrsmith108/linear-claude-skill/raw/main/SKILL.md',
            'description': 'Manage Linear issues, projects, and teams',
            'org': 'wrsmith108',
            'category': 'Community Skills'
        },
        {
            'name': 'skill-rails-upgrade',
            'url': 'https://github.com/robzolkos/skill-rails-upgrade',
            'raw_url': 'https://github.com/robzolkos/skill-rails-upgrade/raw/master/SKILL.md',
            'description': 'Analyze Rails apps and provide upgrade assessments',
            'org': 'robzolkos',
            'category': 'Community Skills'
        },
        {
            'name': 'context-fundamentals',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-fundamentals',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/context-fundamentals/SKILL.md',
            'description': 'Understand what context is, why it matters, and the anatomy of context in agent systems',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'context-degradation',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-degradation',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/context-degradation/SKILL.md',
            'description': 'Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'context-compression',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-compression',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/context-compression/SKILL.md',
            'description': 'Design and evaluate compression strategies for long-running sessions',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'context-optimization',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/context-optimization',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/context-optimization/SKILL.md',
            'description': 'Apply compaction, masking, and caching strategies',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'multi-agent-patterns',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/multi-agent-patterns',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/multi-agent-patterns/SKILL.md',
            'description': 'Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'tool-design',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/tool-design/SKILL.md',
            'description': 'Build tools that agents can use effectively, including architectural reduction patterns',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        # 3 Verified (notebooklm-skill is duplicate, skip it)
        {
            'name': 'evaluation',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/evaluation',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/evaluation/SKILL.md',
            'description': 'Build evaluation frameworks for agent systems',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'memory-systems',
            'url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems',
            'raw_url': 'https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/raw/main/skills/memory-systems/SKILL.md',
            'description': 'Design short-term, long-term, and graph-based memory architectures',
            'org': 'muratcankoylan',
            'category': 'Community Skills'
        },
        {
            'name': 'terraform-skill',
            'url': 'https://github.com/antonbabenko/terraform-skill',
            'raw_url': 'https://github.com/antonbabenko/terraform-skill/raw/master/SKILL.md',
            'description': 'Terraform infrastructure as code best practices',
            'org': 'antonbabenko',
            'category': 'Community Skills'
        },
    ]
    
    print(f"🚀 Implementing {len(skills_to_implement)} new skills...\n")
    
    results = {
        'success': [],
        'failed': []
    }
    
    for skill in skills_to_implement:
        skill_name = skill['name']
        raw_url = skill['raw_url']
        source_url = skill['url']
        description = skill['description']
        
        print(f"📦 Processing: {skill_name}")
        
        # Download SKILL.md
        content = download_file(raw_url)
        if not content:
            print(f"    ❌ Failed to download")
            results['failed'].append(skill_name)
            continue
        
        # Check if it's HTML (shouldn't be, but just in case)
        if '<!DOCTYPE html>' in content or ('<html>' in content.lower() and content.count('<html>') > 1):
            print(f"    ⚠️  Received HTML instead of markdown, trying alternative URL")
            # Try alternative raw URL
            alt_url = raw_url.replace('/raw/main/', '/raw/master/') if '/raw/main/' in raw_url else raw_url.replace('/raw/master/', '/raw/main/')
            alt_content = download_file(alt_url)
            if alt_content and not ('<!DOCTYPE html>' in alt_content or '<html>' in alt_content.lower()):
                content = alt_content
                print(f"    ✅ Got markdown from alternative URL")
            else:
                print(f"    ❌ Still HTML, skipping")
                results['failed'].append(skill_name)
                continue
        
        # Ensure compliance
        content = ensure_frontmatter_compliance(content, skill_name, source_url, description)
        content = ensure_when_to_use_section(content, description)
        
        # Create skill directory
        skill_dir = base_dir / "skills" / skill_name
        skill_dir.mkdir(parents=True, exist_ok=True)
        
        # Write SKILL.md
        skill_file = skill_dir / "SKILL.md"
        skill_file.write_text(content, encoding='utf-8')
        
        print(f"    ✅ Created: {skill_file}")
        results['success'].append(skill_name)
    
    print(f"\n✅ Implementation complete!")
    print(f"   Success: {len(results['success'])}")
    print(f"   Failed: {len(results['failed'])}")
    
    if results['failed']:
        print(f"\n❌ Failed skills: {', '.join(results['failed'])}")
    
    return results

if __name__ == "__main__":
    main()
