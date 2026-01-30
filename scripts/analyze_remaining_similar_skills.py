#!/usr/bin/env python3
"""
Analyze remaining similar skills to determine if they are truly new
and worth adding to the repository.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def normalize_skill_name(name: str) -> str:
    """Normalize skill name to kebab-case."""
    # Remove special chars, convert to lowercase, replace spaces/hyphens
    name = re.sub(r'[^\w\s-]', '', name.lower())
    name = re.sub(r'[\s_]+', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def check_url_accessible(url: str) -> bool:
    """Check if URL is accessible."""
    try:
        req = Request(url, method='HEAD')
        with urlopen(req, timeout=10) as response:
            return response.status == 200
    except (URLError, HTTPError, Exception):
        return False

def get_repo_base_url(github_url: str) -> str:
    """Extract base GitHub repository URL."""
    # Handle various GitHub URL formats
    patterns = [
        r'https://github\.com/([^/]+/[^/]+)',
        r'github\.com/([^/]+/[^/]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, github_url)
        if match:
            return f"https://github.com/{match.group(1)}"
    return None

def check_skill_file_exists(repo_url: str, skill_path: str = None) -> Tuple[bool, str]:
    """Check if SKILL.md exists in the repository."""
    base_url = get_repo_base_url(repo_url)
    if not base_url:
        return False, None
    
    # Common paths to check
    paths_to_check = [
        f"{base_url}/raw/main/{skill_path}/SKILL.md" if skill_path else f"{base_url}/raw/main/SKILL.md",
        f"{base_url}/raw/main/skills/{skill_path}/SKILL.md" if skill_path else None,
        f"{base_url}/raw/master/{skill_path}/SKILL.md" if skill_path else f"{base_url}/raw/master/SKILL.md",
        f"{base_url}/blob/main/{skill_path}/SKILL.md" if skill_path else f"{base_url}/blob/main/SKILL.md",
    ]
    
    for path in paths_to_check:
        if path and check_url_accessible(path):
            return True, path
    
    return False, None

def analyze_similarity(skill_name: str, similar_skills: List[str], existing_skills: Dict) -> Dict:
    """Analyze how similar a skill is to existing ones."""
    analysis = {
        'is_duplicate': False,
        'is_complementary': False,
        'similarity_score': 0.0,
        'closest_match': None,
        'reasoning': []
    }
    
    skill_lower = skill_name.lower()
    
    # Check for exact or near-exact matches
    for existing_name, existing_data in existing_skills.items():
        existing_lower = existing_name.lower()
        
        # Exact match
        if skill_lower == existing_lower:
            analysis['is_duplicate'] = True
            analysis['closest_match'] = existing_name
            analysis['reasoning'].append(f"Exact match with existing skill: {existing_name}")
            return analysis
        
        # Check if one contains the other
        if skill_lower in existing_lower or existing_lower in skill_lower:
            if abs(len(skill_lower) - len(existing_lower)) <= 3:
                analysis['is_duplicate'] = True
                analysis['closest_match'] = existing_name
                analysis['similarity_score'] = 0.9
                analysis['reasoning'].append(f"Near-exact match: '{skill_name}' vs '{existing_name}'")
                return analysis
    
    # Check similarity with similar skills list
    for similar in similar_skills:
        if similar.lower() in existing_skills:
            existing_data = existing_skills[similar.lower()]
            # If the similar skill exists, this might be a duplicate
            analysis['similarity_score'] = 0.7
            analysis['closest_match'] = similar
            analysis['reasoning'].append(f"Similar to existing skill: {similar}")
    
    # Determine if complementary
    if analysis['similarity_score'] < 0.5:
        analysis['is_complementary'] = True
        analysis['reasoning'].append("Low similarity - likely complementary skill")
    
    return analysis

def main():
    base_dir = Path(__file__).parent.parent
    
    # Load remaining similar skills
    remaining_file = base_dir / "remaining_similar_skills.json"
    if not remaining_file.exists():
        print("❌ remaining_similar_skills.json not found. Run the analysis first.")
        return
    
    with open(remaining_file, 'r') as f:
        data = json.load(f)
    
    # Load existing skills
    catalog_file = base_dir / "data" / "catalog.json"
    with open(catalog_file, 'r') as f:
        catalog = json.load(f)
    existing_skills = {s['name'].lower(): s for s in catalog.get('skills', [])}
    
    print(f"🔍 Analyzing {len(data['skills'])} remaining similar skills...\n")
    
    results = {
        'truly_new': [],
        'duplicates': [],
        'complementary': [],
        'needs_review': [],
        'invalid_sources': []
    }
    
    for skill in data['skills']:
        skill_name = skill['name']
        print(f"Analyzing: {skill_name}")
        
        # Skip if already exists
        if skill['exists_in_catalog'] or skill['folder_exists']:
            results['duplicates'].append({
                'name': skill_name,
                'reason': 'Already exists in repository',
                'url': skill['url']
            })
            continue
        
        # Check source accessibility
        exists, raw_url = check_skill_file_exists(skill['url'], skill.get('skill_part'))
        if not exists:
            results['invalid_sources'].append({
                'name': skill_name,
                'url': skill['url'],
                'reason': 'SKILL.md not found or URL inaccessible'
            })
            continue
        
        # Analyze similarity
        similarity_analysis = analyze_similarity(
            skill_name,
            skill['similar_to'],
            existing_skills
        )
        
        skill_result = {
            'name': skill_name,
            'url': skill['url'],
            'raw_url': raw_url,
            'description': skill['description'],
            'org': skill['org'],
            'category': skill['category'],
            'similar_to': skill['similar_to'],
            'similarity_analysis': similarity_analysis
        }
        
        if similarity_analysis['is_duplicate']:
            results['duplicates'].append(skill_result)
        elif similarity_analysis['is_complementary']:
            results['complementary'].append(skill_result)
        else:
            results['needs_review'].append(skill_result)
    
    # Generate report
    report = {
        'summary': {
            'total_analyzed': len(data['skills']),
            'truly_new': len(results['complementary']),
            'duplicates': len(results['duplicates']),
            'needs_review': len(results['needs_review']),
            'invalid_sources': len(results['invalid_sources'])
        },
        'results': results
    }
    
    output_file = base_dir / "similar_skills_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Analysis complete!")
    print(f"📊 Summary:")
    print(f"   - Truly new (complementary): {len(results['complementary'])}")
    print(f"   - Duplicates: {len(results['duplicates'])}")
    print(f"   - Needs review: {len(results['needs_review'])}")
    print(f"   - Invalid sources: {len(results['invalid_sources'])}")
    print(f"\n📄 Full report saved to: {output_file}")

if __name__ == "__main__":
    main()
