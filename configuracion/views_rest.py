
# Third's Libraries
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication

# Own's Libraries
from .models import Empresa
from .serializers import EmpresaSerializer
from .pagination import GenericPagination


class EmpresaByPageAPI(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    pagination_class = GenericPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, SessionAuthentication, )

    def get_queryset(self):

        if self.request.user.is_staff:
            empresas = Empresa.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()

        return empresas
