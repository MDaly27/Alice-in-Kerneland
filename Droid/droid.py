import requests
import sys
import re
from pathlib import Path

# parse args
if len(sys.argv) != 2:
    print("Incorrect usage: droid.py filename")
    exit()

TAG_RX = re.compile(r'#[A-Za-z0-9_]+') # tag matcher

filename = sys.argv[1]

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
    role_msg = {"role": "system", "content": ("Your  goal is to generate a file fileld with tags of this exac format: #{single word descriptor}. output just those tags, "
                                              "seperated by newlines. they should relate to the topics presented as input from the user, taking the main ideas and putting"
                                              " them into single word tag representations. Output only the tags, no exaplanation or other forms of text."
                                              "All tags need to start with a hashtag symbol then a single word."
                                              "Number of tags should be related to the depth of topics included. Only important concepts should be tagged."
                                              "ONLY use the ALLOWED TAGS provided by the user unless NONE apply."
                                              "The previous instruction is VERY IMPORTANT."
                                              "MAXIMUM NUMBER of tags is 10, but 8 or under is prefered. Caputre only whats important.")}


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
    print(f"waiting for answer from droid.py, input: {text}")
    answer = simple_req(messages)
    print(answer)

def main():
    t = "Robots are machines designed to carry out tasks automatically, often using sensors, control systems, and software to interact with their environment. They can be built to handle repetitive or dangerous jobs, such as assembling products in factories, exploring hazardous areas, or assisting in medical procedures. Modern robots range from industrial arms to autonomous drones and even humanoid assistants, showing how versatile the technology has become. As robotics continues to advance, these machines are playing an increasingly important role in both everyday life and specialized industries."
    t = "Surfing is a water sport where a person rides waves on a surfboard, balancing skill and timing to glide across the ocean’s surface. It requires awareness of the sea, from reading wave patterns to positioning correctly for the ride. Surfers often describe it as both physically challenging and deeply relaxing, combining athleticism with a sense of freedom. Beyond being a sport, surfing has grown into a lifestyle and culture centered around the ocean, adventure, and connection to nature."
    run_analysis(t)

if __name__ == "__main__":
    main()
