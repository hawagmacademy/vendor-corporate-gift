import os
import re

# Folder project (asumsikan dijalankan di root project)
target_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Regex patterns
# 1. href="index.html" -> href="/"
index_pattern = re.compile(r'href="(\./)?index\.html"')
# 2. href="nama-file.html" -> href="/nama-file" (internal link)
internal_link_pattern = re.compile(r'href="([a-zA-Z0-9_-]+)\.html"')
# 3. Canonical URL
canonical_pattern = re.compile(r'href="https://vendorcorporategift\.web\.id/([a-zA-Z0-9_-]+)\.html"')

html_files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

# We should first revert any corrupted CSS/Img files if possible, or we just tell the user to git restore.
# Since we might not have git, let's fix the specific known corruptions first.
corruption_fixes = [
    ('href="/exclusive-hardcover-agenda-book" rel="stylesheet"', 'href="assets/vendor/aos/aos.css" rel="stylesheet"'),
    ('href="/executive-leather-gift-box" rel="stylesheet"', 'href="assets/vendor/drift-zoom/drift-basic.css" rel="stylesheet"'),
    ('src="/executive-premium-corporate-gift-set" alt="Workshop', 'src="assets/img/hero/corporate-gift-set.webp" alt="Workshop')
]

for filename in html_files:
    filepath = os.path.join(target_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # Revert known corruptions
    for bad, good in corruption_fixes:
        content = content.replace(bad, good)
        
    # Apply clean URLs
    # 1. Canonical URLs
    content = canonical_pattern.sub(r'href="https://vendorcorporategift.web.id/\1"', content)
    
    # 2. Index link
    content = index_pattern.sub(r'href="/"', content)
    
    # 3. Other internal HTML links
    content = internal_link_pattern.sub(r'href="/\1"', content)
    
    # Save if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filename}")

print("\nSelesai! Semua link telah diubah menjadi clean URL dan file yang terkorupsi telah diperbaiki.")
