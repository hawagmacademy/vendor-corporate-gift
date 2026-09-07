import os
import glob

def main():
    directory = r"d:\GM\vendorcorporategift.web.id\vendorcorporategift.web.id"
    html_files = glob.glob(os.path.join(directory, "*.html"))
    for file in html_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace('href="/"', 'href="index.html"')
            if new_content != content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    main()
