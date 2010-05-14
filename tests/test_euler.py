from mahotas.euler import euler, _euler_lookup4, _euler_lookup8
import numpy as np

def test_lookup():
    Q1 = [np.array(q, np.bool) for q in [[0,0],[1,0]], [[0,0],[0,1]], [[0,1],[0,0]], [[1,0],[0,0]] ]
    Q2 =  [(~q) for q in Q1]
    Q3 = [np.array(q, np.bool) for q in [[0,1],[1,0]], [[1,0],[0,1]] ]
    
    def _value(q, lookup):
        q = q.ravel()
        value = np.dot(q, (1,2,4,8))
        return lookup[value]

    for q in Q1:
        assert _value(q, _euler_lookup8) == .25
        assert _value(q, _euler_lookup4) == .25
    for q in Q2:
        assert _value(q, _euler_lookup8) == -.25
        assert _value(q, _euler_lookup4) == -.25
    for q in Q3:
        assert _value(q, _euler_lookup8) == -.5
        assert _value(q, _euler_lookup4) ==  .5

def test_euler():
    f = np.zeros((16,16), np.bool)
    f[4:8,4:8] = 1
    assert euler(f) == 1

    f[6:7,5:7] = 0

    assert euler(f) == 0
