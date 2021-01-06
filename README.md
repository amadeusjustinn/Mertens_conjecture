# Mertens_conjecture
A graph visualisation of the Mertens function to illustrate the concept of the Mertens conjecture. Inspired by a Youtube video by Numberphile entitled "A Prime Surprise (Mertens Conjecture)".

## Möbius Function

The Möbius function *μ*(*n*) takes one parameter − a positive integer *n* − and returns one of three values:
- ***0*** if *n* has a **squared prime factor** (e.g. 18 has a factor of 9, which is 3^2, and 3 is a prime, thus *μ*(9) = 0.),
- ***1*** if *n* has an **even number of prime factors**, **none** of which  **are "repeated"** (e.g. 210 has *four* prime factors − 2, 3, 5 and 7 − and *4* is an even number. None of 2, 3, 5 and 7 are "repeated" factors, i.e. none of 4, 9, 25 and 49 are factors of 210, thus *μ*(210) = 1.) or
- ***-1*** if *n* has an **odd number of prime factors**, **none** of which  **are "repeated"** (e.g. 30 has *three* prime factors − 2, 3 and 5 − and *3* is an odd number. None of 2, 3 and 5 are "repeated" factors, i.e. none of 4, 9 and 25 are factors of 30, thus *μ*(30) = -1.).

**NOTE:** If any prime factor is "repeated", the function would return 0 (e.g. 24 = 2^3 × 3 = **2^2** × 2 × 3, 27 = 3^3 = **3^2** × 3). Also, -1 would be returned for any prime number since any prime number only has one factor (excluding 1), which is the prime number itself, and 1 is an odd number.

## Mertens Function

The Mertens function *M*(*n*) takes one parameter − **a positive integer *n*** − and returns the "rolling sum" of the return values of the Möbius function up to and including *n*. Less formally, *M*(*n*) is the count of square-free integers up to *n* that have an even number of prime factors, minus the count of those that have an odd number.
- For example,  *M*(5) = **-2** because *μ*(1) = 1, *μ*(2) = -1, *μ*(3) = -1, *μ*(4) = 0 and *μ*(5) = -1. 1 + (-1) + (-1) + 0 + (-1) = **-2**.

## The Conjecture

The Mertens conjecture is a disproven mathematical conjecture regarding the Mertens function *M*(*n*). Its truth was known to imply **the truth of the Riemann hypothesis** ([a good explanation by Jørgen Veisdal](https://medium.com/cantors-paradise/the-riemann-hypothesis-explained-fa01c1f75d3f)).

The conjecture states that **the Mertens function *M*(*n*) is bounded by ±√n**, i.e. the graph of *M*(*n*) never "escapes" the right-facing U-shaped graph of the square root function. This statement was disproven in a 1985 paper by Andrew Odlyzko and Herman te Riele ([the full disproof in PDF format](http://www.dtc.umn.edu/~odlyzko/doc/arch/mertens.disproof.pdf)). The exact value of *n* at which this statement becomes false is not known; the first counterexample appears above ***n* = 10^16** and below ***n* = 10^(6.91×j)** (where **j** = **10^39**), which are terribly imprecise upper and lower bounds.

## The Code

To run the code, simply run `python3 mertensplot.py`. The terminal will prompt the user to type the desired upper bound of the Mertens function, which is included. After said bound is entered, a graph will be generated with the use of the Python library `matplotlib`. The graph includes the Mertens function values for each integer from 1 up to and including the aforementioned upper bound, as well as the positive and negative square root values for real numbers from 0 up to and including the aforementioned upper bound.

At some number that is probably too large for personal computers to handle (see imprecise bounds in description of conjecture above), the Mertens function will "break away" from the square root function. The main takeaway is that just because a pattern (or in this case, a mathematical conjecture) has a large amount of computational evidence in its favour, does not mean it is guaranteed to be true for all numbers up to infinity.
