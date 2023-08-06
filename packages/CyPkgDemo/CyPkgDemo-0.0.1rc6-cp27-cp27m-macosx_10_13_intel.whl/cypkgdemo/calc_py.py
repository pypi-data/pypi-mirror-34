from cypkgdemo.calc import c_sa, c_sa_str

def Sa(x):
    if isinstance(x, int):
        return c_sa(x)
    elif isinstance(x, str):
        return c_sa_str(x)
    else:
        return