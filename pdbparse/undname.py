import idc


def undname(name):
    if name.startswith("?"):
        name = _demangle(name)
    elif name.startswith("_") or name.startswith("@"):
        name = name.rsplit('@',1)[0][1:]
    return name


def _demangle(name, short=True):
    dtype = idc.INF_LONG_DN
    if short:
        dtype = idc.INF_SHORT_DN
    tmp = idc.Demangle(name, idc.GetLongPrm(dtype))
    if tmp:
        name = tmp
    name = name.replace('__', '::')
    return name
