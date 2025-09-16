import requests
import sys
import re
import os
from pathlib import Path

# parse args
if len(sys.argv) != 2:
    print("Correct usage: droid.py <filename>")
    exit()

TAG_RX = re.compile(r'#[A-Za-z0-9_]+') # tag matcher

def simple_req(messages, model="phi4"):
    resp = requests.post("http://localhost:11434/api/chat", json={"model": model, "messages": messages, "stream": False, "options": 
                                                                                                                {"temperature": 0.2,
                                                                                                                 "top_p": 0.9,
                                                                                                                 "top_k": 40,
                                                                                                                 "stop": ["\n(", "\nNote:", "\nNOTE:", "\nnote:"]}})
    return resp.json()["message"]["content"]

with open("file.txt", 'w') as f:
    f.write("hello, file!")

def collect_md(path='.'):
    directory = Path(path)
    md_files = directory.glob("*.md")
    tags = set()
    for file in md_files:
        text = file.read_text(encoding='utf-8', errors='ignore')
        tags.update(TAG_RX.findall(text))
    return sorted(tags, key=str.lower)
    

def run_analysis(text):
    """Run the model with prompt engineering based on textual input. will return text answer response."""

    role_msg = {"role": "system", "content": ("Pick the most relevant tags from the ALLOWED TAGS category based on the input text."
                                              "Create 6 tags unless there is not enough content for that many."
                                              "If no ALLOWED TAGS apply, you have permission to create a few new ones, do this ONLY when NO TAGS APPLY"
                                              "You're output should be a series of tags seperated by newlines"
                                              "ABSOLUTELY NO sentences, explanation, notes, or anything outside of this format: #{tag}\n"
                                              "Tags are in this exact format: hashtag followed by a single lowercase word"
                                              "Example correct output '#machine\n#control\n#automata\n#ai\n#robotics\n#technology'"
                                              f"ALLOWED TAGS: {collect_md()}")}
    messages = [role_msg]
    messages.append({"role": "user", "content": text})
    print(f"waiting for answer from model.")
    answer = simple_req(messages)

    return answer

def main():
    filename = sys.argv[1]
    if filename[-4:] != ".txt":
        print("Not a text file")
        return -1

    output_fn = filename[:-4] +"_tr.md"

    if os.path.exists(output_fn):
        print(f"Output file {output_fn} already exists, please remove it before generating this tag file.")
        return -1
    
    r = False
    with open(filename, 'r') as f:
        data = f.read()
        r = run_analysis(data)
    if not r:
        print("Error opening file")
        return -1

    if r[-1] != '\n':
        r += '\n'

    with open(output_fn, 'w') as f:
        f.write(r)

    print("Succesfully created a tags file, " + output_fn)


if __name__ == "__main__":
    main()
