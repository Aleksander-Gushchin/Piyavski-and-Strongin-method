r_d = 4

def func(x):
    #return round((x - 1)**2, 2)
    return round(x, r_d)

m = 2
n_const = 5

n = 0

x = list(map(float, input().split()))
gl_min = [x[0], func(x[0])]

while (n < n_const):
    R = list()
    for i in range(len(x) - 1):
        R.append (round(0.5 * m * (x[i + 1] - x[i]) - (func(x[i + 1]) + func(x[i]))/2, r_d))


    ind = R.index(max(R))
    x_new = round(0.5 * (x[ind + 1] + x[ind]) - (func(x[ind + 1]) - func(x[ind]))/(2*m), r_d)
    x.append(x_new)
    x.sort()
    if gl_min[1] > func(x_new):
        gl_min[0] = x_new
        gl_min[1] = func(x_new)

    print("R: ", R, "\nX: ", x_new, "\nAll X: ", x, "\nGlobal min at: ", gl_min[0], "\n")
    n += 1
