def fact(n):
    '''
    >>> fact(1)
    1
    >>> fact(3)             #输入fact(3),这里期望输出62,但是其实fact(3)=6,这里会报错
    62

    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()