
import sys
sys.path.append('..')

from hirsch import hirsch

DISCRETE_TESTS = [
	([1], 1.0),
	([2,1], 1.0),
	([1,2], 1.0),
	([2,2], 2.0),
	([2,2,1], 2.0),
	([2,2,3], 2.0),
	([3,3,3,1], 3.0),
	([147,69,59,14,13,10,6,5,2,2,1,1,1,0,0], 6.0), # Louie citations
]

CONTINUOUS_TESTS = [
	([1.0]*10, 1.0), # maximally populated
	([0.0]*10, 0.0), # minimally populated
	([i/10 for i in range(11)], 0.5), # linearly populated
	([1.0,1.0,0.5], 0.75),
]

POPULATION_TESTS = [
	([1,2,3], [1,2,6], 0.75),
]

def test_discrete():
	for samples, h_correct in DISCRETE_TESTS:
		h = hirsch(samples)
		assert h == h_correct, f"{samples=} {h_correct=} {h=}"

def test_continuous():
	for samples, h_correct in CONTINUOUS_TESTS:
		h = hirsch(samples, continuous=True)
		assert h == h_correct, f"{samples=} {h_correct=} {h=}"

def test_populations():
	for samples, populations, h_correct in POPULATION_TESTS:
		h = hirsch(samples, populations)
		assert h == h_correct, f"{samples=} {populations=} {h_correct=} {h=}"
