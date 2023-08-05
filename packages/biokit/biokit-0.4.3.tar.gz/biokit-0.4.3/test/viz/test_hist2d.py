


def test1():
    from numpy import random
    from biokit.viz import hist2d
    X = random.randn(10001)
    Y = random.randn(10001)
    h = hist2d.Hist2D(X,Y)
    h.plot(bins=100, contour=True, norm='log', normed=True)
    h.plot(bins=[100,100], contour=True, norm='log', normed=True)

