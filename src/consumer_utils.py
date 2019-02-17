from src.menu import menu_dict


def get_price(product):
    try:
        price = menu_dict[product]
    except KeyError:
        print('Not found {0}'.format(product))
        return 0
    return price


def get_check(products_list):
    check = 0
    for product in products_list:
        price = get_price(product)
        if price == 0:
            products_list.remove(product)
        else:
            check += price

    return check


def write_products_to_file(products_list, user_name):
    with open('products.txt', 'a') as file:
        products_dict = {user_name: products_list}
        file.write(str(products_dict) + '\n')


def consumer_fn():
    print('Input your user name: ')
    user_name = input()

    products_list = []
    print(
        'Select ice cream: vanilla, chocolate, lemon, orange, pistachio. \n '
        'If u wanna stop shopping input \'check\'')
    while True:
        print('Continue or check')
        user_input = input()
        if user_input != 'check':
            products_list.append(user_input)
        else:
            break

    check = get_check(products_list)
    print('Your check is: {0}'.format(check))

    write_products_to_file(products_list, user_name)
