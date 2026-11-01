import numpy
from sklearn.linear_model import LinearRegression
N = int(input("For how many past periods will demand be provided? "))
p = int(input("Provide the periodicity, or how many times the length of each period occurs in a year: "))
NoF = int(input("For how many future periods do you want to forecast demand? "))
D_a = []
for i in range(N):
    I = float(input("Enter the demand for period " + str(i + 1) + ": "))
    D_a.append(I)
Dbar = []
if p % 2 == 0:
    for t in range(int(p / 2), int(N - (p / 2))):
        Outer_Demand = D_a[int(t - (p/2))] + D_a[int(t + (p/2))]
        Inner_Demand = 0
        for k in range(int(t + 1 - (p/2)), int(t + (p/2))):
            Inner_Demand += 2 * D_a[k]
        Deseasonalized_Demand = (Inner_Demand + Outer_Demand) / (2 * p)
        Dbar.append(Deseasonalized_Demand)
else:
    for t in range(int((p - 1) / 2), int(N - ((p - 1) / 2))):
        Deseasonalized_Demand = 0
        for k in range(int(t - ((p - 1) / 2)), int((t + ((p - 1) / 2) + 1))):
            Deseasonalized_Demand += D_a[k] / p
        Dbar.append(Deseasonalized_Demand)
X = numpy.array(range(int(((N - len(Dbar)) / 2) + 1), int(len(Dbar) + ((N - len(Dbar)) / 2) + 1)))
Y = numpy.array(Dbar)
X = X.reshape(-1,1)
linreg = LinearRegression()
graph = linreg.fit(X,Y)
T = float(linreg.coef_[0])
L = float(linreg.intercept_)
Dbar = []
for n in range(N):
    Deseasonalized_Demand = L + T * (n + 1)
    Dbar.append(Deseasonalized_Demand)
Sbar = []
for K in range(N):
    Seasonal_Factor = D_a[K] / Dbar[K]
    Sbar.append(Seasonal_Factor)
S = []
for l in range(p):
    Seasonal_Factor_Sum = 0
    for j in range(int(N / p)):
        Seasonal_Factor_Sum += Sbar[(j * p) + l]
    Avg_Seasonal_Factor = Seasonal_Factor_Sum / (N / p)
    S.append(Avg_Seasonal_Factor)
F = []
for J in range(NoF):
    Forecasted_Demand = int((L + (((J + 1) + N)* T)) * S[int(((N + J) % p))])
    F.append(Forecasted_Demand)
for f in range(NoF):
    print("Demand for period " + str(N + f + 1) + " is forecasted to be " + str(F[f]) + ".")
