---
title: Ball
---

## ball_distance

n = 10000
ball_distance_stats
ball_distance_histgram
ball_distance_compare

## ball_monte_carlo

```markdown
    while (n <= 65536):
        x, seed = ball01_sample(n, seed)
        for j in range(0, 7):
            e = e_test[j, :]
            value = monomial_value(3, n, e, x)
            result = ball01_volume() * np.sum(value) / float(n)
        n = 2 * n
```

mononial_value
product ( 1 <= i <= m ) x(i)^e(i)
