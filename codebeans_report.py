#!/usr/bin/env python

from random import randint, sample, uniform
from codebeans import Product

ADJECTIVES = ['Iced', 'Hot', 'Sweet', 'Bubble', 'Honey']
NOUNS = [ 'Americano', 'Cafe Latte', 'Cappuccino', 'Milk Tea', 'Green Tea', 'Lemon Tea', '???']


def generate_products(num_products=30):
    products = []

    # TODO - 코드를 작성해주세요! 랜덤한 제품을 생성하고 추가할 수 있어야 합니다.
    # 샘플 이름 생성을 위해 random 모듈을 사용하면 유용할 수도..?

    for i in range(num_products) :
        ADJECTIVES_ran = randint(0, len(ADJECTIVES)-1)
        NOUNS_ran = randint(0, len(NOUNS)-1)
        name = ADJECTIVES[ADJECTIVES_ran] +' '+ NOUNS[NOUNS_ran]
        price = randint(5,100)
        size = randint(5,100)
        warmness = uniform(0.0,2.5)
        sweetness = uniform(0.0,2.5)
        products.append(Product(name,price,size,warmness,sweetness))

    return products


def inventory_report(products):

    print("CODEBEANS CORPORATION OFFICIAL INVENTORY REPORT")
    namelist = []
    pricelist = []
    sizelist = []
    warmnesslist = []
    sweetnesslist = []

    for i in range(30) :
        namelist.append(products[i].name)
        pricelist.append(products[i].price)
        sizelist.append(products[i].size)
        warmnesslist.append(products[i].warmness)
        sweetnesslist.append(products[i].sweetness)

    print('Unique product names: ',len(set(namelist)))
    print('Average price: ',sum(pricelist)/len(pricelist))
    print('Average size: ', sum(sizelist)/len(sizelist))
    print('Average warmness: ',sum(warmnesslist)/len(warmnesslist))
    print('Average sweetness: ',sum(sweetnesslist)/len(sweetnesslist))

    pass  # TODO - 코드를 작성해주세요! 계산된 보고서를 위해 제품들을 반복(loop)하여 확인해야 합니다.


if __name__ == '__main__':
    inventory_report(generate_products())
    