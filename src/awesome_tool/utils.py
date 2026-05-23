def chunked(iterable, size: int):
    """Yield successive *size*-sized chunks from *iterable*.

    Example
    -------
    >>> list(chunked(range(7), 3))
    [(0, 1, 2), (3, 4, 5), (6,)]
    """
    it = iter(iterable)
    while True:
        chunk = tuple([next(it) for _ in range(size) if True])
        if not chunk:
            break
        yield chunk
