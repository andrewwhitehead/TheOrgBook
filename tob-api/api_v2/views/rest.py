from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api_v2.serializers import (
    IssuerSerializer,
    SchemaSerializer,
    CredentialTypeSerializer,
    TopicSerializer,
    CredentialSerializer,
    AddressSerializer,
    ClaimSerializer,
    ContactSerializer,
    NameSerializer,
    PersonSerializer,
)
from api_v2.models.Issuer import Issuer
from api_v2.models.Schema import Schema
from api_v2.models.CredentialType import CredentialType
from api_v2.models.Topic import Topic
from api_v2.models.Credential import Credential
from api_v2.models.Address import Address
from api_v2.models.Claim import Claim
from api_v2.models.Contact import Contact
from api_v2.models.Name import Name
from api_v2.models.Person import Person


class IssuerViewSet(ViewSet):
    def list(self, request):
        queryset = Issuer.objects.all()
        serializer = IssuerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Issuer.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = IssuerSerializer(item)
        return Response(serializer.data)


class SchemaViewSet(ViewSet):
    def list(self, request):
        queryset = Schema.objects.all()
        serializer = SchemaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Schema.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SchemaSerializer(item)
        return Response(serializer.data)


class CredentialTypeViewSet(ViewSet):
    def list(self, request):
        queryset = CredentialType.objects.all()
        serializer = CredentialTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CredentialType.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CredentialTypeSerializer(item)
        return Response(serializer.data)


class TopicViewSet(ViewSet):
    def list(self, request):
        queryset = Topic.objects.all()
        serializer = TopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(item)
        return Response(serializer.data)


class CredentialViewSet(ViewSet):
    def list(self, request):
        queryset = Credential.objects.all()
        serializer = CredentialSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Credential.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CredentialSerializer(item)
        return Response(serializer.data)


class AddressViewSet(ViewSet):
    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(item)
        return Response(serializer.data)


class ClaimViewSet(ViewSet):
    def list(self, request):
        queryset = Claim.objects.all()
        serializer = ClaimSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Claim.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ClaimSerializer(item)
        return Response(serializer.data)


class ContactViewSet(ViewSet):
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contact.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(item)
        return Response(serializer.data)


class NameViewSet(ViewSet):
    def list(self, request):
        queryset = Name.objects.all()
        serializer = NameSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Name.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = NameSerializer(item)
        return Response(serializer.data)


class PersonViewSet(ViewSet):
    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(item)
        return Response(serializer.data)
