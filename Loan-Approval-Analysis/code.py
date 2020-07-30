# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
# Step 1
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = "object")
numerical_var = bank.select_dtypes(include = "number")



# Step 2
banks = bank.drop(columns=['Loan_ID'])
bank_mode = banks.mode()
banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())


# Step 3
avg_loan_amount = pd.pivot_table(banks, index = ["Gender", "Married", "Self_Employed"], values = "LoanAmount", aggfunc = np.mean)
print(avg_loan_amount)


# Step 4
loan_approved_se = banks[(banks["Self_Employed"] == "Yes") & (banks["Loan_Status"] == "Y")]
loan_approved_nse = banks[(banks["Self_Employed"] == "No") & (banks["Loan_Status"] == "Y")]
percentage_se = (len(loan_approved_se) * 100) / 614
percentage_nse = (len(loan_approved_nse) * 100) / 614
print(percentage_se)
print(percentage_nse)


# Step 5
loan_term = banks["Loan_Amount_Term"].apply(lambda x: int(x)/12)
big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)


# Step 6
loan_groupby = banks.groupby(["Loan_Status"])["ApplicantIncome", "Credit_History"]
mean_values = loan_groupby.mean()
print(mean_values)





