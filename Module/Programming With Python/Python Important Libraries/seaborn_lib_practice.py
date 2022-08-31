# Seaborn library builds on matplotlib library, however, this library is a complement to matplotlib,
# not a replacement.
# It was specifically developed for statistical data visuali- zation.
# Seaborn provides the following features for data visualization:
# Develops themes for styling matplotlib graphics, visualizes univariate and bivariate array data,
# fits in and visualizes linear and non-linear regression models, excellent plotting
# for statistical time series data, built to work effectively with NumPy and pandas data structures,
# pro- vides new themes for styling matplotlib plots, etc.
# Seaborn can be installed using “pip install seaborn” or “conda install seaborn” with the Anaconda Distribution package.

import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


def main():
    iris_data = sns.load_dataset("iris")
    style.use('ggplot')

    # swarm plot example
    sns.swarmplot(x="species", y="petal_length", data=iris_data)
    plt.text(40, 7, "abc")
    plt.ylabel("patel length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    # factor plot example
    g = sns.factorplot("species", "petal_length", data=iris_data, kind="bar",
                       palette="muted", legend=False)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    # box plot example
    sns.boxplot(x="species", y="petal_length", data=iris_data)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    # pair plot example
    sns.pairplot(iris_data, hue="species", size=2)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.show()


if __name__ == '__main__':
    main()
