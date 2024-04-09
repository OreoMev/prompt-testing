import requests
import argparse
import random

def read_file_into_array(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        raise Exception("File not found:", file_name)
        return []

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--seed') 
parser.add_argument('-m', '--models') 
parser.add_argument('-p', '--prompts')  
args = parser.parse_args()
if (args.seed != None):
    seed=args.seed
else:
    seed=random.randint(1, 999999) #if no seed is specified, random seed is created
    print("Random seed selected: "+ seed )
    print ("To specify the seed run with -s seed argument, where seed is any positive integer")
if (args.prompts != None):
    file_name = args.prompts 
else:
    print ("No file for prompts was specified, defaulting to prompts.txt")
    file_name= "prompts.txt"
prompts = read_file_into_array(file_name)

if (args.models != None):
    models=args.models.split(",")
else:
    raise Exception("Specify the models with -m model1,model2,model3 and make sure you have this models installed in local Ollama instalations")

for m in models:
    for p in prompts:
        body={
        "model": m.strip(),
        "prompt": p,
        "stream": False,
        "options": {
            "seed": int(seed),
            "temperature": 0
        }
        }
        r = requests.post('http://localhost:11434/api/generate', json=body)
        print("--------------------------------------------------------")
        print("Model:   " + m)
        print("Prompt:   " + p)
        print (r.json()["response"])
        print("--------------------------------------------------------")
