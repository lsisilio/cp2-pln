# Setup
import spacy
from collections import Counter
nlp = spacy.load('pt_core_news_sm')
print('Processando... (demora um pouco)')

# Carregando notícia
with open("noticia.txt", "r", encoding="utf-8") as f:
    texto = f.read()
doc = nlp(texto)

# Tokenização
def tokenizar(file):
  print('####TOKENIZAÇÃO####')
  # Exibindo apenas os primeiro 20 tokens para não inundar o terminal
  counter = 0
  for token in file:
    print(token.text, token.pos_)
    counter += 1
    if counter == 20:
      break

# Identificação de Entidades Nomeadas (NER)
def identificar_en(file):
  print(f'\n#### IDENTIFICAÇÃO DE ENTIDADES NOMEADAS ####')
  # Contando quantas vezes cada entidade aparece
  entities_counter = Counter([(ent.text, ent.label_) for ent in file.ents])
  # Ordenando pelas que mais aparecem
  sorted_entities = sorted(entities_counter.items(), key=lambda x: x[1], reverse=True)
  # Imprimindo as 10 entidades mais repetidas
  for (ent, label), frequency in sorted_entities[:10]:
    print(f'{ent} ({label}): {frequency}')

# Análise de sentenças
def analisar_sentencas(file):
  print(f'\n#### ANÁLISE DE SENTENÇAS ####\n')
  # Analisando apenas 5 sentenças para não inundar o terminal
  counter = 0
  for sent in file.sents:
    print(sent.text)
    print("Raiz:", sent.root.text, sent.root.pos_)
    print("Dependências:")
    for child in sent.root.children:
        print(f"{child.text} ({child.dep_}) -> {sent.root.text}")
    counter += 1
    if counter == 5:
      break

# Extração de tópicos
def extrair_topicos(file):
  print(f'\n#### EXTRAÇÃO DE TÓPICOS ####\n')
  # Coletando as pessoas, organizações e locais
  topics = [ent.text for ent in file.ents if ent.label_ in ["GPE", "ORG", "PERSON", "NORP"]]
  # Contando quantas vezes se repetem
  topics_counter = Counter(topics)
  # Ordenando por quantidades de vezes
  sorted_topics = sorted(topics_counter.items(), key=lambda x: x[1], reverse=True)
  # Extraindo apenas os 10 tópicos mais citados
  topics = [topic for topic, _ in sorted_topics[:10]]
  print('Principais tópicos:')
  for topic in topics:
    print(topic)

# Resumo automático
def resumir_texto(file):
  print(f'\n#### RESUMO ####')
  # Identificando as frases mais relevantes
  relevancia_sentencial = {}
  # Sentenças começam com valor 0
  for sent in file.sents:
    relevancia_sentencial[sent] = 0.0
    # Ganha um ponto a cada PESSOA, ORGANIZAÇÃO ou LOCAL
    for ent in sent.ents:
      if ent.label_ in ("PERSON", "ORG", "GPE", "NORP"):
        relevancia_sentencial[sent] += 1.0
  # Meio ponto se forem outros SUBSTANTIVOS ou VERBOS
  for token in file:
    if token.pos_ in ("NOUN", "VERB", "PROPN"):
      relevancia_sentencial[token.sent] += 0.5
  # Ordenando as frases por relevância
  frases_ordenadas = sorted(relevancia_sentencial.items(), key=lambda x: x[1], reverse=True)
  # Construindo o resumo
  resumo = ""
  for sent, score in frases_ordenadas:
    if score > 0.0:
      resumo += sent.text + " "
      if len(resumo) > 500:
        break
  return resumo.strip()

# Resultados
tokenizar(doc)
identificar_en(doc)
analisar_sentencas(doc)
extrair_topicos(doc)
resumo = resumir_texto(doc)
print(f"Resumo: {resumo}")