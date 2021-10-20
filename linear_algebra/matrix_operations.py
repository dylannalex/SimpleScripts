def dim(matrix):
    """
    Returns matrix dimension
    """
    if not type(matrix) == list:
        return []
    return [len(matrix)] + dim(matrix[0])


def sum_matrices(m1, m2):
    """
    Returns m1 + m2
    """
    if dim(m1) != dim(m2):
        raise ValueError("Matrices must have the same dimension")

    return [
        [m1[row][col] + m2[row][col] for col in range(len(m1[0]))]
        for row in range(len(m1))
    ]


def matrix_multiplication(m1, m2):
    """
    Returns m1.m2
    """
    m1_dim = dim(m1)
    m2_dim = dim(m2)

    if m1_dim[1] != m2_dim[0]:
        raise ValueError("Matrices cannot be multiplied")

    result_dim = [m1_dim[0], m2_dim[1]]
    result = [[0 for _ in range(result_dim[0])] for _ in range(result_dim[1])]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    return result


def main():
    m1 = [[1, 2], [5, 3], [1, 6]]
    m2 = [[8, 3, 9], [-6, 1, 7]]

    print(f"Matrix dimension:           dim(m1) = {dim(m1)}")
    print(f"                            dim(m2) = {dim(m2)}\n\n")
    print(f"Matrix multiplication:      m1 x m2 = {matrix_multiplication(m1, m2)}")


if __name__ == "__main__":
    main()
