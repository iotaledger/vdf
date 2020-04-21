import os

t_values = range(8, 9)
lambda_values = ['2048']
kk_p = [1, 2, 3, 4, 5, 6, 7, 8]
kk = [2**k for k in kk_p]
ww = [2, 3, 4]
repeat = 2


for t in t_values:
    print(t)
    for lamda in lambda_values:
        print("\t" + lamda)
        for k in kk:
            print("\t\t" + str(k))
            for w in ww:
                print("\t\t\t" + str(w))
                for r in range(repeat):
                    a = os.system('src/bin/vdf ' + str(t) +
                                  ' ' + lamda + ' ' + str(k) + ' ' + str(w))
