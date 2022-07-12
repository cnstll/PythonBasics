from cgitb import reset
import time
from random import randint
import os


def format_time_diff(diff):
    if diff >= 1e-3:
        formated_time = f"{diff:.3f} s"
    elif diff >= 1e-6:
        formated_time = f"{diff * 1e3:.3f} ms"
    else:
        formated_time = f"{diff * 1e6:.3f} μs"
    return formated_time


def log(func):
    '''
        Decorator to measure execution time of a function
        and log it into 'machine.log' file
    '''
    def inner(*arg):
        start = time.perf_counter()
        res = func(*arg)
        end = time.perf_counter()
        diff = end - start
        func_name = str(func.__name__).replace('_', ' ').title()
        f_time = format_time_diff(diff)
        # Add formated log line to file
        login = os.getlogin()
        line = f"({login})Running: {func_name:<19}[ exec-time = {f_time} ]\n"
        with open('machine.log', 'a') as f:
            f.write(line)
        return res
    return inner


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
