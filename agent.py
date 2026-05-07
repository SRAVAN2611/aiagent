from google import genai
from colorama import Fore, Style, init
import time

init(autoreset=True)

# 🔑 API KEY
API_KEY = "AIzaSyCnkdzQMPmGBpLZpl8bGfJ-T-JNbbCEePs"

client = genai.Client(api_key=API_KEY)

# 🔥 MODEL PRIORITY LIST (best → fallback)
MODELS = [
    "models/gemini-2.5-flash",
    "models/gemini-2.0-flash",
    "models/gemini-flash-latest"
]

MAX_RETRIES = 2

def header():
    print(Fore.CYAN + "="*60)
    print(Fore.GREEN + "        🤖 AI AGENT (SMART FALLBACK)")
    print(Fore.CYAN + "="*60)
    print(Fore.YELLOW + "Type 'exit' to quit\n")

def run():
    header()

    while True:
        query = input(Fore.BLUE + "You ➤ ")

        if query.lower() == "exit":
            print(Fore.YELLOW + "\nGoodbye!")
            break

        if query.strip() == "":
            print(Fore.RED + "Empty input!")
            continue

        success = False

        # 🔥 try each model
        for model in MODELS:
            print(Fore.CYAN + f"\nTrying model: {model}")

            for attempt in range(MAX_RETRIES):
                try:
                    response = client.models.generate_content(
                        model=model,
                        contents=query
                    )

                    print(Fore.GREEN + "\nAgent ➤ " + response.text + "\n")
                    success = True
                    break

                except Exception as e:
                    if "503" in str(e):
                        print(Fore.YELLOW + "Server busy... retrying")
                        time.sleep(1)
                    else:
                        break

            if success:
                break

        if not success:
            print(Fore.RED + "All models failed. Try again.")

run()