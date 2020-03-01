#! /usr/bin/env python3
#


def mcmc_test():

    # *****************************************************************************80
    #
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(123456789)

    data = np.random.randn(20)

    plt.hist(data, rwidth=0.95)
    plt.xlabel('<-- X -- >')
    plt.ylabel('<-- # of observations -- >')
    plt.grid(True)
    plt.title('Histogram of random normal data')
    plt.show()
#
#  For this case, we can actually determine the posterior distribution analytically.
#
    x = np.linspace(-1.0, +1.0, 500)
    mu_post, sigma_post = calc_posterior_analytical(data, 0.0, 1.0)
    y = 1.0 / np.sqrt(2.0 * np.pi * sigma_post**2) * \
        np.exp(- 0.5 * (x - mu_post)**2 / sigma_post**2)
    plt.plot(x, y)
    plt.xlabel('<-- X -- >')
    plt.ylabel('<-- Y -- >')
    plt.grid(True)
    plt.title('Analytical posterior')
    plt.show(block=False)
#
#  Now let's do this by sampling.
#
    mu_current = 1.0
    proposal_width = 1.0

    likelihood_current = normal_likelihood(data, mu_current, 1.0)
    likelihood_proposal = normal_likelihood(data, mu_proposal, 1.0)

    prior_current = normal_pdf(mu_current, mu_prior_mu, mu_prior_sd)
    prior_proposal = normal_pdf(mu_proposal, mu_prior_mu, mu_prior_sd)

    p_current = likelihood_current * prior_current
    p_proposal = likelihood_proposal * prior_proposal

    p_accept = p_proposal / p_current

    accept = np.random.rand() < p_accept

    if (accept):
        cur_pos = proposal

    return


def calc_posterior_analytical(data, mu_0, sigma_0):
    import numpy as np
    sigma = 1.0
    n = len(data)
    mu_post = (mu_0 / sigma_0**2 + data.sum() / sigma**2) / \
        (1.0 / sigma_0**2 + n / sigma**2)
    sigma_post = np.sqrt(1.0 / (1.0 / sigma_0**2 + n / sigma**2))
    return mu_post, sigma_post


def log_normal_likelihood(x_vec, mu, sigma):
    value = 0.0
    for x in xvec:
        value = value + log_normal_pdf(x, mu, sigma)


def log_normal_pdf(x, mu, sigma):
    value = - 0.5 * (x - mu)**2 / sigma**2 - 0.5 * log(2 * pi * sigma**2)
    return value


def normal_likelihood(x_vec, mu, sigma):
    value = 1.0
    for x in x_vec:
        value = value * normal_pdf(x, mu, sigma)


def normal_pdf(x, mu, sigma):
    value = 1 / sqrt(2 * pi * sigma**2) * exp(- 0.5 * (x - mu)**2 / sigma**2)
    return value


if (__name__ == '__main__'):
    mcmc_test()
