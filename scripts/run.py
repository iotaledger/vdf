import os

t_values = range(10, 15)
lambda_values = ['1024', '2048', '4096']
kk = [256]
ww = [0]
repeat = 10
repeat_large = 3

for i in range(repeat_large):
    print("I=" + str(i))
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
