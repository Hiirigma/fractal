import math


def helpPlumk(n: int, weight: int) -> list:
    giri = []
    outWeight = []

    for g in range(n + 1):
        giri.append(int(math.pow(3, n - g)))

    tmpWeigt = 0
    for g in giri:
        tmpWeigt += g
        outWeight.append(g)

        if tmpWeigt == weight:
            return outWeight

        if tmpWeigt > weight:
            outWeight.pop()
            tmpWeigt -= g

        if (tmpWeigt + g) == weight:
            outWeight.append(g)
            return outWeight

        if (tmpWeigt + g) < weight:
            tmpWeigt += g
            outWeight.append(g)

    return None


def main():
    n = int(input())
    weight = int(input())

    out = helpPlumk(n, weight * 1000)
    if out is None:
        print(-1)
    else:
        print(" ".join("{}".format(k[1]) for k in enumerate(out)))


if __name__ == "__main__":
    main()
