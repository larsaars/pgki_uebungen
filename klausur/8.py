import numpy as np


def riemann(f, a: float, b: float, n: int = 1000) -> float:
    # the x values
    x = np.linspace(a, b, n + 1)
    # width of a single rectangle
    w = abs(a - b) / n
    # calc the summarized height; f(x) is the height
    hs = f(x).sum()
    # subtract the triangle areas (overheads of the rectangles)
    hs -= (f(a) + f(b)) / 2
    # approached area under f is heights * width of each rectangle
    return hs * w


def riemann_prof(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    return ((b - a) / n) * (f(x).sum() - (f(a) + f(b)) / 2)


if __name__ == '__main__':
    a, b, n = -10, 100, 1000
    func = lambda x: x * x
    print(riemann(func, a, b, n))
    print(riemann_prof(func, a, b, n))
