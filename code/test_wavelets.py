from wavelets import pairWise, lowPass


def testpairwise():
    n = [1, 2, 3, 1, 2, 3, 4, 0]
    assert pairWise(n) == [(1,2),(3,1),(2,3),(4,0)]

def testlowPass():
    assert pairWise(n) == [(1,2),(3,1),(2,3),(4,0)]
    assert lowPass(n) == [2.121   2.828   3.536   2.828]
testpairwise()
