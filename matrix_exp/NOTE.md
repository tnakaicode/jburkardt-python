---
title: matrix_exponential
---

compare

- MATLAB's matrix exponential function
- Taylor series approach
  - exp ( A ) = I + A + 1/2 A^2 + 1/3! A^3 + ...
- eigenvalue calculation
  - exp(A) = V *D* inv(V)
  - V is the matrix of eigenvectors of A
  - D is the diagonal matrix

## 1. Taylor

```markdown
    e = np.zeros([n, n])
    f = np.eye(n)
    k = 1
    while (r8mat_is_significant(n, n, e, f)):
        e = e + f
        f = np.dot(a, f)
        f = f / float(k)
        k = k + 1
```

## 2. Eigenvalue

```makrdown
    cevals, cevecs = np.linalg.eig(a)
    evals = cevals.real
    evecs = cevecs.real

    exp_evals = np.exp(evals)
    d2 = np.diag(exp_evals)

    b = np.dot(evecs, d2)
    bt = b.transpose()

    a = evecs
    at = a.transpose()

    et, residuals, rank, s = np.linalg.lstsq(at, bt, rcond=None)
    e = et.transpose()
```
