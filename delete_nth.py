from random import randint

def delete_nth(n, num_list):
    num_map = dict()
    out_list = []

    for num in num_list:
        try:
            num_map[num] += 1
        except KeyError:
            num_map[num] = 1

        if num_map.get(num) <= n:
            out_list.append(num)

    return out_list


if __name__ == '__main__':
    while True:
        try:
           n = int(input('Insert the maximum occurrences: '))
        except:
           print('Invalid input. Try again.')
        else:
            break

    in_list = []
    for _ in range(50):
        in_list.append(randint(1, 5))

    out_list = delete_nth(n, in_list)

    print('Original list:')
    print(in_list)
    print()
    print('Out list:')
    print(out_list)
