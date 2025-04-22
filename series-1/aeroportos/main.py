import pandas as pd

# Carrega o CSV
df = pd.read_csv("voos.csv", sep=";")  # ajuste o separador se necessário

# Colunas que nos interessam
colunas = [
    "Sigla ICAO Aeroporto Origem", "Descrição Aeroporto Origem",
    "Partida Prevista",
    "Sigla ICAO Aeroporto Destino", "Descrição Aeroporto Destino",
    "Chegada Prevista"
]

df = df[colunas].dropna()

# Início do conteúdo DOT
dot = ["digraph aeroportos {"]

# Criar conjunto único de aeroportos
aeroportos = set()

for _, row in df.iterrows():
    origem_sigla = row["Sigla ICAO Aeroporto Origem"]
    origem_nome = row["Descrição Aeroporto Origem"]
    destino_sigla = row["Sigla ICAO Aeroporto Destino"]
    destino_nome = row["Descrição Aeroporto Destino"]

    aeroportos.add((origem_sigla, origem_nome))
    aeroportos.add((destino_sigla, destino_nome))

# Adiciona os nós (aeroportos)
for sigla, nome in aeroportos:
    dot.append(f'    {sigla} [label="{nome} - {sigla}"];')

# Adiciona as arestas (voos)
for _, row in df.iterrows():
    origem = row["Sigla ICAO Aeroporto Origem"]
    destino = row["Sigla ICAO Aeroporto Destino"]
    partida = row["Partida Prevista"]
    chegada = row["Chegada Prevista"]
    label = f"{partida} → {chegada}"
    dot.append(f'    {origem} -> {destino} [label="{label}", partida="{partida}", chegada="{chegada}"];')

# Fecha o grafo
dot.append("}")

# Salva o arquivo
with open("aeroportos.dot", "w", encoding="utf-8") as f:
    f.write("\n".join(dot))

print("Arquivo DOT gerado com sucesso: aeroportos.dot")
