INF = 10000000


def good_perm(tsp, start=0, end=-1):
    """
    Generating a good first permutation by searching
    every time for the nearest neighbor of the current visited city
    """
    visited = [0 for i in range(len(tsp))]
    good = [start]
    current = start
    visited[start] = 1
    while len(good) - len(tsp) and current != end:
        best_len = INF
        best_neighbor = 0
        for i in range(len(tsp)):
            next_neighbor = tsp[current][i]
            if next_neighbor != 0 and next_neighbor < best_len and not visited[i]:
                best_len = next_neighbor
                best_neighbor = i
        good.append(best_neighbor)
        visited[best_neighbor] = 1
        current = best_neighbor
    return good


def route_length(tsp, cities, output_mode):
    """
    Computing the length of the given cities route
    """
    length = 0
    if output_mode == "w":
        start_index = 0
    else:
        start_index = 1
    for i in range(start_index, len(cities)):
        length += tsp[cities[i]][cities[i - 1]]
    return length


def generate_perms(cities):
    """
    Generating all possible permutations for the given cities schema
    """
    perms = []
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            perm = cities.copy()
            perm[i] = cities[j]
            perm[j] = cities[i]
            perms.append(perm)
    return perms


def find_best_solution(tsp, perms, output_mode):
    """
    Looking for the best route (with smallest length cost)
    from the given routes (perms)
    """
    best_len = route_length(tsp, perms[0], output_mode)
    best_sol = perms[0]
    for perm in perms:
        last_best_len = best_len
        best_len = min(best_len, route_length(tsp, perm, output_mode))
        if last_best_len >= best_len:
            best_sol = perm
    return best_sol, best_len


def solve(file_name, output_mode):
    # begin of reading data
    fin = open(file_name, "r")
    n = int(fin.readline())
    tsp = []
    for i in range(n):
        row = [int(num) for num in fin.readline().split(',')]
        tsp.append(row)
    start = int(fin.readline())
    end = int(fin.readline())
    # end of reading data

    if output_mode == "w":
        cities = good_perm(tsp)
    else:
        cities = good_perm(tsp, start - 1, end)
    current_len = route_length(tsp, cities, output_mode)
    new_perms = generate_perms(cities)

    if new_perms:
        best_perm, best_len = find_best_solution(tsp, new_perms, output_mode)
        while best_len < current_len:
            current_len = best_len
            cities = best_perm
            new_perms = generate_perms(cities)
            best_perm, best_len = find_best_solution(tsp, new_perms, output_mode)

    # begin of writing data
    fout = open("output.txt", output_mode)
    fout.write(str(len(cities)) + '\n')
    for i in range(len(cities)):
        fout.write(str(cities[i] + 1))
        if i < len(cities) - 1:
            fout.write(',')
    fout.write('\n' + str(current_len) + '\n')
    # end of writing data


if __name__ == '__main__':
    file = "easy_01_tsp.txt"
    solve(file, "w")
    solve(file, "a")
