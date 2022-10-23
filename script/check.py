import os


def test_pr(name):
    assert name != None
    filename = "../" + name + ".txt"
    isFile = os.path.isfile(filename)
    assert isFile
    with open(filename) as file:
        content = file.read()
        assert name in content
