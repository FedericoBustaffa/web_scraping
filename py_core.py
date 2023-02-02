
class persona:
    def __init__(self, nome, cognome, anno, occupazione):
        self.nome = nome
        self.cognome = cognome
        self.anno = anno
        self.occupazione = occupazione


if __name__ == "__main__":
    p = persona("Federico", "Bustaffa", 1999, "Studente")
    print(f"Nome: {p.nome}\nCognome: {p.cognome}")

