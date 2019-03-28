def print_triangle(n):
    if n == 1:
        return "*\n"
    else:
        return print_triangle(n-1)+ "*"*n+"\n"


def print_oposite_triangles(n):
    if n == 1:
        return "*\n"
    else:
        return "*"*n+"\n"+print_oposite_triangles(n - 1)+"*" * n + "\n"


def print_ruler(n):
    if n == 1:
        return '-\n'
    else:
        return print_ruler(n - 1) + '-' * n+"\n" + print_ruler(n-1)