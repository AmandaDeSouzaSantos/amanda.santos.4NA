import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import os

st.title("🎥 Recomendação de Filmes do Studio Ghibli com Análise de Sentimentos")
st.markdown("""
Com base no que você está sentindo, esta aplicação recomenda filmes do Studio Ghibli que combinam com ou contrastam com seu sentimento atual.
""")

@st.cache_resource
def carregar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(
        "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    )
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

analisador = carregar_modelo()

# Carrega os dados dos filmes
if not os.path.exists('ghibli_filmes.csv'):
    st.error("❌ Arquivo CSV não encontrado. Execute o script `obter_filmes.py` para gerar os dados.")
    st.stop()

filmes_df = pd.read_csv('ghibli_filmes.csv')

frase = st.text_input("🗣️ Como você está se sentindo? Escreva com suas palavras:")

romance = st.checkbox("Quero filmes com romance")
fantasy = st.checkbox("Quero filmes de fantasia")

if frase:
    resultado = analisador(frase)[0]
    sentimento_raw = resultado["label"].lower()
    score = resultado["score"]

    mapeamento_sentimentos = {
        'positive': 'happy',
        'negative': 'sad',
        'mixed': 'neutral',
        'neutral': 'neutral'
    }

    sentimento_mapeado = mapeamento_sentimentos.get(sentimento_raw, 'neutral')

    st.markdown(f"🧠 Sentimento detectado: **{sentimento_raw.upper()}** (confiança: {score:.2f})")

    escolha = st.radio(
        "Você quer um filme que:",
        ["complemente esse sentimento", "acentue esse sentimento"]
    )

    sentimentos_opostos = {
        'happy': 'sad',
        'sad': 'happy',
        'neutral': 'neutral'
    }

    if escolha == "complemente esse sentimento":
        sentimento_alvo = sentimentos_opostos[sentimento_mapeado]
    else:
        sentimento_alvo = sentimento_mapeado

    st.write(f"🎯 Sentimento alvo para recomendação: **{sentimento_alvo}**")

    recomendados = filmes_df[
        (filmes_df['sentimento'] == sentimento_alvo) &
        ((filmes_df['romance'] == romance) if romance else True) &
        ((filmes_df['fantasia'] == fantasy) if fantasy else True)
    ]

    if recomendados.empty:
        st.info("🔍 Nenhum filme encontrado com esses filtros. Mostrando sugestões apenas com base no sentimento.")
        recomendados = filmes_df[filmes_df['sentimento'] == sentimento_alvo]

    st.subheader("🎬 Recomendação de filme(s):")
    if not recomendados.empty:
        for _, f in recomendados.iterrows():
            st.markdown(f"**{f['titulo']}** — _{f['descricao']}_")
    else:
        st.warning("😕 Não encontrei filmes para esse sentimento com as preferências escolhidas.")
