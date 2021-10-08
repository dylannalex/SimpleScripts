def sum_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")

    return [v1[i] + v2[i] for i in range(len(v1))]


def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension")

    return sum([v1[i] * v2[i] for i in range(len(v1))])


def scale(v: list, k: float):
    return [k * i for i in v]


def subtract_vectors(v1, v2):
    """returns v1 - v2"""
    return sum_vectors(v1, scale(v2, -1))


def main():
    v1 = [1, 2, 3]
    v2 = [6, 7, 8]
    k = 2
    print(f"Sum vectors:        v1 + v2 = {sum_vectors(v1, v2)}\n\n")
    print(f"Dot product:        v1.v2 = {dot_product(v1, v2)}\n\n")
    print(f"Scale vector:       k.v1 = {scale(v1, k)}")
    print(f"                    k.v2 = {scale(v2, k)}\n\n")
    print(f"Subtract vectors:   v1 - v2 = {subtract_vectors(v1,v2)}")
    print(f"                    v2 - v1 = {subtract_vectors(v2,v1)}")


if __name__ == "__main__":
    main()
