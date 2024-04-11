# prompt-testing
Prompt testing for AI development

Open source python tool for testing multiple prompts against multiple models in ollama.

Very early development, will be updated with more features.

How to use:

1. Prepare prompts file
Each prompt should be in a new line inside txt file
Keep in mind token limits for different models

2. Run test.py
To run the script you need to provide the following parameters:
- -s seed (optional) - used for deterministic output, if omitted random value will be used every time
- -m models - comma seperated list of ollama models, they need to be installed locally
- -p prompts - txt file containing prompts
