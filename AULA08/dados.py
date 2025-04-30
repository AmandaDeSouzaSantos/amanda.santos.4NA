import pandas as pd

# Dicionário completo dos filmes
filmes_atributos = {
    'Meu Amigo Totoro': {'sentimento': 'happy', 'romance': False, 'fantasia': True},
    'A Viagem de Chihiro': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'O Castelo Animado': {'sentimento': 'sad', 'romance': True, 'fantasia': True},
    'O Conto da Princesa Kaguya': {'sentimento': 'neutral', 'romance': True, 'fantasia': False},
    'O Serviço de Entregas da Kiki': {'sentimento': 'happy', 'romance': False, 'fantasia': True},
    'Porco Rosso': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Pompoko': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Sussurros do Coração': {'sentimento': 'happy', 'romance': True, 'fantasia': False},
    'Princesa Mononoke': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Meus Vizinhos, os Yamadas': {'sentimento': 'happy', 'romance': False, 'fantasia': False},
    'O Reino dos Gatos': {'sentimento': 'happy', 'romance': False, 'fantasia': True},
    'Contos de Terramar': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Ponyo - Uma Amizade que Veio do Mar': {'sentimento': 'happy', 'romance': False, 'fantasia': True},
    'Arrietty e o Mundo dos Diminutos': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Vidas ao Vento': {'sentimento': 'sad', 'romance': False, 'fantasia': True},
    'Marnie - O Segredo': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'As Memórias de Marnie': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'A Tartaruga Vermelha': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'O Mundo dos Pequeninos': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Túmulo dos Vagalumes': {'sentimento': 'sad', 'romance': False, 'fantasia': False},
    'Laputa: O Castelo no Céu': {'sentimento': 'happy', 'romance': False, 'fantasia': True},
    'Nausicaä do Vale do Vento': {'sentimento': 'neutral', 'romance': False, 'fantasia': True},
    'Omoide Poroporo': {'sentimento': 'sad', 'romance': True, 'fantasia': False},
    'Ocean Waves': {'sentimento': 'neutral', 'romance': True, 'fantasia': False},
    'Earwig e a Bruxa': {'sentimento': 'neutral', 'romance': False, 'fantasia': True}
}

# Converte o dicionário em DataFrame
df = pd.DataFrame([
    {"titulo": titulo, **atributos} for titulo, atributos in filmes_atributos.items()
])

# Salva o DataFrame como CSV
df.to_csv("ghibli_filmes.csv", index=False, encoding='utf-8')
print("✅ CSV salvo com sucesso.")
