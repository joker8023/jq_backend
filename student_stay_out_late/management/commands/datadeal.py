import datetime
import hashlib
import time
import urllib
from django.core.management.base import BaseCommand

from student_stay_out_late.models import Timesetting, Vthdpass, stuinfo, Passresults
from student_stay_out_late.util import message
def dataproceing():
    day='2017-05-21'
    day2= (datetime.datetime.strptime(day, '%Y-%m-%d')+datetime.timedelta(1)).strftime("%Y-%m-%d")
    timesetting=Timesetting.objects.get(id=1)
    quesetset=Vthdpass.objects.filter(passdtday=day,passdttime__gte=timesetting.starttime)|Vthdpass.objects.filter(passdtday=day2,passdttime__lte=timesetting.starttime).order_by('passdt')
    stuinfoall=stuinfo.objects.filter(permise='学生')
    data=[]
    for stuinfoone in stuinfoall:
        passresults=Passresults()
        passresults.userid=stuinfoone
        passresults.passinout=None
        passresults.passdtday=day
        passresults.passdttime=None
        passresults.lastpasstime=None
        passresults.tasktype='未归'
        for quesetsetone in quesetset:
            if stuinfoone==quesetsetone.userid:
                passresults.passdttime = quesetsetone.passdttime
                passresults.lastpasstime = quesetsetone.passdt
                if passresults.passinout== quesetsetone.passinout:
                    passresults.tasktype='异常'
                else:
                    passresults.passinout = quesetsetone.passinout
        if passresults.passinout==0 and passresults.passdttime<=timesetting.latetime and passresults.tasktype!='异常':
            passresults.tasktype='正常'
        elif passresults.passinout==0 and passresults.passdttime>timesetting.latetime:
            passresults.tasktype = '晚归'
        data.append(passresults)
    Passresults.objects.bulk_create(data)
class Command(BaseCommand):
    def handle(self, *args, **options):
        dataproceing()


