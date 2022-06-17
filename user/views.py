# views.py
from email import message
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import login, authenticate,logout

class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
       
        user = authenticate(request, username=username, password=password)
        # user = authenticate(request,**requst.data) < 위에 세줄 한줄 입력 시 
        if not user: # 인증 실패 시 
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        # if 문 return 으로 끗난 경우 else 안써도 됨. 
        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    #로그아웃 
    def delete(self, request):
        logout(request)
        return Response({"message":"logout success!"})