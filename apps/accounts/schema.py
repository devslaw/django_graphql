import graphene
from graphene_django.types import DjangoObjectType
import graph_auth.schema

from .models import User
from .inputs import UserInput
from apps.core.utils import site_email



class UsersType(DjangoObjectType):
    class Meta:
        model = User


class AddUserEnum(graphene.Enum):
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    CLIENT = 'client'



class AddUser(graphene.Mutation):
    class Input:
        add_user_data = graphene.List(UserInput)

    user = graphene.Field(UsersType)

    @staticmethod
    def mutate(root, args, context, info):
        mutation = '''
            mutation{
              addUser(addUserData:{username:"test",firstName:"test",lastName:"test",email:"test@mailinator.com"}){
                user{
                  username
                }
              }
            }
        '''
        datas = args.get('add_user_data')
        for data in datas:
            user_company = data.get('company',None)
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                user_type='client'
            )
            user.save()
            to = [data['email']]
            site_email(to, 'invite', data, 'You have been invited')
        return AddUser(user=user)


class EditUser(graphene.Mutation):
    class Input:
        edit_user_data = graphene.Argument(UserInput)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, args, context, info):
        mutation = '''
            mutation{
              editUser(editUserData:{id:"11",firstName:"test",lastName:"test",email:"test@mailinator.com"}){
                ok
              }
            }
        '''

        data = args.get('edit_user_data')
        user = User.objects.get(id=data['id'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.save()
        ok = True
        return EditUser(ok=ok)


class InviteUser(graphene.Mutation):
    class Input:
        user_list = graphene.List(UserInput)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, args, context, info):
        user_list = args.get('user_list')
        for new_user in user_list:
            user = User(
                first_name=new_user['first_name'],
                last_name=new_user['last_name'],
                email=new_user['email'],
                username=new_user['first_name'],
                user_type='employee'
            )
            user.save()
        ok = True
        return InviteUser(ok=ok)


class Query(graphene.AbstractType):
    user_delete = graphene.Field(
        UsersType,
        id=graphene.Int(),
    )

    users = graphene.List(UsersType)

    def resolve_users(self, args, context, info):
        return User.objects.all()

    def resolve_user_delete(self, args, context, info):

        id = args.get('id')
        if isinstance(id, int):
            user = User.objects.get(id=id)
            if user is not None:
                return user.delete()
        return None

    users_with_type = graphene.List(
        UsersType,
        user_type=graphene.String()
    )

    def resolve_users_with_type(self, args, context, info):
        users = User.objects.all().filter(user_type=args.get('user_type'))
        return users


class Mutations(graph_auth.schema.Mutation, graphene.AbstractType):
    add_user = AddUser.Field()
    edit_user = EditUser.Field()
    invite_user = InviteUser.Field()
