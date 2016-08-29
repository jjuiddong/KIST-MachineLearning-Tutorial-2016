import sklearn.decomposition
import numpy as np
import pandas as pd
#import elice_utils


def main():
    df = input_data()

    # 2
    pca, pca_array = run_PCA(df, 1)

    # 4
    #elice_utils.draw_toy_example(df, pca, pca_array)


def input_data():
    # 1
    first_line = input().strip()  # receice first line
    n = int(first_line)

    row2 = []
    for i in range(n):
        row2.append([])

    for i in range(n):
        line = input().strip()
        row = line.split(" ")
        for j in range(2):
            row2[j].append(float(row[j]))

    df = pd.DataFrame({'x': row2[0], 'y': row2[1]})
    return df


def run_PCA(df, num_components):
    # 2
    pca = sklearn.decomposition.PCA(n_components=num_components)
    pca.fit(df)
    pca_array = pca.transform(df)
    return pca, pca_array


if __name__ == '__main__':
    main()
