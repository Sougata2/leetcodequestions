def pascal_triangle(n):
    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    for i in range(n-2):
        layer = triangle[-1]
        layer_size = len(layer)
        new_layer = [1]
        for j in range(1, layer_size):
            new_layer.append(layer[j] + layer[j - 1])
            if j == layer_size-1:
                new_layer.append(layer[j])
        triangle.append(new_layer)
    return triangle


print(pascal_triangle(3))
print(pascal_triangle(2))
print(pascal_triangle(1))
