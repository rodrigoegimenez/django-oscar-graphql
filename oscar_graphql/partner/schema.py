# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType
from oscar.core.loading import get_model

StockRecord = get_model('partner', 'stockrecord')


class StockRecordType(DjangoObjectType):
    class Meta:
        model = StockRecord
        fields = '__all__'


class Query(graphene.ObjectType):
    stockrecords = graphene.List(StockRecordType)
    stockrecord_by_id = graphene.Field(StockRecordType, id=graphene.String())

    def resolve_stockrecords(root, info):
        return StockRecord.objects.all()

    def resolve_stockrecord_by_id(root, info, id):
        return StockRecord.objects.get(id=id)
