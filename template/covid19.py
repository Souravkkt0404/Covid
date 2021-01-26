from covid import Covid
import matplotlib.pyplot as plt

covid = Covid()
name=input("Enter Your Country Name : ")

virusdata = covid.get_status_by_country_name(name)

remove = ['id' , 'country', 'latitude' , 'longitude' , 'last_update']
for i in remove :
    virusdata.pop(i)
all = virusdata.pop('confirmed')
id = list(virusdata.keys())
value = [str(i) for i in virusdata.values()]
plt.pie(value , labels=id , colors = ['r','g','b','y','b'],autopct = '%1.1f%%')
plt.title("Country : " +name+"\n Total cases :  "+str(all))
plt.legend()
plt.show()