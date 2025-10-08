import json
import os
from datetime import datetime, timezone

class HybridMemory:
    """
    Egy egyszerű, fájl-alapú memória megvalósítás, ami a beszélgetési
    előzményeket egy JSON fájlban tárolja. Ez a 4-es, "Hibrid" opció
    alapját képezi.
    """

    def __init__(self, db_path="conversation_history.json"):
        """
        Inicializálja a memória modult.

        Args:
            db_path (str): Az adatbázis fájl elérési útja.
        """
        self.db_path = db_path
        self.history = self._load_history()

    def _load_history(self):
        """
        Betölti a beszélgetési előzményeket a JSON fájlból.
        Ha a fájl nem létezik, üres listát ad vissza.
        """
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Hiba a memória betöltése közben: {e}. Új memória jön létre.")
                return []
        return []

    def _save_history(self):
        """
        Elmenti a teljes beszélgetési előzményt a JSON fájlba.
        """
        try:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Hiba a memória mentése közben: {e}")

    def add_entry(self, user_message, ai_response):
        """
        Új bejegyzést ad a beszélgetési előzményekhez.

        Args:
            user_message (str): A felhasználó üzenete.
            ai_response (str): Az MI válasza.
        """
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "user": user_message,
            "ai": ai_response
        }
        self.history.append(entry)
        self._save_history()
        print("Memória frissítve.")

    def get_history(self):
        """
        Visszaadja a teljes beszélgetési előzményt.

        Returns:
            list: A beszélgetési bejegyzések listája.
        """
        return self.history

    def get_context(self, last_n=5):
        """
        Visszaadja az utolsó 'n' bejegyzést formázott szövegként,
        ami kontextusként használható egy MI számára.

        Args:
            last_n (int): Az utolsó hány bejegyzést kérjük le.

        Returns:
            str: A formázott kontextus.
        """
        context_entries = self.history[-last_n:]
        formatted_context = "A beszélgetés előzményei:\n\n"
        for entry in context_entries:
            formatted_context += f"Felhasználó: {entry['user']}\n"
            formatted_context += f"AI: {entry['ai']}\n---\n"
        return formatted_context


def simulate_conversation():
    """
    Egy egyszerű példa a HybridMemory osztály használatára.
    """
    print("Codi Memória Szimulátor (Hibrid Modell - 4. Opció)")
    print("Írj 'kilep' szót a befejezéshez.")

    # A memóriát a 'memory' mappában tároljuk, hogy rend legyen.
    if not os.path.exists("memory"):
        os.makedirs("memory")

    memory_db_path = os.path.join("memory", "conversation_history.json")
    memory = HybridMemory(db_path=memory_db_path)

    # Előzmények kiírása, ha vannak
    if memory.get_history():
        print("\n--- Korábbi beszélgetés betöltve ---")
        print(memory.get_context(last_n=10)) # Akár 10 korábbi üzenet
        print("--- Beszélgetés folytatása ---\n")


    while True:
        user_input = input("Te: ")
        if user_input.lower() == 'kilep':
            print("Viszlát!")
            break

        # Egyszerű, szabály-alapú "MI" válasz a szimulációhoz
        ai_output = f"Megkaptam az üzeneted: '{user_input}'. Ezt most elmentem a memóriámba."

        print(f"Codi: {ai_output}")

        # Bejegyzés hozzáadása a memóriához
        memory.add_entry(user_input, ai_output)


if __name__ == "__main__":
    simulate_conversation()