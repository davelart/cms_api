from rest_framework import serializers

from attendance.models import Attendance, AttendanceProgram

class AttendanceProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceProgram
        exclude = ['datecreated']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ['datecreated']