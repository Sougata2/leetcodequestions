# Brute force : Checking every possible solution
# time Complexity : O(n2)
# time Complexity : O(n)

def gas_station(gas, cost):
    # collect all the possible start position.
    start_pos_list = []
    for i in range(len(gas)):
        if cost[i] < gas[i]:
            start_pos_list.append(i)

    for start_pos in start_pos_list:
        possible = True
        end_pos = start_pos + len(gas)
        tank = 0
        for i in range(start_pos, end_pos):
            if i > len(gas)-1:
                real_ind = i % len(gas)
                tank += gas[real_ind]
                tank -= cost[real_ind]
            else:
                tank += gas[i]
                tank -= cost[i]

            if tank <= 0 and i < end_pos - 1:
                possible = False
                break

        if possible:
            return start_pos

    return -1

# Greedy solution
# intuation : first check if the sum of gas is greater than
# the sum of cost because a solution if only possible if the
# gas is equal or more than the cost.
# traverse over the difference of the gas and cost
# whenever the total sum goes zero or negetive set the total sum to zero
# because there might be possiblity that starting position is not the answer
# if you get a position and from the position to end you don't get a negetive value
# then it can be assured that a loop can be covered from that position.


def gas_station_greedy(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start_pos = 0
    total_sum = 0
    for i in range(len(gas)):
        total_sum += (gas[i] - cost[i])
        if total_sum < 0:
            total_sum = 0
            start_pos = i + 1

    return start_pos


if __name__ == "__main__":
    # test case 1
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    # test case 2
    gas = [2, 3, 4]
    cost = [3, 4, 3]

    # test case 3
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]

    # test case 4
    gas = [5, 8, 2, 8]
    cost = [6, 5, 6, 6]

    print(gas_station(gas, cost))
    print(gas_station_greedy(gas, cost))
