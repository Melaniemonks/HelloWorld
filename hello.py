
#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#%%
#read the CSV to a variable called Df
df = pd.read_csv(r'C:/Users/12085/OneDrive/Documents/HelloWorld/covidData/Global_COVID_Vaccination_Tracker.csv', encoding="ISO-8859-1")

#isolated results based on what i am needing for my computation
df = (df[['Countries and regions', 'Percentage of population with 1+ dose', 'Doses administered', 'Percentage of population fully vaccinated']])
#print(df)

#Used this to see the columns avaialble in the table
columns = df.columns
print(f'The following table contains data related to covid 19. The data consists of the following columns ')


question = int(input(" To view complete table press 1, To filter data press 2, For general info press 3 to exit press 0: "))

print()
count=0
if question == 1:
    print(df)

elif question == 2:
    print("Filter data based on the following. Press the following numbers to select") 

    print()

    option = ''

    while option != 0:

        print('1. Countries and regions')
        print('2. Percentage of population with +1 dose')
        print('3. Doses administered')
        print('4. Percentage of population fully vaccinated')

        option = int (input('Show top data based on one of the below. Please insert number: '))

#filter information bases on countries
        if option == 1:
            dp = df.rename(columns={"Countries and regions": "countries"})
            name = (input('Type name of country: ')).capitalize()
            country = dp.query(f"countries == '{name}'")
            print (country)

#top countries with the highest percentage of population with 1+ doses
        elif option == 2:
            amount = int (input ('number of rows: '))
            onepluse = df.sort_values(by=['Percentage of population with 1+ dose'], ascending=False)
            onepluse = onepluse.head(amount)
            onepluse.plot(kind='bar',x='Countries and regions',y='Percentage of population with 1+ dose')

            #view chart
            chart = input(' View chart? Y/N: ').upper()
            if chart == 'Y':
                plt.show()

            elif chart == 'N':
                print(onepluse)
            else:
                print('No more result')
        

# Top countries with doses administered
        elif option == 3:
            amount = int (input ('number of rows: '))
            administered = df.sort_values(by=['Doses administered'], ascending=False)
            administered = administered.head(amount)
            administered.plot(kind='bar',x='Countries and regions',y='Doses administered')

            #View chart
            chart = input(' View chart? Y/N: ').upper()
            if chart == 'Y':
                plt.show()
            elif chart == 'N':
                print(administered)
            else:
                print('No more result')


#Top countries with the highest percentage population of fully vaccinated individuals
        elif option == 4:
            amount = int (input ('number of rows: '))
            fully = df.sort_values(by=['Percentage of population fully vaccinated'], ascending=False)
            fully = fully.head(amount)
            fully.plot(kind='bar',x='Countries and regions',y='Percentage of population fully vaccinated')

            #view chart
            chart = input(' View chart? Y/N: ').upper()
            if chart == 'Y':
                plt.show()
            elif chart == 'N':
                print(fully)
            else:
                print('No more result')
        else: 
            print('Unknown input')

# Total number of vaccines administered
elif question == 3:
    total_doses = df['Doses administered'].sum()
    print (f'Total Doses of vaccines administered: {total_doses}')






#Top 
# %%
