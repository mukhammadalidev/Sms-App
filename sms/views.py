
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from sms.models import Sms
from sms.serializers import SmsSerializer

from eskiz.client.sync import ClientSync

eskiz_client = ClientSync(
    
    email="mukhammadalidev@gmail.com",
    password="1bBvGmUTuM7p9ecmafVjca1CU2IsRtXXIMDihjW2",
)

text = "Bu Eskiz dan test"




class SendPhoneNumber(APIView):
    def post(self,request):

        serializer = SmsSerializer(data=request.data)
        
        if serializer.is_valid():
            resp = eskiz_client.send_sms(
            phone_number=serializer.data['phone_number'],
            message=text

                        )
            
            print(resp)
            print(serializer.data['phone_number'])
            return Response(
                data={
                    "success"
                }
            )
        else:
            return Response("error")
        


    
