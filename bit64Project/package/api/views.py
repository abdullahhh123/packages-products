from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailizers import PackageSerializer , SubscriptionSerializer
from django.http import HttpResponse
from package.models import Package


@api_view(['GET','POST'])
def getRoutes(request):
    routes = [
        'GET /api/packages',
        'GET /api/package/:name',
        'POST /api/package/post',
        'POST /api/make-order',
    ]
    return Response(routes)


@api_view(['GET'])
def get_package_by_name(request,pk):
    try:
         package = Package.objects.filter(product_name=pk)
    except:
        return HttpResponse('''
        <br/>
        <h1>No Packages With The Given Name</h1>''')
    serialzer = PackageSerializer(package,many=True)
    return Response(serialzer.data)


@api_view(['GET'])
def packages(request):
    Videos = Package.objects.all().order_by('product_price')
    serialzer = PackageSerializer(Videos,many=True)
    return Response(serialzer.data)
    
@api_view(['POST'])
def package_post(request):
    serializer = PackageSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def subscription_post(request):
    serializer = SubscriptionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)