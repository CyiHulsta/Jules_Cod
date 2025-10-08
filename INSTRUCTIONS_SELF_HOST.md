# Útmutató: Saját Nyílt Forráskódú MI Modell Hosztolása (3. Opció)

Ez az útmutató lépésről lépésre bemutatja, hogyan telepíthetsz és futtathatsz egy nyílt forráskódú nagy nyelvi modellt (LLM) a saját szervereden. Ez a megoldás teljes kontrollt, adatvédelmet és potenciálisan alacsonyabb hosszú távú költségeket biztosít.

Az útmutató az **Ollama** nevű eszközt használja, ami jelentősen leegyszerűsíti a modellek telepítését és kezelését.

---

## 1. Előfeltételek

Mielőtt belevágnál, győződj meg róla, hogy a rendszered megfelel a következő követelményeknek.

### Hardver
- **GPU:** Erősen ajánlott egy modern NVIDIA GPU, legalább 8 GB VRAM-mal. Minél nagyobb a modell, annál több VRAM-ra lesz szükséged. A professzionális kártyák (pl. H100, A100) a legjobbak, de a konzumer kártyák (pl. RTX 30xx, 40xx sorozat) is kiválóan működnek.
- **RAM:** Legalább 16 GB RAM.
- **Tárhely:** Legalább 20-50 GB szabad SSD tárhely a modellek számára.

### Szoftver
- **Operációs rendszer:** Linux (ajánlott) vagy macOS. A Windows a WSL2-n keresztül támogatott.
- **NVIDIA Driverek:** A megfelelő, naprakész NVIDIA driverek telepítve kell, hogy legyenek.
- **CUDA Toolkit:** Az NVIDIA driverekhez illeszkedő CUDA Toolkit. Az Ollama ezt sok esetben automatikusan kezeli, de a manuális telepítés a legbiztosabb.

---

## 2. Telepítési Lépések

### 1. Lépés: Ollama Telepítése

Az Ollama telepítése rendkívül egyszerű. Nyiss egy terminált, és futtasd a következő parancsot:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Ez a szkript letölti és telepíti az Ollama-t a rendszeredre, és beállítja szolgáltatásként.

### 2. Lépés: Modell Letöltése és Futtatása

Az Ollama telepítése után már le is tölthetsz egy modellt. Az eredeti javaslatban szereplő modellek közül a `Qwen` elérhető az Ollama könyvtárában.

1.  **Modell letöltése:** Töltsük le a Qwen modell egy kisebb, 7 milliárd paraméteres változatát.
    ```bash
    ollama pull qwen
    ```
    Ez a parancs letölti a modell súlyait. Légy türelmes, ez több GB adat is lehet.

2.  **Modell futtatása (interaktív chat):** A modell futtatásához és a vele való csevegéshez használd a `run` parancsot.
    ```bash
    ollama run qwen
    ```
    Ezzel elindul egy interaktív chat a terminálban, ahol már beszélgethetsz is a modellel. A kilépéshez írd be: `/bye`.

---

## 3. Modell Használata API-n Keresztül

Az Ollama egyik legnagyobb előnye, hogy automatikusan biztosít egy OpenAI-kompatibilis REST API-t a futó modellekhez. Ez lehetővé teszi, hogy bármilyen programozási nyelvről vagy alkalmazásból meghívd a saját MI modelledet.

Az API alapértelmezetten a `http://localhost:11434` címen érhető el.

### Példa: `curl` parancs

Egy egyszerű kérést a `curl` segítségével is küldhetsz a modellnek:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen",
  "prompt": "Miért kék az ég?",
  "stream": false
}'
```

### Példa: Python szkript

Készíthetsz egy Python szkriptet is, ami a `requests` könyvtár segítségével kommunikál a modellel.

```python
import requests
import json

def ask_local_ai(prompt):
    """
    Kérdést küld a lokálisan futó Ollama modellnek.
    """
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "qwen", # A használni kívánt modell neve
        "prompt": prompt,
        "stream": False # Ha True lenne, a válasz darabokban érkezne
    }

    try:
        response = requests.post(url, data=json.dumps(payload))
        response.raise_for_status() # Hiba dobása, ha a kérés sikertelen

        # A válasz feldolgozása
        data = response.json()
        return data['response']

    except requests.exceptions.RequestException as e:
        return f"Hiba történt az API hívás során: {e}"

# Példa használat
if __name__ == "__main__":
    user_prompt = "Magyarázd el a fekete lyukak működését egyszerűen."
    ai_answer = ask_local_ai(user_prompt)

    print("--- Kérdés ---")
    print(user_prompt)
    print("\n--- A Lokális MI Válasza ---")
    print(ai_answer)

```

Ezt a szkriptet elmentheted `local_ai_client.py` néven, és futtathatod. A `requests` csomag telepítése szükséges (`pip install requests`).

---

## 4. Összegzés

Gratulálok! Sikeresen telepítettél és futtattál egy nagy nyelvi modellt a saját gépeden az Ollama segítségével. Most már képes vagy:
- Interaktívan csevegni a modellel.
- API-n keresztül integrálni a modellt a saját alkalmazásaidba, teljes kontrollt élvezve a folyamat felett.

Ezzel a 3-as opció, a "Self-Hosted Codi" megvalósításának alapjait fektetted le. Innen már csak a fantáziád szab határt.