def to_literal(s):
    if "'" not in s:
        return "'%s'" % s
    if '"' not in s:
        return '"%s"' % s
    return "concat('%s')" % s.replace("'", "',\"'\",'")