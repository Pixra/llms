import os
import time
import google.generativeai as genai

# ✅ 1. APNI API KEY YAHAN DAALO
genai.configure(api_key="AIzaSyCLYLnA4LTUx-o8_65nNqNdY5h0GTPrGPM")

# YAHAN UPDATE KIYA HAI: 'gemini-3-flash' ab standard model hai
model = genai.GenerativeModel('gemini-flash-latest')

PROMPT_TEMPLATE = """
Rewrite this documentation for 'Pixra AI Hub'. 
Rules: 
- Title: Emoji + Professional Name (e.g., 📄 Chat with PDF).
- Style: Premium SaaS, clean and high-tech.
- Sections: Intro (catchy), Features (bold keywords), Setup (1. Clone, 2. Install, 3. Keys, 4. Run).
- Repository Link: Use https://github.com/Pixra/llms.git.
- Cleanup: Remove all personal bios, YouTube links, and tutorial ads.

Original Content:
{content}
"""

def process_files():
    root_dir = "." 
    exclude_dirs = {'.git', 'venv', '__pycache__', '.ipynb_checkpoints', 'node_modules'}

    print(f"🚀 Starting Global Scan in: {os.getcwd()}")

    processed_count = 0
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for filename in ['README.md', 'READUS.md', 'readme.md']:
            if filename in files:
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        old_content = f.read()
                except:
                    continue
                
                if "Pixra AI Hub" in old_content[:150]:
                    print(f"⏩ Skipping (Already Pixra): {file_path}")
                    continue

                print(f"✨ Polishing: {file_path}...")
                try:
                    # Model generation call
                    response = model.generate_content(PROMPT_TEMPLATE.format(content=old_content))
                    new_content = response.text
                    
                    new_file_path = os.path.join(root, 'READUS.md')
                    with open(new_file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    if filename.lower() == 'readme.md':
                        os.remove(file_path)

                    processed_count += 1
                    print(f"✅ Success! ({processed_count} files total)")
                    
                    # Rate limit safety
                    time.sleep(5) 
                except Exception as e:
                    if "429" in str(e):
                        print("⏳ Rate limit hit! Waiting 30 seconds...")
                        time.sleep(30)
                    elif "404" in str(e):
                        print(f"⚠️ Model ID error: {e}. Check if 'gemini-3-flash' is available in your region.")
                        return # Stop script if model name is wrong
                    else:
                        print(f"⚠️ Error at {file_path}: {e}")
                        time.sleep(5)

    print(f"\n🎉 MISSION COMPLETE! Total {processed_count} files transformed into Pixra Style.")

if __name__ == "__main__":
    process_files()