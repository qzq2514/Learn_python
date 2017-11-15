class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> print("这是测试内容-----------1")
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    
    >>> print("这是测试内容-----------2")
    >>> d1.y = 200
    >>> d1['y']
    200
    
    >>> print("这是测试内容-----------3")
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> print("这是测试内容-----------4")
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
#进行文档测试，会按照命令行的形式执行文档中的注释部分
#什么输出也没有。这说明我们编写的doctest运行都是正确的
    import doctest
    doctest.testmod()
    
    
