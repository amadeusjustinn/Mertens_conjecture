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

    maxmertens = minmertens = 1
    maxindex = minindex = []
    for p in range(1, n):
        # Assign Mertens function values for p
        ymertens[p] = mertens.mobius(p + 1) + ymertens[p - 1]
        # Set max and min values
        if ymertens[p] >= maxmertens:
            if ymertens[p] > maxmertens:
                maxmertens = ymertens[p]
                maxindex = []
            maxindex.append(str(p + 1))
        if ymertens[p] <= minmertens:
            if ymertens[p] < minmertens:
                minmertens = ymertens[p]
                minindex = []
            minindex.append(str(p + 1))
    max_string = "Max: " + str(maxmertens) + " at x = " + ", ".join(maxindex)
    min_string = "Min: " + str(minmertens) + " at x = " + ", ".join(minindex)
    final_string = max_string + "\n" + min_string

    plt.title("Disproven Mertens conjecture\nMertens function and square roots for positive integers <= " + str(n), fontsize=10)
    plt.xlabel("x")
    plt.ylabel("Mertens(x) and sqrt(x)")

    plt.plot(xarr, ymertens, "#FF2F00", label="Mertens(x)")

    # Smoothen square root graph using scipy
    xarr3 = np.linspace(0, n, n * 50)
    bsp1 = ipl.make_interp_spline(xarr2, ysqrtpos)
    ysqrtpos2 = bsp1(xarr3)
    plt.plot(xarr3, ysqrtpos2, "#0066FF", label="sqrt(x)")

    bsp2 = ipl.make_interp_spline(xarr2, ysqrtneg)
    ysqrtneg2 = bsp2(xarr3)
    plt.plot(xarr3, ysqrtneg2, "#0066FF")

    # Place grid, legend and text on graph
    plt.grid(b=True)
    plt.legend(bbox_to_anchor=(0, 1), loc='upper left')

    plt.figtext(0.5, 0.03, final_string, fontsize=9, ha="center",
                bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5})
    plt.subplots_adjust(bottom=0.19, top=0.9)

    plt.show()


if __name__ == "__main__":
    main()
