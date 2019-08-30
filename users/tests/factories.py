from factory import DjangoModelFactory, Faker

from ..models import User


class UserFactory(DjangoModelFactory):

    username = Faker('username'),
    first_name = Faker('first_name'),
    last_name = Faker('last_name'),
    email = Faker('email')

    class Meta:
        model = User
