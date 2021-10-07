10 countries where vaccines are administered
administered = df.sort_values(by=['Doses administered'], ascending=False)
administered = administered.head(10)
#print(administered)
administered.plot(kind='bar',x='Countries and regions',y='Doses administered')
#plt.show()


#Top 10 countries with highest percent of fully vaccinated individuals
fully = df.sort_values(by=['Percentage of population fully vaccinated'], ascending=False)
fully = fully.head(10)
fully.plot(kind='bar',x='Countries and regions',y='Percentage of population fully vaccinated')


#What are the Top 10 countries with at least 1+ doses administered
onepluse = df.sort_values(by=['Percentage of population with 1+ dose'], ascending=False)
onepluse = onepluse.head(10)
onepluse.plot(kind='bar',x='Countries and regions',y='Percentage of population with 1+ dose')
#plt.show()
#print(onepluse)

#%%

#print (data)
# %%
