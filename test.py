import requests
seed=323156744 #You can specify seed or use any random number generator
def read_file_into_array(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Remove trailing newline characters
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print("File not found:", file_name)
        return []
file_name = "prompts.txt" #Each prompt should be in a new line
prompts = read_file_into_array(file_name)
models=[
    "mistral",
    "gemma:2b"
]

for m in models:
    for p in prompts:
        body={
        "model": m,
        "prompt": p,
        "stream": False,
        "options": {
            "seed": seed,
            "temperature": 0
        }
        }
        r = requests.post('http://localhost:11434/api/generate', json=body)
        print("--------------------------------------------------------")
        print("Model:   " + m)
        print("Prompt:   " + p)
        print (r.json()["response"])
        print("--------------------------------------------------------")