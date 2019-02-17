from src.consumer_utils import consumer_fn
from src.worker_utils import worker_fn


if __name__ == '__main__':
    print('Hello, if you are a consumer, enter 1\n'
          'If you worker, enter 2')
    user_type = input()
    if user_type == '1':
        consumer_fn()
    elif user_type == '2':
        worker_fn()
    else:
        print('Sorry, I don\'t know this type: {0}'.format(user_type))

