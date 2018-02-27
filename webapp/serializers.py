from rest_framework import serializers

from webapp.models import employees


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields=('firstname','lastname')