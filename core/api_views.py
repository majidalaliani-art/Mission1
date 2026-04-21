from rest_framework import viewsets, permissions
from .models import Report, Location
from .serializers import ReportSerializer, LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Simple search or filtering can be added here if needed

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow superusers/staff to see all, regular users see only their own
        user = self.request.user
        if user.is_staff:
            return Report.objects.all().order_by('-created_at')
        return Report.objects.filter(user=user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the new report
        serializer.save(user=self.request.user)
