🌸 Iris Dataset — Pipeline Reprodutível de Classificação Supervisionada
1. Visão Geral

Este repositório implementa um pipeline reprodutível de Machine Learning supervisionado utilizando o clássico dataset Iris.

O objetivo não é otimizar hiperparâmetros ou atingir máxima performance, mas compreender:

Representação vetorial dos dados

Separação treino/teste

Comportamento comparativo de algoritmos

Avaliação estruturada de modelos

Geração de artefato auditável

Este projeto funciona como o “Hello World” do Machine Learning clássico.

2. Fundamentação Teórica
2.1 Dataset Iris

Criado por Ronald Fisher (1936), contém:

150 amostras

3 classes:

Setosa

Versicolor

Virginica

4 features numéricas:

Comprimento da sépala

Largura da sépala

Comprimento da pétala

Largura da pétala

2.2 Representação Matemática

Cada flor é representada como um vetor em ℝ⁴:

𝑋
∈
R
150
×
4
X∈R
150×4

Classificar flores equivale a classificar vetores em um espaço multidimensional.

3. Metodologia Experimental
3.1 Separação Treino/Teste

80% treino

20% teste

random_state = 42 para reprodutibilidade

O conjunto de teste funciona como validação externa.

3.2 Algoritmos Avaliados
1️⃣ k-Nearest Neighbors (kNN)

Classificação baseada em distância

Sensível à escolha das features

2️⃣ Support Vector Machine (SVM)

Busca fronteira ótima de separação

Robusto em baixa dimensionalidade

3️⃣ Random Forest

Ensemble de árvores de decisão

Menos sensível a ruído

4. Experimento Didático Central
Experimento 1 — ℝ⁴ (todas as features)

Separabilidade quase perfeita.
Acurácia próxima de 1.0.

Experimento 2 — ℝ² (apenas sépalas)

Redução de informação → redução de desempenho.

Resultados observados:

Modelo	Acurácia
kNN (k=4)	~0.70
SVM (linear)	~0.90
Random Forest	~0.76

Conclusão:
Algoritmos reagem de forma diferente à limitação informacional.

5. Avaliação

Utiliza-se:

Accuracy

Matriz de Confusão

A matriz permite analisar:

Acertos por classe

Erros entre espécies

Padrões de confusão

6. Arquitetura do Projeto
iris-ml/
├── iris_knn.py          # Pipeline principal
├── iris_report.json     # Artefato gerado (output estruturado)
├── README.md
└── .venv/

7. Artefato Gerado

O script gera automaticamente:

iris_report.json


Conteúdo:

Timestamp UTC

Dataset utilizado

Features selecionadas

Parâmetros de split

Métricas por modelo

Matrizes de confusão estruturadas

Isso transforma o exercício em um pipeline auditável e versionável.

8. Como Executar
8.1 Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

8.2 Instalar dependências
pip install scikit-learn

8.3 Executar pipeline
python3 iris_knn.py


O artefato iris_report.json será gerado no diretório raiz.

9. Evoluções Técnicas Possíveis

Este projeto pode evoluir para:

Persistência de modelos (joblib)

Versionamento de experimentos

Aplicação de hash SHA-256 no artefato

Criptografia de outputs

Integração com pipelines de segurança

Deploy em ambiente cloud (Azure ML)

10. Conclusão

Machine Learning começa com:

Representação geométrica

Estruturação de dados

Decisão supervisionada

Antes de qualquer deep learning, existe matemática, separabilidade e generalização.

Este projeto demonstra esses fundamentos de forma controlada, reprodutível e auditável.