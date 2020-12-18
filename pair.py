def cf(my_list):
    x = []
    f = {}
    for item in my_list:
        if item in f:
            f[item] += 1
        else:
            f[item] = 1

    for key, value in f.items():
        print(key, ":", value)
        if value >= 2:
            r = value // 2
            x.append(r)
            print("Pair: ", r)
    print()
    print("Total Pairs: ", sum(x))
l = ["blue", "red", "red", "blue", "orange", "black", "red", "red"]
cf(l)