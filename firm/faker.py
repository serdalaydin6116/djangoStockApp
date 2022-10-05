from .models import Firm, Category, Brand, Product,Stock
from faker import Faker

def run():
    '''
        python manage.py shell
        from .faker import run
        run()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    fake = Faker()
    firms = (
        "Unilever",
        "Nestle",
        "Ulker",
        "Mitsubishi",
    )

    for firm in firms:
        new_firm = Firm.objects.create(f_name = firm)
        for _ in range(50):
            Stock.objects.create(user=fake.user, firm = new_firm, product = fake.product(), quantity = fake.quantity(), price = fake.price())
    
    print('OK')
