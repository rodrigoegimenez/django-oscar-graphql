# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType
from oscar.core.loading import get_model, get_class

Product = get_model('catalogue', 'Product')
Selector = get_class("partner.strategy", "Selector")


class PriceType(graphene.ObjectType):
    incl_tax = graphene.Int()
    excl_tax = graphene.Int()
    tax = graphene.Int()

    def resolve_incl_tax(parent, info):
        if parent.incl_tax is not None:
            return int(parent.incl_tax * 100)
        else:
            return None

    def resolve_excl_tax(parent, info):
        if parent.excl_tax is not None:
            return int(parent.excl_tax * 100)
        else:
            return None

    def resolve_tax(parent, info):
        if parent.tax is not None:
            return int(parent.tax * 100)
        else:
            return None


class ProductType(DjangoObjectType):
    price = graphene.Field(PriceType)

    def resolve_price(self, info):
        strategy = Selector().strategy()
        return strategy.fetch_for_product(self).price

    class Meta:
        model = Product
        fields = '__all__'


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    product_by_id = graphene.Field(ProductType, id=graphene.String())

    def resolve_products(root, info):
        return Product.objects.all()

    def resolve_product_by_id(root, info, id):
        return Product.objects.get(id=id)
