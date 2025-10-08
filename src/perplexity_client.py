import os
import requests
import json

# A Perplexity API kulcs beolvasása a környezeti változókból.
# A felhasználónak be kell állítania ezt a változót a szkript futtatása előtt.
# pl. export PPLX_API_KEY="az_api_kulcsod"
API_KEY = os.environ.get("PPLX_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

class PerplexityClient:
    """
    Egy kliens a Perplexity API használatához, ami megőrzi a beszélgetési
    kontextust a munkameneten belül. Ez a 2-es, "Perplexity Spaces"
    opció gyakorlati bemutatása.
    """
    def __init__(self, model="sonar-small-chat"):
        self.model = model
        # A beszélgetési előzményeket egy listában tároljuk.
        # A rendszerüzenet segít az MI-nek megérteni a szerepét.
        self.history = [
            {"role": "system", "content": "Légy egy segítőkész MI asszisztens."},
        ]

    def ask_perplexity(self, prompt):
        """
        Kérdést küld a Perplexity API-nak a teljes beszélgetési
        előzménnyel együtt.
        """
        if not API_KEY:
            return "Hiba: A PPLX_API_KEY környezeti változó nincs beállítva."

        # Az új felhasználói üzenet hozzáadása az előzményekhez
        self.history.append({"role": "user", "content": prompt})

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": self.history
        }

        try:
            print("Kérés küldése a Perplexity API-nak...")
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()

            data = response.json()
            ai_response = data['choices'][0]['message']['content']

            # Az MI válaszának hozzáadása az előzményekhez
            self.history.append({"role": "assistant", "content": ai_response})

            return ai_response

        except requests.exceptions.HTTPError as e:
            # Részletesebb hibaüzenet adása, különösen a 401 (Unauthorized) esetén
            if e.response.status_code == 401:
                return "Hiba: A Perplexity API visszautasította a kérést (401 Unauthorized). Valószínűleg érvénytelen az API kulcs."
            return f"Hiba történt az API hívás során: {e}"
        except requests.exceptions.RequestException as e:
            return f"Csatlakozási hiba: {e}"

if __name__ == "__main__":
    print("--- Perplexity API Kliens (2. Opció) ---")
    print("Ez a szkript a Perplexity API-t használja, és megőrzi a beszélgetés kontextusát.")

    if not API_KEY:
        print("\nFIGYELEM: A 'PPLX_API_KEY' környezeti változó nincs beállítva.")
        print("A szkript futtatása előtt add meg a kulcsodat, pl.:")
        print("export PPLX_API_KEY=\"pplx-xxxxxxxx...\"")
    else:
        print(f"API kulcs sikeresen betöltve.")

    print("Írj 'kilep' szót a befejezéshez.\n")

    client = PerplexityClient()

    while True:
        user_prompt = input("Te: ")
        if user_prompt.lower() == 'kilep':
            print("Viszlát!")
            break

        ai_answer = client.ask_perplexity(user_prompt)

        print("\n--- Perplexity MI Válasza ---")
        print(ai_answer)
        print("----------------------------\n")