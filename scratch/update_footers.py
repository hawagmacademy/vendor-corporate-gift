import os, re
import glob

workspace = r'd:\GM\LuxuryHotel-pro\LuxuryHotel-pro'
index_path = os.path.join(workspace, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the new footer
match = re.search(r'<footer id="footer".*?</footer>', index_html, re.DOTALL)
if not match:
    print("Could not find footer in index.html")
    exit(1)
new_footer = match.group(0)

# Replace in all html files
for filepath in glob.glob(os.path.join(workspace, '*.html')):
    if filepath.endswith('index.html'): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the old footer
    new_content, count = re.subn(r'<footer id="footer".*?</footer>', new_footer, content, flags=re.DOTALL)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No footer found in {os.path.basename(filepath)}")
