from multiprocessing import Pool

print("hogex12")

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(1) as p:
        print(p.map(f, [1, 2, 3]))
