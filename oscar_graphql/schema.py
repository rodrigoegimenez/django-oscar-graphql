import graphene

from oscar_graphql.catalogue.schema import Query as CatalogueQuery
from oscar_graphql.partner.schema import Query as PartnerQuery


class Query(CatalogueQuery, PartnerQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
