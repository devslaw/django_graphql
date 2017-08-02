import graphene



class UserInput(graphene.InputObjectType):
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    id = graphene.String(Required=False)
    company = graphene.String(Required=False)
    status = graphene.String(Required=False)