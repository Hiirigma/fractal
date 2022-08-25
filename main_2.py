import sys


def permutate(names: list, k: int, out: list):
    if k == 1:
        out.append(names.copy())
        return

    for i in range(k):
        permutate(names, k - 1, out)
        if k % 2 == 0:
            names[i], names[k - 1] = names[k - 1], names[i]
        else:
            names[0], names[k - 1] = names[k - 1], names[0]


def main():
    inp = sys.stdin.readline()
    # inp = "Kireev         Fedorova        Popov     \n"
    inp = inp[:-1]

    names = inp.split(" ")
    names = [name for name in names if len(name) != 0]

    names = sorted(names)

    if len(names) == 0:
        print(-1)
        return

    k_part = ""
    i = 0
    while i < len(names):
        if len(names[i]) != 0 and names[i].lower()[0] == 'k':
            k_part = names[i]
            if i != 0:
                names[0], names[i] = names[i], names[0]

            break
        i += 1

    if len(k_part) == 0:
        print(-1)
        return

    if len(names) == 1:
        print("".join(names))
        return

    out = list()
    permutate(names[1:], len(names[1:]), out)
    print("\n".join(sorted("{0} {1}".format(k_part, " ".join(k[1])) for k in enumerate(out))))


if __name__ == "__main__":
    main()
