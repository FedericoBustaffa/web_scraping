import numpy as np

if __name__ == "__main__":
    print("--- Array ---")
    v = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    for row in v:
        print(row)

        # attributes
    print("--- Attributes ---")
    print(f"Shape: {v.shape}")
    print(f"Dimensions: {v.ndim}")
    print(f"Size: {v.size}")

    # filling
    print("--- Filling 3 x 3 x 3 tensor with 10s ---")
    v = np.full((3, 3, 3), 10)
    print(v)

    print("--- Filling 3 x 3 tensor with 0s ---")
    v = np.zeros((3, 3))
    print(v)

    # arange
    print("--- Arange ---")
    v = np.arange(20, 50, 5)
    print(v)

    # NaN and Inf
    print(f"--- NaN and Inf ---\nNaN: {np.nan}\nInf: {np.inf}")

    # operazioni matematiche
    print("--- Operazioni algebriche ---")
    v1 = np.arange(0, 10, 2)
    v2 = np.arange(1, 6)
    print(f"V1: {v1}\nV2: {v2}")

    print("--- Operazioni con uno scalare ---")
    print(f"Somma: {v1 + 3}")
    print(f"Differenza: {v1 - 1}")
    print(f"Prodotto: {v1 * 3}")
    print(f"Divisione: {v1 / 2}")

    print("--- Operazioni tra vettori ---")
    print(f"Somma: {v1 + v2}")
    print(f"Differenza: {v1 - v2}")
    print(f"Prodotto: {v1 * v2}")
    print(f"Quoziente: {v1 / v2}")

    print("--- Prodotto tra matrici ---")
    m1 = np.array([[1, 2, 3],
                   [3, 5, 1],
                   [9, 2, 6]])

    m2 = np.array([[2, 4, 6],
                   [6, 3, 1],
                   [9, 1, 3]])

    print(f"{m1 * m2}")

    print(np.delete(m1, 2, 1))
