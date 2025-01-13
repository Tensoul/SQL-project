import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.stats.diagnostic
import het_white
from statsmodels.tsa.stattools
import adfuller
from scipy.stats import shapiro

# Load data
crypto_data = pd.read_csv('crypto_monthly_data.csv')
macro_data = pd.read_excel('Makro.xlsx')

# Define dependent and independent variables
X = macro_data[['Inflation (%)', 'Interest Rate (%)',
                'M2 (Billion USD)', 'Gold Price']]
y = crypto_data['Zmiana_cen_kryptowalut']

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Print the summary
print(model.summary())

# White's test for heteroskedasticity
white_test = het_white(model.resid, model.model.exog)
print('White’s test p-value:', white_test[1])

# Durbin-Watson test for autocorrelation
dw_stat = sm.stats.durbin_watson(model.resid)
print('Durbin-Watson statistic:', dw_stat)

# Shapiro-Wilk test for normality
shapiro_test = shapiro(model.resid)
print('Shapiro-Wilk test p-value:', shapiro_test.pvalue)

# Augmented Dickey-Fuller test for unit root
adf_test = adfuller(model.resid)
print('ADF test p-value:', adf_test[1])
