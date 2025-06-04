import re

class Logradouro:
    def __init__(self, tipos_logradouro):
        self.tipos = tipos_logradouro
                     
    def separar_logradouro(self, logradouro):
        logradouro = ' '.join(logradouro.strip().split())  # Remove espaços duplos
        pattern = r'^(' + '|'.join(self.tipos) + r')\s+(.*)'
        match = re.match(pattern, logradouro, re.IGNORECASE)
        if match:
            tipo = match.group(1).upper()
            nome = match.group(2).strip()
            return tipo, nome
        else:
            return "RUA", logradouro


if __name__ == '__main__':
    tipos_logradouro = [
        "RUA", "AVENIDA", "ESTRADA", "RODOVIA", "TRAVESSA",
        "ALAMEDA", "PRAÇA", "LADEIRA", "VIA", "VILA",
        "CAMINHO", "VIADUTO", "LARGO", "PARQUE", "BECO", "PASSAGEM"
    ]
    
    logradouro = Logradouro(tipos_logradouro)

    tipo, nome = logradouro.separar_logradouro("Avenida Paulista")
    print(f"Tipo: {tipo}, Nome: {nome}")

    tipo, nome = logradouro.separar_logradouro("Rua das Flores")
    print(f"Tipo: {tipo}, Nome: {nome}")

    tipo, nome = logradouro.separar_logradouro("Praça da Sé")
    print(f"Tipo: {tipo}, Nome: {nome}")

    tipo, nome = logradouro.separar_logradouro("Beco do Batman")
    print(f"Tipo: {tipo}, Nome: {nome}")
