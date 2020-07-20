"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name #name as string
        self.flavor = flavor #str
        self.price = price #price of this cupcake
        self.qty = 0 # the amount of this cupcake in int
        self.cache[name] = self

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    """Instance methods"""

    def add_stock(self, amount):
        """Adds amount to self.qty"""

        self.qty += amount

    def sell(self, amount):
        """Sell the given amount of cupcakes and update self.qty"""

        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
        if self.qty - amount < 0:
            self.qty = 0
        else:
            self.qty -= amount

    """Static Methods"""

    @staticmethod
    def scale_recipe(ingredients, amount):
        multiplied_amounts = []
        for ingredient in ingredients:
            multiplied_ingredient = ingredient[1] * amount
            multiplied_amounts.append((ingredient[0], multiplied_ingredient))
        return multiplied_amounts





if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
