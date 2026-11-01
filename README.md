This is a demand forecasting model built using Python that uses the static method to analyze past demand and forecast future demand for a given number of periods.

Overview of the Model:

The model works to calculate future demand by following six distinct steps:

1. The model begins by collecting basic data from the user, including the number of past periods the user wants to analyze, the length of these periods measured by their periodicity, and the number of future periods that the user would like to forecast demand for.
2. The model works to deseasonalize this demand using a series of formulas, 'smoothing' the data provided and removing seasonal factors.
3. The model uses linear regression to draw a trendline for the deseasonalized demand. From this trendline, the model pulls two numbers: the slope, or 'trend' T; and the intercept, or 'level' L.
4. Using these two numbers, the model recalculates a new deseasonalized demand for each period t using a linear equation of the form L + Tt.
5. The model calculates the seasonal factor for each period by dividing the original demand by its deaseasonalized counterpart and then averaging out seasonal factors over similar periods. That is, for p = 4, periods 1, 5, 9, and so on have similar seasonality and will be assigned the same seasonal factor.
6. With all necessary variables defined, the model computes the forecasted demand for the requested amount of periods using the static method formula.

How to Run this Model

1. Create and activate a virtual environment.
2. Run the following commands in the terminal to install the necessary libraries if they are not already installed:
   pip install numpy
   pip install -U scikit-learn
3. Copy and run the code for the model.
