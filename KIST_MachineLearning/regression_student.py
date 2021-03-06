import statsmodels.api
import numpy

def main():
    (N, X, Y) = read_data()

    results = do_multivariate_regression(N, X, Y)
    print(results.summary())

    effective_variables = get_effective_variables(results)
    print(effective_variables)

def do_multivariate_regression(N, X, Y):
    # 2
    X = numpy.array(X)

    results = statsmodels.api.OLS(Y,X).fit()
    return results

def get_effective_variables(results):
    eff_vars = []
	# 3
    #print(results.params)
    idx=1
    for x in results.pvalues:
        if x < 0.05:
            eff_vars.append(idx)
        ++idx


    return eff_vars

def read_data():
    # 1
    N = 0
    X = []
    Y = []
    with open("students.txt") as f:
        next(f)
        for line in f:
            splits = line.strip().split(" ")
            numeric_data = [float(x) for x in splits]
            x = numeric_data[0:-1]
            y = numeric_data[-1]
            X.append(x)
            Y.append(y)
            N += 1

    # X must be numpy.array in (30 * 5) shape.
    # Y must be 1-dimensional numpy.array.
    X = numpy.array(X)
    Y = numpy.array(Y)
    return (N, X, Y)

if __name__ == "__main__":
    main()
