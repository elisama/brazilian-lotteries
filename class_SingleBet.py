"""
Class SingleBet - Defines
"""
import numpy as np

LOTOFACIL_NUMBERS = np.arange(1, 25, dtype=int)

class SingleBet():
    """
    """
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def verify_draw(self, draw_result):
        """

        """
        result_of_draw = 0
        for number in self:
            for number_2 in draw_result:
                if number == number_2:
                    result_of_draw += 1
        return result_of_draw


    def generate_random_bet(self, numbers_of_numbers, set_of_all_numbers):
        """
        """


    def generate_complementar_bet(self):
        """
        """


# Unitary Test of Class SingleBet
if __name__ == "__main__":
    # the most simple bet of the Lotofácil lottery
    bet = SingleBet(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    
    # the first draw of Lotofácil lottery in sept/29/2003
    draw = SingleBet(np.array([1, 3, 5, 6, 9, 10, 11, 13, 14, 16, 18, 20, 23, 24, 25]))
    
    # print the
    print(bet.verify_draw(draw))
    
    # generate a random bet of 15 numbers chosen
    # from the set {1, 2, 3, ..., 23, 24, 25}
    random_bet = SingleBet([])
    print(LOTOFACIL_NUMBERS)
    print(random_bet.generate_random_bet(15, LOTOFACIL_NUMBERS))