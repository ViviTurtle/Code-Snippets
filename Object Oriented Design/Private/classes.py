class _Private(object):

    def __init__(self, fruit):
        self._best_fruit = fruit

    def _private_class(self):
        print(f'The private Fruit is {self._best_fruit}')

    def public_class(self):
        print(f'The private Fruit is {self._best_fruit}')


class Public(object):

    def __init__(self, fruit):
        self._best_fruit = fruit

    def _private_class(self):
        print(f'The public Fruit is {self._best_fruit}')

    def public_class(self):
        print(f'The public Fruit is {self._best_fruit}')
