def e_approx(n):
    result = 1
    factorial = 1
    for i in range(1, n+1):
        result += 1/factorial
        factorial *= (i + 1)
    return result

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
main()