"""
iris_knn.py

Objetivo:
- Treinar e avaliar modelos clássicos (kNN, SVM e Random Forest) no dataset Iris.
- Persistir um artefato local (iris_report.json) contendo métricas e parâmetros do experimento.

Por que isso importa:
- Sem um "artefato" (arquivo gerado), o resultado fica apenas no console.
- Com o artefato, você pode versionar, auditar, aplicar hash/criptografia e evoluir o pipeline.
"""

# ---------------------------
# Bibliotecas padrão (Python)
# ---------------------------

import json
# json: serialização do relatório técnico (artefato) em um formato portátil e versionável.

from datetime import datetime
# datetime: adiciona timestamp no relatório para rastreabilidade.

# ---------------------------
# Bibliotecas de Machine Learning (scikit-learn)
# ---------------------------

from sklearn.datasets import load_iris
# load_iris: carrega o dataset Iris (clássico para classificação supervisionada).

from sklearn.model_selection import train_test_split
# train_test_split: separa os dados em treino e teste de forma reprodutível.

from sklearn.neighbors import KNeighborsClassifier
# KNeighborsClassifier: modelo kNN (classificador baseado em distância e vizinhos mais próximos).

from sklearn.svm import SVC
# SVC: Support Vector Classifier (modelo SVM para classificação).

from sklearn.ensemble import RandomForestClassifier
# RandomForestClassifier: ensemble de árvores de decisão (robusto e geralmente forte em baseline).

from sklearn.metrics import accuracy_score, confusion_matrix
# accuracy_score: mede acurácia (proporção de acertos).
# confusion_matrix: matriz de confusão (detalha acertos/erros por classe).


def evaluate(model, X_train, X_test, y_train, y_test, name: str) -> dict:
    """
    Treina o modelo, realiza predição e retorna métricas estruturadas.

    Parameters:
        model: instância sklearn (ainda não treinada)
        X_train, X_test: features de treino e teste
        y_train, y_test: rótulos de treino e teste
        name (str): rótulo legível do modelo (para relatório e logs)

    Returns:
        dict: métricas estruturadas para persistência em artefato JSON
    """

    # 1) Treinamento
    model.fit(X_train, y_train)

    # 2) Predição no conjunto de teste
    y_pred = model.predict(X_test)

    # 3) Métricas
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    # 4) Saída no console (diagnóstico humano imediato)
    print("\n" + "=" * 60)
    print(f"Modelo: {name}")
    print(f"Acurácia: {acc:.6f}")
    print("Matriz de confusão:")
    print(cm)

    # 5) Retorno estruturado (para compor o artefato)
    return {
        "model": name,
        "accuracy": float(acc),
        "confusion_matrix": cm.tolist(),
    }


if __name__ == "__main__":
    # ---------------------------------------------------------------------
    # 1) Carregar dataset Iris
    # ---------------------------------------------------------------------
    iris = load_iris()

    # ---------------------------------------------------------------------
    # 2) Selecionar features
    # Observação: você escolheu apenas as sépalas (features mais difíceis)
    # Índices no iris.data:
    #   0 = sepal length
    #   1 = sepal width
    #   2 = petal length
    #   3 = petal width
    # ---------------------------------------------------------------------
    X = iris.data[:, [0, 1]]
    y = iris.target

    # ---------------------------------------------------------------------
    # 3) Separar treino e teste (reprodutível via random_state)
    # ---------------------------------------------------------------------
    test_size = 0.2
    random_state = 42

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    # ---------------------------------------------------------------------
    # 4) Avaliar modelos e coletar resultados
    # ---------------------------------------------------------------------
    results = []

    # Modelo 1: kNN
    # Observação: seu código tinha "k=5" no texto, mas n_neighbors=4.
    # Aqui, mantemos coerente: k=4.
    knn_k = 4
    knn = KNeighborsClassifier(n_neighbors=knn_k)
    results.append(evaluate(knn, X_train, X_test, y_train, y_test, f"kNN (k={knn_k})"))

    # Modelo 2: SVM Linear
    svm = SVC(kernel="linear")
    results.append(evaluate(svm, X_train, X_test, y_train, y_test, "SVM (kernel=linear)"))

    # Modelo 3: Random Forest
    rf_trees = 200
    rf = RandomForestClassifier(n_estimators=rf_trees, random_state=random_state)
    results.append(
        evaluate(rf, X_train, X_test, y_train, y_test, f"Random Forest ({rf_trees} árvores)")
    )

    # ---------------------------------------------------------------------
    # 5) Criar e salvar o artefato local (iris_report.json)
    # Esse arquivo será o "output auditável" do pipeline Iris.
    # ---------------------------------------------------------------------
    report = {
        "created_at_utc": datetime.utcnow().isoformat() + "Z",
        "dataset": "sklearn.datasets.load_iris",
        "features_used": {
            "indices": [0, 1],
            "names": ["sepal_length", "sepal_width"],
        },
        "split": {
            "test_size": test_size,
            "random_state": random_state,
        },
        "classes": {
        "labels": [int(label) for label in set(y)],
        "names": [str(name) for name in iris.target_names],
},

        "results": results,
    }

    output_file = "iris_report.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

    print("\n" + "-" * 60)
    print(f"Relatório técnico salvo em: {output_file}")
