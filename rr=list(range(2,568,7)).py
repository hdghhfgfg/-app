rr=list(range(2,568,7))
print(rr)
tt=[yy**2 for yy in range(3,6777,8)]
print(tt)
def name_car(color,named,kind=''):
    if kind:
        full_dd=f"{color} {named} {kind}"
    else:
        full_dd=f"{color} {named}"
    return full_dd.title()
oo=name_car('gree','bwm','ttttt')
print(oo)
oo=name_car('yellow','uuuuuu')
print(oo)

