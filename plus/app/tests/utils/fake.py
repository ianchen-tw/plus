from faker import Faker

# TODO: move this file to testutil
Faker.seed(1234)


# exported fidlds
fakeChinese = Faker("zh_TW")
fake = Faker()
