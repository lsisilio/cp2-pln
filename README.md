# cp2-pln
Atividade 2 de Processamento de Linguagem Natural utilizando spaCy

Relatório
Leonardo Sisilio - rm 99652

Resultados:
A Tokenização no spaCy tem por padrão o critério de separar pelas barras de espaço. Aqui mostro 10 exemplos de tokens, com suas classes gramaticais.
#
Pela NOUN
primeira ADP
vez NOUN
, PUNCT
o DET
Irã PROPN
realizou VERB
ataques NOUN
diretos NOUN
contra ADP
#

Para a Identificação de Entidades Nomeadas, optei por analisar as classes (labels) dos tokens. Elas podem ser separadas em pessoas, organizações, locais, eventos etc. No nosso texto, as cinco mais repetidas foram locais (e Estados homônimos).
#
Israel (LOC): 33
Irã (LOC): 20
Iraque (LOC): 4
Síria (LOC): 4
Teerã (LOC): 4
#

A Análise de Sentenças define qual o verbo raiz da frase e como os outros tokens dependem dele.
#
Sentença: No meio da noite de sábado, alertas de ataque aéreo dispararam em Israel.
Raiz: dispararam VERB
Dependências:
meio (obl) -> dispararam
alertas (nsubj) -> dispararam
Israel (obl) -> dispararam
. (punct) -> dispararam
#

Na Extração de Tópicos escolhi coletar os tokens de classe pessoa, local, organização e nacionalidades/grupos políticos, então ordená-los pelo número de repetições no texto.
#
Forças de Defesa de Israel
Conselho de Segurança
ONU
Hamas
BBC
Corpo da Guarda Revolucionária Islâmica
#

O Resumo Automático é mais complicado, nele decidi extrair os tópicos assim como na tarefa acima, e dar pontos as frases me baseando nisso. Ordenada a lista, imprimo as frases mais relevantes me mantendo num limite de 500 caracteres.
#
Resumo: Desde que a guerra em Gaza eclodiu há seis meses, Israel intensificou os seus movimentos contra o Irã, não apenas atacando o fornecimento de armas e infraestruturas na Síria, mas assassinando altos comandantes do Corpo da Guarda Revolucionária Islâmica (IRGC) do Irã e do Hezbollah (organização política e paramilitar fundamentalista islâmica, criada no Irã e presente no Líbano).
 Entre os inúmeros desdobramentos da guerra de Israel contra o Hamas na Faixa Gaza, a intensificação da inimizade entre Israel e o Irã é considerada a mais explosiva, escreve a correspondente internacional da BBC Lyse Doucet.
#
