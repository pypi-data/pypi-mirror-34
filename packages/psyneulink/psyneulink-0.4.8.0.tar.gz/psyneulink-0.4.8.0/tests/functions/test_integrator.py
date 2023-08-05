
import psyneulink.components.functions.function as Function
import psyneulink.globals.keywords as kw
import numpy as np
import pytest

SIZE=4
test_var = np.random.rand(SIZE)
test_initializer = np.random.rand(SIZE)
test_noise_arr = np.random.rand(SIZE)

RAND0_1 = np.random.random()
RAND2 = np.random.rand()
RAND3 = np.random.rand()

def AdaptiveIntFun(init, value, iterations, rate, noise, offset, **kwargs):
    val = np.full_like(value, init)
    for i in range(iterations):
        val = (1 - rate) * val + rate * value + noise + offset
    return val

test_data = [
    (Function.AdaptiveIntegrator, test_var, {'rate':RAND0_1, 'noise':RAND2, 'offset':RAND3}, None, AdaptiveIntFun),
    (Function.AdaptiveIntegrator, test_var, {'rate':RAND0_1, 'noise':test_noise_arr, 'offset':RAND3}, None, AdaptiveIntFun),
    (Function.AdaptiveIntegrator, test_var, {'initializer':test_initializer, 'rate':RAND0_1, 'noise':RAND2, 'offset':RAND3}, None, AdaptiveIntFun),
    (Function.AdaptiveIntegrator, test_var, {'initializer':test_initializer, 'rate':RAND0_1, 'noise':test_noise_arr, 'offset':RAND3}, None, AdaptiveIntFun),
]

# use list, naming function produces ugly names
names = [
    "AdaptiveIntegrator",
    "AdaptiveIntegrator Noise Array",
    "AdaptiveIntegrator Initializer",
    "AdaptiveIntegrator Initializer Noise Array",
]

GROUP_PREFIX="Integrator "

@pytest.mark.function
@pytest.mark.integrator_function
@pytest.mark.parametrize("func, variable, params, fail, expected", test_data, ids=names)
@pytest.mark.benchmark
def test_basic(func, variable, params, fail, expected, benchmark):
    if fail is not None:
        # This is a rather ugly hack to stop pytest benchmark complains
        benchmark.disabled = True
        benchmark(lambda _:0,0)
        pytest.xfail(fail)
        return
    f = func(default_variable=variable, **params)
    benchmark.group = GROUP_PREFIX + func.componentName;
    f.function(variable)
    f.function(variable)
    res = benchmark(f.function, variable)
    # This is rather hacky. it might break with pytest benchmark update
    iterations = 3 if benchmark.disabled else benchmark.stats.stats.rounds + 2
    assert np.allclose(res, expected(f.initializer, variable, iterations, **params))
