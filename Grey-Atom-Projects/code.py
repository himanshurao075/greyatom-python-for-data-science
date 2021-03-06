# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')
#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
print(property_and_loan['N'][1])
print(property_and_loan['Y'][0])
#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
print(education_and_loan['N'][1])
print(education_and_loan['Y'][0])



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')
#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1, ax_2, ax_3)=plt.subplots(1,3)

#Plotting scatter plot

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')
#Setting the subplot axis title
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')

#Plotting scatter plot
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
print(data['TotalIncome'].head())
#Setting the subplot axis title

ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')
#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



