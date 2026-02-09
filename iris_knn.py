from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier




def evaluate(model, X_train, X_test, y_train, y_test, name: str):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\n" + "=" * 44)
    print(name)
    print("Acurácia:", acc)
    print("Matriz de confusão:\n", cm)


if __name__ == "__main__":
    # 1) carregar dataset
    iris = load_iris()

   # usando apenas sépalas (features mais difíceis)
   # índices: 0 = sepal length, 1 = sepal width
    X = iris.data[:, [0, 1]]

   
    y = iris.target

    # 2) FIXAR split (mesmas amostras sempre)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3) algoritmo 1: kNN
    knn = KNeighborsClassifier(n_neighbors=4)
    evaluate(knn, X_train, X_test, y_train, y_test, "kNN (k=5)")

    # 4) algoritmo 2: SVM (linear)
    svm = SVC(kernel="linear")
    evaluate(svm, X_train, X_test, y_train, y_test, "SVM (kernel=linear)")

    # 5) algoritmo 3: Random Forest
    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    evaluate(rf, X_train, X_test, y_train, y_test, "Random Forest (200 árvores)")

    print(set(y))


