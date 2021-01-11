
def test(Input):
    try:
        assert (Input*2).split("|")[2] == "Awesome"
    except:
        assert False
