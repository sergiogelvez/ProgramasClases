import numpy as np
from numba import njit, prange, set_num_threads
from time import perf_counter_ns

def matrix_product(mat_a, mat_b):
    """Returns the product of the matrices mat_a and mat_b."""
    m = mat_a.shape[0]
    n = mat_b.shape[1]

    assert(mat_a.shape[1] == mat_b.shape[0])

    ncol = mat_a.shape[1]

    mat_c = np.zeros((m, n), dtype=np.float64)

    for row_ind in range(m):
        for col_ind in range(n):
            for k in range(ncol):
                mat_c[row_ind, col_ind] += mat_a[row_ind, k] * mat_b[k, col_ind]

    return mat_c

@njit(parallel=True)
def matrix_product_par(mat_a, mat_b):
    """Returns the product of the matrices mat_a and mat_b."""

    sset_num_threads(8);

    m = mat_a.shape[0]
    n = mat_b.shape[1]

    assert(mat_a.shape[1] == mat_b.shape[0])

    ncol = mat_a.shape[1]

    mat_c = np.zeros((m, n), dtype=np.float64)

    for row_ind in prange(m):
        for col_ind in prange(n):
            for k in prange(ncol):
                mat_c[row_ind, col_ind] += mat_a[row_ind, k] * mat_b[k, col_ind]

    return mat_c

a = np.random.randn(10, 10)
b = np.random.randn(10, 10)

c_actual_par = matrix_product(a, b)
#segunda corrida
t_ini = perf_counter_ns()
c_actual_par = matrix_product(a, b)
t_fin = perf_counter_ns()
t_par = t_fin - t_ini

t_ini = perf_counter_ns()
c_actual = matrix_product(a, b)
t_fin = perf_counter_ns()
t_norm = t_fin - t_ini

t_ini = perf_counter_ns()
c_expected = a @ b
t_fin = perf_counter_ns()
t_np = t_fin - t_ini

error = np.linalg.norm(c_actual - c_expected) / np.linalg.norm(c_expected)
error_par = np.linalg.norm(c_actual_par - c_expected) / np.linalg.norm(c_expected)

print(f"The error is {error}, the parallel error is {error_par}.")
print(f"The times are: parallel = {t_par} -- manual = {t_norm} -- numpy = {t_np}")