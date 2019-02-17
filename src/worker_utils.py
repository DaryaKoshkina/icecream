def worker_fn():
    print('Want to see the choice of buyers? Enter yes or no: ')
    worker_input = input()
    if worker_input == 'yes':
        with open('products.txt', 'r') as file:
            for line in file.readlines():
                print(line)
    elif worker_input == 'no':
        print('Bye :)')
    else:
        print('Sorry, I don\'t know this command: {0}'.format(worker_input))
