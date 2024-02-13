import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, num):
        removed_list = []
        if num > len(self.contents):
            num = len(self.contents)
        for i in range(num):
            remove_num = self.contents.pop(random.randrange(len(self.contents)))
            removed_list.append(remove_num)
        return removed_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat2 = copy.deepcopy(hat)
        drawball = hat2.draw(num_balls_drawn)
        b = 0
        for key, val in expected_balls.items():
            if drawball.count(key) >= val:
                b += 1
        if b == len(expected_balls):
            count += 1
            
    return count / num_experiments
