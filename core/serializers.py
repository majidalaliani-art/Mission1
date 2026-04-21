from rest_framework import serializers
from .models import Report, ReportItemEvaluation, Location
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ReportItemEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportItemEvaluation
        fields = ['id', 'item_name', 'status']

class ReportSerializer(serializers.ModelSerializer):
    items = ReportItemEvaluationSerializer(many=True)
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Report
        fields = ['id', 'user', 'user_name', 'region', 'site_type', 'location', 'created_at', 'items']
        read_only_fields = ['user']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # The user will be injected in the view during perform_create
        report = Report.objects.create(**validated_data)
        for item_data in items_data:
            ReportItemEvaluation.objects.create(report=report, **item_data)
        return report
