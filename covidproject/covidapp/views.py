from django.shortcuts import render
import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "dbcbb5f94dmshaf7c0ff5765f2ffp158b3cjsnf38adbf900c5",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)



def helloworld(request):
    
    number_of_results = int(response['results'])
    country_list = []
    for x in range(0,number_of_results):
        country_list.append((response['response'][x]['country']))
    
    if request.method =="POST":
        selectedcountry = request.POST['selectedcountry']
        # print(selectedcountry)
        for x in range (0,number_of_results):
            if selectedcountry == (response['response'][x]['country']):
                new= response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)
        context = {'country_list':country_list ,'selectedcountry':selectedcountry,'new':new ,'active':active ,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'helloworld.html',context)
    context = {'country_list':country_list}
    return render(request,'helloworld.html',context)