def sum_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")

    return [v1[i] + v2[i] for i in range(len(v1))]
