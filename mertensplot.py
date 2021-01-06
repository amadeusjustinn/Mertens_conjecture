import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as ipl
import mertens


def main() -> None:
    n = int(
        input("Enter upper bound for Mertens conjecture graph (upper bound included). "))

    xarr = np.array([h for h in range(1, n + 1)])
    xarr2 = np.array([i for i in range(n)])
    # Initialise array for Mertens function valuess
    ymertens = np.array([1 for j in range(n)])
    ysqrtpos = np.array([float(format(k ** 0.5, '.10f'))
                         for k in range(n)])  # Positive square root values
    ysqrtneg = np.array([-m for m in ysqrtpos])  # Negative square root values

    maxmertens = maxindex = minmertens = minindex = 1
    for p in range(1, n):
        # Assign Mertens function values for p
        ymertens[p] = mertens.mobius(p + 1) + ymertens[p - 1]
        # Set max and min values
        if ymertens[p] > maxmertens:
            maxmertens = ymertens[p]
            maxindex = p + 1
        if ymertens[p] < minmertens:
            minmertens = ymertens[p]
            minindex = p + 1
    maxstring = "Maximum: " + str(maxmertens) + " at x = " + str(maxindex)
    minstring = "minimum: " + str(minmertens) + " at x = " + str(minindex)

    plt.title("Disproven Mertens conjecture\nMertens function and square roots for positive integers <= " + str(n), fontsize=10)
    plt.xlabel("x")
    plt.ylabel("Mertens(x) and sqrt(x)")

    plt.plot(xarr, ymertens, "#FF2F00", label="Mertens(x)")

    xarr3 = np.linspace(0, n, n * 50)

    # Smoothen square root graph using scipy
    bsp1 = ipl.make_interp_spline(xarr2, ysqrtpos)
    ysqrtpos2 = bsp1(xarr3)
    plt.plot(xarr3, ysqrtpos2, "#0066FF", label="sqrt(x)")

    bsp2 = ipl.make_interp_spline(xarr2, ysqrtneg)
    ysqrtneg2 = bsp2(xarr3)
    plt.plot(xarr3, ysqrtneg2, "#0066FF")

    plt.grid(b=True)
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left')
    plt.figtext(0.5, 0, maxstring + ", " + minstring, fontsize=9,
                ha="center", bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})
    plt.show()


if __name__ == "__main__":
    main()
