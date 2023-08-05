from biokit.viz import imshow, Imshow



def test_viz_imshow():
    from pandas import DataFrame
    df = DataFrame({'a':[1,2], 'b':[3,4]})
    imshow(df)

def test_viz_imshow_class():
    from pandas import DataFrame
    df = DataFrame({'a':[1,2], 'b':[3,4]})
    im = Imshow(df)
    im.plot(xticks_on=False, yticks_on=False)
