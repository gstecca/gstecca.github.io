import re
import os

def parse_bib(file_path):
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = re.findall(r'@(\w+)\{([^,]+),\s*(.*?)\n\}', content, re.DOTALL)
    publications = []
    
    for entry_type, cite_key, entry_body in entries:
        data = {'type': entry_type.lower()}
        fields = re.findall(r'(\w+)\s*=\s*\{(.*?)\},?', entry_body, re.DOTALL)
        for key, val in fields:
            clean_val = val.replace('{', '').replace('}', '').strip()
            data[key.lower()] = clean_val
        
        if 'title' in data and 'author' in data:
            publications.append(data)
    
    return sorted(publications, key=lambda x: x.get('year', '0000'), reverse=True)

def generate_markdown(pubs):
    md = ""
    for pub in pubs:
        title = pub.get('title', 'No Title')
        authors = pub.get('author', 'Unknown')
        year = pub.get('year', 'N/A')
        journal = pub.get('journal', pub.get('booktitle', ''))
        doi = pub.get('doi', '')
        url = pub.get('url', '')
        
        line = f"- **{title}**  \n  {authors}  \n  *{journal}*, {year}"
        if doi:
            line += f" [DOI: {doi}](https://doi.org/{doi})"
        elif url:
            line += f" [Link]({url})"
        
        md += line + "\n\n"
    return md

def update_index(index_path, pubs_md):
    if not os.path.exists(index_path):
        return
        
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to replace content between <!-- bibliography_start --> and <!-- bibliography_end -->
    pattern = r'(<!-- bibliography_start -->)(.*?)(<!-- bibliography_end -->)'
    replacement = f'\\1\n{pubs_md}\\3'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    bib_path = 'static/files/scopus2025.bib'
    pubs = parse_bib(bib_path)
    pubs_md = generate_markdown(pubs)
    
    # Update localized indexes
    update_index('content/en/_index.md', pubs_md)
    update_index('content/it/_index.md', pubs_md)
    
    print(f"Successfully updated indexes with {len(pubs)} publications.")
