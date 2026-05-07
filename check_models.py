from google import genai

# 🔑 paste your API key here
client = genai.Client(api_key="AIzaSyCnkdzQMPmGBpLZpl8bGfJ-T-JNbbCEePs")

# list models
for model in client.models.list():
    print(model.name)