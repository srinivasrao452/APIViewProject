
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .models import Emp
from .serializers import EmpSerializer

class EmpListView(APIView):
    def get(self,request):
        emps = Emp.objects.all()
        serializer = EmpSerializer(emps,many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self,request):

        serializer = EmpSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )












class EmpDetailView(APIView):
    def get(self,request,id):
        try:
            emp = Emp.objects.get(eno=id)
        except:
            return Response('Record not available',
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmpSerializer(emp)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def get_object_by_id(self,id):
        try:
            emp = Emp.objects.get(eno=id)
        except:
            emp = None
        return emp


    def put(self,request,id):
        emp = self.get_object_by_id(id)
        if emp is None:
            return Response('Record not avaliable to update',
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmpSerializer(emp,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        emp = self.get_object_by_id(id)
        if emp is None:
            return Response('Record not avaliable to delete',
                            status=status.HTTP_404_NOT_FOUND)
        else:
            emp.delete()
            return Response('Record deleted successfully',
                            status=status.HTTP_204_NO_CONTENT)









class EmpDetailView(APIView):
    def get(self,request,id):
        try:
            emp = Emp.objects.get(eno=id)
        except Emp.DoesNotExist:
            return Response('Record not found',
                            status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmpSerializer(emp)
            return Response(serializer.data)

    def get_object_by_id(self,id):
        try:
            emp = Emp.objects.get(eno=id)
        except Emp.DoesNotExist:
            emp = None
        return emp

    def put(self,request,id):
        emp = self.get_object_by_id(id)
        if emp is None:
            return Response('record not available for updating')
        else:
            serializer = EmpSerializer(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
       emp = self.get_object_by_id(id)
       if emp is None:
           return Response('record not available for deleting')
       else:
            emp.delete()
            return Response('Record deleted succssfully',
                            status=status.HTTP_204_NO_CONTENT)
















