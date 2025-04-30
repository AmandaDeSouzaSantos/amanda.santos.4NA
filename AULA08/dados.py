import requests
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

if not api_key:
    raise ValueError("❌ Chave da API TMDb não encontrada. Verifique se o arquivo .env contém TMDB_API_KEY.")

def obter_e_salvar_filmes():
    url = "https://api.themoviedb.org/3/company/10342/movies"
    params = {
        "api_key": api_key,
        "language": "pt-BR",
        "sort_by": "release_date.asc"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"❌ Erro ao obter dados da API: {response.status_code} - {response.text}")

    films = response.json().get('results', [])


    data = {
        'titulo': [film.get('title', '') for film in films],
        'descricao': [film.get('overview', '') for film in films],
        'sentimento': ['neutral'] * len(films),
        'romance': [False] * len(films),
        'fantasia': [True] * len(films)  
    }

    df = pd.DataFrame(data)

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

    for titulo, atributos in filmes_atributos.items():
        if titulo in df['titulo'].values:
            df.loc[df['titulo'] == titulo, 'sentimento'] = atributos['sentimento']
            df.loc[df['titulo'] == titulo, 'romance'] = atributos['romance']
            df.loc[df['titulo'] == titulo, 'fantasia'] = atributos['fantasia']

    df.to_csv('ghibli_filmes.csv', index=False, encoding='utf-8')
    print("✅ Dados dos filmes salvos em ghibli_filmes.csv")

if __name__ == "__main__":
    obter_e_salvar_filmes()


