def count_ways(row, col):
    
    if row == 1 or col == 1:
        return 1
    return count_ways(row - 1, col) + count_ways(row, col - 1)


if __name__ == '__main__':
    ways = []
    print(count_ways(4, 3))
    
    
    