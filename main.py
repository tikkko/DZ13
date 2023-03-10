s1 = [1, 2, 3, 4, 5, 'six']
s2 = [4, 5, 6, "six", 7, 8]


def intersection():
    s3 = []
    for i in s1:
        for j in s2:
            if i == j:
                s3.append(i)

    print(s3)


if __name__ == '__main__':
    intersection()
