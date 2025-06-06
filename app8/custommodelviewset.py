from rest_framework import status
from rest_framework import viewsets
from app8.customresponse import CustomResponse

class CustomModelViewSet(viewsets.ModelViewSet):

    #CreateModelMixin->create
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return CustomResponse(data=serializer.data, code=201,msg="OK", status=status.HTTP_201_CREATED,headers=headers)
    #ListModelMixin->list
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None: # 如果分页，则调用get_paginated_response()方法返回分页响应
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return CustomResponse(data=serializer.data, code=200, msg="OK", status=status.HTTP_200_OK)
    #RetrieveModelMixin->retrieve
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(data=serializer.data, code=200, msg="OK", status=status.HTTP_200_OK)
    #UpdateModelMixin->update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return CustomResponse(data=serializer.data, code=200, msg="OK", status=status.HTTP_200_OK)

    #DestroyModelMixin->destroy
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return CustomResponse(data=[], code=204, msg="OK", status=status.HTTP_204_NO_CONTENT)