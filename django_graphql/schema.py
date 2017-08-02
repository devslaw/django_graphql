import graphene
from graphene_django.debug import DjangoDebug
import apps.accounts.schema

class Query(
    apps.accounts.schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name='__debug')

class Mutations(
    apps.accounts.schema.Mutations,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(query=Query, mutation=Mutations)
