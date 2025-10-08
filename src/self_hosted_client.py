import requests
import json

def ask_local_ai(prompt, model="qwen"):
    """
    Kérdést küld a lokálisan futó, Ollama által menedzselt MI modellnek.

    Args:
        prompt (str): A kérdés vagy utasítás a modellnek.
        model (str): A használni kívánt modell neve (pl. "qwen", "llama3").

    Returns:
        str: Az MI válasza vagy hibaüzenet.
    """
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Ha True lenne, a válasz darabokban érkezne
    }

    print(f"Kérés küldése a(z) '{model}' modellnek a helyi Ollama szerverre...")

    try:
        response = requests.post(url, data=json.dumps(payload))
        response.raise_for_status()  # Hiba dobása, ha a kérés sikertelen (pl. 404, 500)

        data = response.json()
        return data.get('response', 'A válasz nem tartalmazta a "response" kulcsot.')

    except requests.exceptions.ConnectionError:
        return "Hiba: Nem sikerült csatlakozni az Ollama szerverhez a http://localhost:11434 címen. Biztosan fut?"
    except requests.exceptions.RequestException as e:
        return f"Hiba történt az API hívás során: {e}"

if __name__ == "__main__":
    print("--- Saját Hosztolású MI Kliens (3. Opció) ---")
    print("Ez a szkript egy lokálisan, Ollama segítségével futtatott MI modellhez küld kérést.")
    print("Győződj meg róla, hogy az Ollama fut, és letöltötted a használni kívánt modellt (pl. `ollama pull qwen`).")
    print("Írj 'kilep' szót a befejezéshez.\n")

    while True:
        user_prompt = input("Te: ")
        if user_prompt.lower() == 'kilep':
            print("Viszlát!")
            break

        ai_answer = ask_local_ai(user_prompt)

        print("\n--- Lokális MI Válasza ---")
        print(ai_answer)
        print("--------------------------\n")