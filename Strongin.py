r_d = 4

def func(x):
    return round((x)**2, r_d)
    #return round(x, r_d)

n_const = 5

n = 0
r = 2

x = list(map(float, input().split()))
gl_min = [x[0], func(x[0])]

while (n < n_const):
    R = list()
    M_list = list()
    for i in range(len(x) - 1):
        M_list.append (round(abs(func(x[i + 1]) - func(x[i])) / (x[i+1] - x[i]), r_d) )
    
    M = max(M_list)
    m = 1 if M == 0 else r * M

    print("M: ", M, " m: ", m)

    for i in range(len(x) - 1):
        R.append (round(m * (x[i + 1] - x[i]) + (func(x[i + 1]) - func(x[i]))**2/(m * (x[i+1] - x[i])) - 2 * (func(x[i + 1]) + func(x[i])), r_d))


    ind = R.index(max(R))
    x_new = round(0.5 * (x[ind + 1] + x[ind]) - (func(x[ind + 1]) - func(x[ind]))/(2*m), r_d)
    x.append(x_new)
    x.sort()
    if gl_min[1] > func(x_new):
        gl_min[0] = x_new
        gl_min[1] = func(x_new)

    print("R: ", R, "\nX: ", x_new, "\nAll X: ", x, "\nGlobal min at: ", gl_min[0], "\n")
    n += 1
