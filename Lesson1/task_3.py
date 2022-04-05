
sk = ["", "а", "ов"]
idx=0
for list_n in range(1,101):
    if 1 < list_n <= 4:
        idx = 1
    if 4 < list_n:
        idx = 2
    print(str(list_n)+" процент"+str(sk[idx]))
