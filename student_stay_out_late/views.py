import json

from django.db.models import Count
from django.forms import renderers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import  api_view, list_route, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from student_stay_out_late.models import Passresults, stuinfo, Care, Explain
from student_stay_out_late.serializers import PassresultsSerializer, StuinfoSerializer
NOPERMISSION = -2
#cookie 验证
def cookie_required(view):
    def decorator(request, *args, **kwargs):
        try:
            if'UserId' in request.COOKIES:
                return view(request, *args, **kwargs)
        except :
            pass
        return auth_fail_handler(request)
    return decorator
#异常处理
def auth_fail_handler(request):
    return HttpResponse(json.dumps({'code': NOPERMISSION}))
#模拟登陆
def pertendlogin(request,userid):
    response = redirect('http://localhost:8100')
    response.set_cookie('UserId',value=str(userid), max_age=60 * 60 * 24,domain='127.0.0.1')
    return response
#获取辅导员的所有班级
@api_view(['GET'])
def getclass(request):
    fudaoyuanid=request.GET.get('fudaoyuanid','')
    if  not fudaoyuanid:
        fudaoyuanid='01016'
    querset=stuinfo.objects.filter(fudaoyuanid=fudaoyuanid).values('classname').distinct()
    classlist=[]
    for quersetone in querset:
        classlist.append(quersetone['classname'])
    return Response(classlist)


class StuinfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = stuinfo.objects.all()
    serializer_class = StuinfoSerializer
class PassresultsViewSet(viewsets.ModelViewSet):
    queryset = Passresults.objects.all()
    serializer_class = PassresultsSerializer
    @list_route(methods=['GET'])
    def querydataforfudaoyuan(self, request):
        userid='01016'
        startday=request.GET.get('startday','')
        endday=request.GET.get('endday','')
        tasktype=request.GET.get('tasktype','')
        classname=request.GET.get('classname','').strip()
        queryset = Passresults.objects.filter(userid__fudaoyuanid=userid, passdtday__range=(startday, endday),
                                              tasktype=tasktype,userid__classname__contains=classname)
        serializer = PassresultsSerializer(self.paginate_queryset(queryset), many=True)
        querysetdatainfo= Passresults.objects.filter(userid__fudaoyuanid=userid, passdtday__range=(startday, endday),userid__classname__contains=classname).values('tasktype').annotate(Count('id'))
        datainfo={}
        for querysetdatainfoone in querysetdatainfo:
            name=""
            if querysetdatainfoone['tasktype']=='晚归':
                name='wangui'
            elif querysetdatainfoone['tasktype']=='未归':
                name='weigui'
            else:
                name='yichang'
            datainfo[name] = querysetdatainfoone['id__count']
        datainfo['data']=serializer.data
        return Response(datainfo)
    @list_route(methods=['GET'])
    def querystatisticalforfudaoyuan(self,request):
        userid='01016'
        startday = request.GET.get('startday', '')
        endday = request.GET.get('endday', '')
        tasktype = request.GET.get('tasktype', '')
        queryset=Passresults.objects.filter(userid__fudaoyuanid=userid, passdtday__range=(startday, endday),
                                            tasktype=tasktype).values('userid__classname').annotate(Count('userid')).order_by('userid__classname')
        jsonlist=[]
        for querysetone in queryset:
            KVP={}
            KVP['classname']=querysetone['userid__classname']
            KVP['count']=querysetone['userid__count']
            jsonlist.append(KVP)
        return Response(jsonlist)

    @detail_route(methods=['POST','PUT'])
    def carestu(self,request,pk=None):
        req = json.loads(request.body.decode('utf-8'))
        carecontent = req['carecontent']
        passresultsid =pk
        userid='01016'
        result=False
        try:
            passresults = Passresults.objects.get(id=passresultsid)
            if passresults.userid.fudaoyuanid == userid:
                if carecontent and passresultsid:
                    care = Care(carecontent=carecontent)
                    care.save()
                    passresults.care = care
                    passresults.save()
                    result = True
        except:
            pass
        return  Response({'result':result})
    @detail_route(methods=['post'])
    def explainstu(self,request):
        explaincontent = request.POST.get('explaincontent', None)
        passresultsid = request.POST.get('id', None)
        result=False
        try:
            if explaincontent and passresultsid:
                explain=Explain(explaincontent=explaincontent)
                passresults=Passresults.objects.get(id=passresultsid)
                passresults.explaincontent=explaincontent
                passresults.save()
                result=True
        except:
            pass
        return  Response(result)