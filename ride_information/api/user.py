from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializer.user import UserSerializer
from ..models.user import User
from ..utils.pagination import CustomPaginationSettings
from ..utils.permission import IsAdminUser


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPaginationSettings
    permission_classes = [IsAuthenticated, IsAdminUser]

    def _get_user(self, pk):
        # Helper method to get the user by primary key (pk).
        return get_object_or_404(User, pk=pk)

    def list(self, request):
        queryset = get_list_or_404(User)

        # apply custom pagination
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'User created successfully',
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        user = self._get_user(pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        user = self._get_user(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'User updated successfully',
        }, status.HTTP_200_OK)

    def destroy(self, request, pk):
        user = self._get_user(pk)
        user.delete()
        return Response({
            'message': 'User deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)
