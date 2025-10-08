import json
import os
from datetime import datetime
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# A HybridMemory osztályt itt is felhasználjuk az adatok tárolására
from hybrid_memory import HybridMemory

class RagMemory(HybridMemory):
    """
    Egy fejlettebb, RAG-alapú memória, ami a releváns kontextust
    hasonlóság alapján keresi ki a beszélgetési előzményekből.
    Ez az 1-es, "RAG Rendszer" opció megvalósítása.
    """

    def __init__(self, db_path="conversation_history.json"):
        """
        Inicializálja a RAG memória modult.
        """
        super().__init__(db_path)
        self.vectorizer = TfidfVectorizer()
        self.history_vectors = None
        if self.history:
            self._vectorize_history()

    def _vectorize_history(self):
        """
        A teljes beszélgetési előzményt (felhasználói és AI üzeneteket)
        vektorokká alakítja.
        """
        # A szövegeket egy listába gyűjtjük
        corpus = [f"{entry['user']} {entry['ai']}" for entry in self.history]
        if corpus:
            self.history_vectors = self.vectorizer.fit_transform(corpus)
        else:
            self.history_vectors = None

    def add_entry(self, user_message, ai_response):
        """
        Új bejegyzést ad az előzményekhez, és frissíti a vektorokat.
        """
        super().add_entry(user_message, ai_response)
        # A vektorizációt újra kell futtatni az új adattal
        self._vectorize_history()
        print("RAG memória frissítve és újravektorizálva.")

    def get_relevant_context(self, query, top_n=3):
        """
        Kikeresi a legrelevánsabb 'n' darab előzményt a query alapján.

        Args:
            query (str): A felhasználó aktuális üzenete/kérdése.
            top_n (int): A visszaadandó releváns bejegyzések száma.

        Returns:
            str: A formázott, releváns kontextus.
        """
        if not self.history or self.history_vectors is None:
            return "Nincs elegendő előzmény a kontextus kereséséhez."

        # A query-t is vektorizáljuk
        query_vector = self.vectorizer.transform([query])

        # Kiszámoljuk a koszinusz hasonlóságot
        similarities = cosine_similarity(query_vector, self.history_vectors).flatten()

        # Megkeressük a 'top_n' leghasonlóbb indexét, de a legutolsót kihagyjuk,
        # mert az a mostani üzenet, amit épp hozzáadtunk.
        # A -1 a mostani, -2 az előző, stb.
        # A `[:-1]` szeletelés eltávolítja a legutolsó elemet.
        if len(similarities) > 1:
            # A legutolsó bejegyzést (ami a jelenlegi) figyelmen kívül hagyjuk
            relevant_indices = np.argsort(similarities[:-1])[-top_n:]
        else:
            relevant_indices = []

        if not relevant_indices.any():
            return "Nem található releváns kontextus."

        # A releváns bejegyzések összegyűjtése és formázása
        context_entries = [self.history[i] for i in relevant_indices]

        # Időrendbe rakjuk őket, hogy a kontextus logikus legyen
        context_entries.sort(key=lambda x: x["timestamp"])

        formatted_context = "A legrelevánsabb előzmények:\n\n"
        for entry in context_entries:
            formatted_context += f"Felhasználó: {entry['user']}\n"
            formatted_context += f"AI: {entry['ai']}\n---\n"

        return formatted_context

def simulate_rag_conversation():
    """
    Egy egyszerű példa a RagMemory osztály használatára.
    """
    print("\nCodi Memória Szimulátor (RAG Modell - 1. Opció)")
    print("Írj 'kilep' szót a befejezéshez.")
    print("Példa: Kérdezz rá egy korábbi témára, pl. 'mit tanulsz?'")

    if not os.path.exists("memory"):
        os.makedirs("memory")

    memory_db_path = os.path.join("memory", "conversation_history.json")
    rag_memory = RagMemory(db_path=memory_db_path)

    # Előre feltöltjük a memóriát pár adattal, ha üres
    if not rag_memory.get_history():
        print("\n--- Memória előfeltöltése példa adatokkal ---")
        rag_memory.add_entry("Szia Codi!", "Szia! Miben segíthetek?")
        rag_memory.add_entry("Mit tanulsz éppen?", "Jelenleg a RAG rendszerek működését tanulmányozom.")
        rag_memory.add_entry("Milyen az idő?", "Nem rendelkezem valós idejű adatokkal az időjárásról.")
        rag_memory.add_entry("Melyik a kedvenc színed?", "Nincs kedvenc színem, mivel egy algoritmus vagyok.")
        print("--- Előfeltöltés kész ---\n")

    while True:
        user_input = input("Te: ")
        if user_input.lower() == 'kilep':
            print("Viszlát!")
            break

        # 1. Releváns kontextus kérése a RAG memóriától
        context = rag_memory.get_relevant_context(user_input)
        print("\n--- Releváns kontextus a memóriából ---")
        print(context)
        print("--------------------------------------\n")

        # 2. Szimulált "MI" válasz (a kontextust is felhasználhatná)
        ai_output = f"A '{user_input}' kérdésedre a kontextus alapján válaszolok. Most elmentem ezt a beszélgetést is."
        print(f"Codi: {ai_output}")

        # 3. Új bejegyzés hozzáadása a memóriához
        rag_memory.add_entry(user_input, ai_output)


if __name__ == "__main__":
    simulate_rag_conversation()