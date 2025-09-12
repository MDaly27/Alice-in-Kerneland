import requests
import sys

def simple_req(messages, model="phi3"):
    resp = requests.post("http://localhost:11434/api/chat", json={
                                                                "model": model,
                                                                "messages": messages,
                                                                "stream": False
                                                                })
    #print(resp.json())
    return resp.json()["message"]["content"]


role_msg = {"role": "system", "content": ("You MUST always answer in a single short sentence. Do not explain. Do not ask follow-up questions.")}
messages = [role_msg]


with open("file.txt", 'w') as f:
    f.write("hello, file!")

for line in sys.stdin:
    messages.append({"role": "user", "content": line.strip()})
    answer = simple_req(messages)
    messages.append({"role": "assistant", "content": answer})
    messages.append({"role": "system", "content": "Reminder, one sentence only."})
    print(answer)
    #print(messages)
