from main import QueryProdRev

def test():
    ProductRevenue = QueryProdRev()
    assert ProductRevenue <= 43233.17
    assert ProductRevenue >= 43233.169

if __name__ == '__main__':
    test()
