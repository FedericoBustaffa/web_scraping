import matplotlib.pyplot as plt


if __name__ == "__main__":
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter([0, 1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10])
    plt.grid()
    plt.show()
