import factory
from faker import Factory

from ..models import (
    User,
)

# list all fakers:
# from faker import Faker
# F = Faker()
# dir(F)

faker = Factory.create(locale="de_DE")


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = factory.Sequence(lambda n: "email%d@localhost" % n)
    password = factory.PostGenerationMethodCall("set_password", "passw0rd")
    profile_image = factory.django.ImageField(color="blue")
