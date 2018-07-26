# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def main() -> None:
    iris = load_iris()
    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(iris.data, iris.target)

    # sepal length, sepal width, petal length, petal width
    X = np.array([[5.0, 2.9, 1.0, 4.85]])
    #X = np.array([[5.0, 2.9, 1.0, 0.2]])
    print(clf.predict(X))
    print(clf.decision_path(X))
    print(clf.decision_path(X).todense())
    with open('iris-dtree.dot', mode='w') as f:
        export_graphviz(clf, out_file=f,
                        rounded=True,
                        feature_names=iris.feature_names,
                        class_names=iris.target_names,
                        special_characters=True)


if __name__ == '__main__':
    main()
