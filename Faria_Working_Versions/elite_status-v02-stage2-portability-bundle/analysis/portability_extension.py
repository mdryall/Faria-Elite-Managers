"""Symbolic and numerical checks for the Stage 2 portability extension."""

from fractions import Fraction
from math import exp, inf
from random import Random


def exact_algebra_checks() -> None:
    """Check the displayed identities exactly over rational test points."""

    rng = Random(20260723)
    for _ in range(10_000):
        z = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        advantage = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        wp = z + advantage
        wk = wp + Fraction(rng.randint(1, 20), rng.randint(1, 10))
        rho_d = z / wp
        rho_a = z * (wk - wp) / (wp * (wk - z))
        rho = rho_a + (rho_d - rho_a) * Fraction(
            rng.randint(1, 99), 100
        )

        assert rho_a / rho_d == (wk - wp) / (wk - z)
        eta_p = (wk - wp) / (rho * wp)
        eta_ep = advantage / (z - rho * wp)
        crossing_gap = (
            (wk - z) * wp * (rho - rho_a)
            / (rho * wp * (z - rho * wp))
        )
        assert eta_ep - eta_p == crossing_gap

        k = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        c = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        r = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        p2phi = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        alpha = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        beta = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        tau = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        c_r = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        phi = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        m_e = Fraction(rng.randint(0, 10), rng.randint(11, 30))
        m_p = Fraction(rng.randint(0, 10), rng.randint(11, 30))

        denominator = c + r + p2phi
        n_portable = (
            k
            - m_e * (tau * r + beta * c + alpha * p2phi)
            - m_p * (r + beta * c + c_r + alpha * p2phi)
        ) / denominator
        output = phi * (n_portable + alpha * (m_e + m_p))
        proposed = (
            phi * k / denominator
            + phi
            / denominator
            * (
                m_e * (alpha * (c + r) - (beta * c + tau * r))
                + m_p * (alpha * (c + r) - (beta * c + r + c_r))
            )
        )
        assert output == proposed


def numerical_continuation() -> None:
    k = 2.0
    r = 1.0
    c = 1.0
    tau = 4.0
    beta = 1.25
    alpha = 1.25
    phi = 6.0
    mu = 4.0
    lambda_e = 2.5
    taste_mean = 0.1
    z = 5.75
    c_r = 9.0 / 4.0
    advantage = (tau - 1.0) * r - c_r
    w_p = z + advantage
    p2phi = 12.0

    rho_a = z * (mu * k - w_p) / (w_p * (mu * k - z))
    rho_d = z / w_p

    def cdf(eta: float) -> float:
        return 1.0 if eta == inf else 1.0 - exp(-eta / taste_mean)

    def allocation(rho: float) -> dict[str, float]:
        eta_e = mu * k / z - 1.0
        if rho <= rho_a:
            eta_p = inf
            eta_ep = eta_e
            m_e = 1.0 - cdf(eta_e)
            m_p = 0.0
        elif rho < rho_d:
            eta_p = (mu * k - w_p) / (rho * w_p)
            eta_ep = advantage / (z - rho * w_p)
            m_e = 1.0 - cdf(eta_ep)
            m_p = cdf(eta_ep) - cdf(eta_p)
        else:
            eta_p = (mu * k - w_p) / (rho * w_p)
            eta_ep = inf
            m_e = 0.0
            m_p = 1.0 - cdf(eta_p)

        n_portable = (
            k
            - m_e * (tau * r + beta * c + alpha * p2phi)
            - m_p * (r + beta * c + c_r + alpha * p2phi)
        ) / (c + r + p2phi)
        sigma = 1.0 - 3.0 * (n_portable + m_e + m_p)
        output = phi * (n_portable + alpha * (m_e + m_p))
        burn = (
            m_e * ((tau - 1.0) * r + (beta - 1.0) * c)
            + m_p * (c_r + (beta - 1.0) * c)
        )
        return {
            "eta_p": eta_p,
            "eta_ep": eta_ep,
            "m_e": m_e,
            "m_p": m_p,
            "n": n_portable,
            "sigma": sigma,
            "output": output,
            "burn": burn,
        }

    minimum_n = inf
    minimum_sigma = inf
    for index in range(20_001):
        rho = index / 20_000
        values = allocation(rho)
        minimum_n = min(minimum_n, values["n"])
        minimum_sigma = min(minimum_sigma, values["sigma"])

    assert minimum_n > 0.0
    assert minimum_sigma > 0.0

    print(f"activation threshold = {rho_a:.12f}")
    print(f"displacement threshold = {rho_d:.12f}")
    print(f"minimum n on [0,1] = {minimum_n:.12f}")
    print(f"minimum sigma on [0,1] = {minimum_sigma:.12f}")
    for label, rho in (("0", 0.0), ("rho_D", rho_d), ("1", 1.0)):
        values = allocation(rho)
        print(
            label,
            *(f"{values[key]:.12f}" for key in (
                "m_e", "m_p", "n", "sigma", "output", "burn"
            )),
        )


if __name__ == "__main__":
    exact_algebra_checks()
    numerical_continuation()
