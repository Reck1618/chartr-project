from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request, *args, **kwargs):
        title = self.request.query_params.get('title', None)
        queryset = self.get_queryset()

        if title:
            queryset = queryset.filter(title__icontains=title)

        if not queryset.exists():
            return Response({'detail': 'No notes found matching the query'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
