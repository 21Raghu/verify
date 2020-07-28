from rest_framework.views import APIView
from django.http import JsonResponse
import requests

class DataView(APIView):
    def get(self, request):
        id = int(request.GET.get('id'))
        first_name = request.GET.get('first_name')
        response_data = {}
        res = getJsonResponse()
        if res:
            for user in res:
                print(type(user['id']),type(id),user['first_name']),type(first_name)
                if user['id'] == id and user['first_name'] == first_name:
                    response_data["id_assigned_to_name"] = True

            if len(res) == 12:
                response_data['Lenght_is_12'] = True
            else:
                response_data['Lenght_is_12'] = False
            return JsonResponse(response_data)
        else:
            return JsonResponse(response_data)


class Verifycomp(APIView):
    def get(self, request):
        id = int(request.GET.get('id'))
        company_name = request.GET.get('Company_name')
        response_data = {}
        response_data = getId(id,company_name)
        return JsonResponse(response_data)
i = 1
listData = []
def getJsonResponse():
    global i,listData
    url='https://reqres.in/api/users?page='+str(i)
    response = requests.get(url).json()
    if len(response['data']):
        for data in response['data']:
            listData.append(data)
        i = i+1
    else:
        return listData
    getJsonResponse()


j = 1
iDdata=[]
def getId(id,company):
    global j,iDdata
    url="https://reqres.in/api/users/" + str(j)
    response = requests.get(url).json()
    response_data={}
    data_ad = response['ad']
    data = response['data']
    if id == data['id'] and company == data_ad['company']:
        print(id,data['company'])
        response_data['Id_found_in_company'] = True
        return response_data
    else:
        return response_data















