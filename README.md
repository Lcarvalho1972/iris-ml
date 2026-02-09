🌸 Iris Dataset — Hello World de Machine Learning
Este repositório apresenta um exercício introdutório de Machine Learning supervisionado, utilizando o clássico dataset Iris.
O objetivo é entender conceitos fundamentais, mais do que “otimizar modelos”.
Pense neste projeto como o Hello World do ML: simples, didático e conceitualmente completo.

🌼 O que é o dataset Iris?
O dataset Iris é um conjunto de dados clássico da estatística e do Machine Learning, criado por Ronald Fisher (1936).
Ele contém 150 amostras de flores do gênero Iris, divididas em três espécies:
Setosa
Versicolor
Virginica
Cada flor foi medida fisicamente em laboratório.

🌿 Sépala e Pétala — o que são?
Cada flor possui duas estruturas principais:
Sépala → parte externa da flor (proteção)
Pétala → parte interna, geralmente colorida
Para cada flor, foram feitas quatro medições:
Estrutura
Medida
Sépala
Comprimento
Sépala
Largura
Pétala
Comprimento
Pétala
Largura


📐 Representação matemática dos dados
Os dados não são “flores” para o algoritmo.
Eles são representados como vetores numéricos.
Forma do dataset
150 flores
Cada flor → vetor em ℝ⁴
Dataset completo → matriz 150 × 4
X ∈ ℝ^(150×4)

Visualmente:
X = [
  [sepal_len, sepal_wid, petal_len, petal_wid],  ← flor 1
  [sepal_len, sepal_wid, petal_len, petal_wid],  ← flor 2
  ...
  [sepal_len, sepal_wid, petal_len, petal_wid]   ← flor 150
]

👉 Classificar flores = classificar vetores em um espaço multidimensional

🎯 Objetivo do exercício
Construir um pipeline básico de ML supervisionado, contendo:
Separação treino / teste
Treinamento de modelos
Predição
Avaliação por acurácia e matriz de confusão
Comparação entre algoritmos

🔀 Separação Treino / Teste
Utilizamos:
80% para treino
20% para teste
random_state = 42 para reprodutibilidade
📌 O modelo aprende apenas com o treino
📌 O teste funciona como uma “prova que ele nunca viu”

🤖 Algoritmos utilizados
Este projeto testa três algoritmos clássicos de classificação:
1️⃣ k-Nearest Neighbors (kNN)
Classifica pela distância entre vetores
Sensível à escolha das features
Muito intuitivo para fins didáticos
2️⃣ Support Vector Machine (SVM)
Busca uma fronteira ótima de separação
Funciona bem mesmo com menos informação
Forte em espaços de baixa dimensão
3️⃣ Random Forest
Conjunto de árvores de decisão
Mais robusto, menos sensível a ruído
Serve como bom “baseline moderno”

🧪 Experimento didático central
Experimento 1 — Todas as features (ℝ⁴)
Usando:
sépalas + pétalas
📌 Resultado esperado:
Acurácia próxima de 1.0
Matrizes de confusão quase perfeitas
👉 Mostra que o problema é facilmente separável quando há informação suficiente.

Experimento 2 — Apenas sépalas (ℝ²)
Usando:
comprimento e largura da sépala
📌 Resultado observado:
kNN ≈ 0.70
SVM ≈ 0.90
Random Forest ≈ 0.76
👉 Aqui fica claro que:
Reduzir features reduz informação
Algoritmos reagem de forma diferente à mesma limitação
Este é o aprendizado mais importante do exercício.

📊 Matriz de Confusão — por que usamos?
A matriz de confusão mostra:
acertos
erros
quais classes são confundidas
Os valores na diagonal principal representam:
classificações corretas
Fora da diagonal:
erros de classificação entre espécies
👉 Ela explica o tipo de erro, não só “quanto errou”.

🧠 Por que isso é o “Hello World do ML”?
Porque neste exercício você aprende:
o que são features
o que é label
o que é vetor
o que é treino vs teste
como avaliar um modelo
por que dados importam tanto quanto algoritmos
Sem:
deep learning
tuning excessivo
abstrações mágicas

🚀 Conclusão
Machine Learning começa com geometria, não com IA.
Este projeto mostra que ML é, antes de tudo:
matemática aplicada
representação de dados
tomada de decisão baseada em exemplos
Um verdadeiro Hello World, feito do jeito certo.