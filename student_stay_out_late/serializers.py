from rest_framework import serializers

from student_stay_out_late.models import Passresults, stuinfo, Care, Explain


class StuinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = stuinfo
        fields = ('userid', 'username', 'gender', 'classname','major','department','permise','fudaoyuanid','fudaoyuanname')
class CareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Care
        fields=('caretime','carecontent')
class ExplainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Explain
        fields=('explaintime','explaimcontent','ifagree')
class PassresultsSerializer(serializers.ModelSerializer):
    userid = StuinfoSerializer(read_only=True)
    care = CareSerializer(read_only=True)
    explain = ExplainSerializer(read_only=True)
    class Meta:
        model = Passresults
        fields = ('id','passinout', 'passdtday', 'tasktype', 'lastpasstime','userid','care','explain')