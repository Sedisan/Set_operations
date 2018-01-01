from enum import Enum
import copy
from logging import warn as logging_warn

class PossibleChoises(Enum):
    UNION = 1
    INTERSECTION = 2
    DIFFERENCE = 3
    SYMMETRIC_DIFFERENCE = 4

    @staticmethod
    def print_choises(msg):
        set_with_number = set({})
        for i,j in PossibleChoises.__members__.items():
            set_with_number.add(j.value)
            print("{}: {} to {}".format(msg, j.value, j.name))
        return set_with_number
    @staticmethod
    def get_selected_value(val):
        return PossibleChoises(val).name.lower()


class DefaultSet(object):    
    def __init__(self, first_set, second_set):
        self.first_set = copy.deepcopy(first_set)
        self.second_set = copy.deepcopy(second_set)
        self.fill_default_values()

    def fill_default_values(self):
        self.first_set = set(tuple(list(range(0, 6))))
        self.second_set = set(tuple(list(range(5, 11))))

class Operation(DefaultSet):  
    def __init__(self):
        self.first_set = set()
        self.second_set = set()
        super().__init__(self.first_set, self.second_set)

    def get_first_set(self):
        return self.first_set

    def get_second_set(self):
        return self.second_set

    def set_up_set(self):
        self.first_set.clear()
        self.second_set.clear()
        print("How many elements of the first set would you like inserted?")
        how_many = 0
        how_many = LoadUserData.load(how_many)
        print("How many elements of the second set would you like inserted?")
        how_many_second = 0
        how_many_second = LoadUserData.load(how_many)
        self.__fill(how_many, how_many_second)
            
    def __fill(self, how_many, how_many_second):
        self.first_set = self.__fill_set_by_for(how_many, 'first')
        self.second_set = self.__fill_set_by_for(how_many_second, 'second')

    def __fill_set_by_for(self, what, which_one):
        temp_set = set()
        temp_set.update([])
        for elem in range(what):
            print("Insert: ", elem, 'to your %s set' % which_one)
            what_element = input(':')
            if what_element in temp_set:
                print("Element{} exist".format(what_element))
                continue
            temp_set.add(what_element)
            print("Element: %s was added"% what_element)
        return temp_set


class DealWithIt(Operation):
    def __init__(self):
        super().__init__()
        self.count_it()
        
    def count_it(self):
        result = self.start_program()
        print('\n' * 100) # Yeah, High Life
        print("Result of your operation:")
        user_result = set(getattr(self.get_first_set(), result)( self.get_second_set()))
        print(*user_result)
    
    def start_program(self):
        print("Hello!\nWelcome to my calculator of set. The program will be computed only first from the second one.\n" +
              "Default sets: \nFirst set:{}\nSecond set:{} \nWould you like to create new sets(press 1), or use deafault?(input any number)".format(self.get_first_set(),self.get_second_set()))
        us_dec = 0
        us_dec = LoadUserData.load(us_dec)
        if us_dec == 1:
            self.set_up_set()
        print("Okay! Now select operation in this range: ")
        numbers = PossibleChoises.print_choises("Type")
        us_dec = None
        while us_dec not in numbers:
            us_dec = LoadUserData.load(us_dec)
            print(us_dec)
            if us_dec not in numbers:
                print("Out of range")
        try:
            us_dec = PossibleChoises.get_selected_value(us_dec)
        except KeyError:
            raise KeyError("Bad Key. Please contact with me to repair it")
        return us_dec


class LoadUserData(object):
    @staticmethod
    def load(variable_to_load, type_variable = int):
        if not isinstance(variable_to_load, type_variable) and not isinstance(variable_to_load, type(None)):
            logging_warn("Gotten type is not correct")
            type_variable = LoadUserData.__get_type_of_argument(variable_to_load)
        while True:
            try:
                check_type = input(':')
                variable_to_load = type_variable((check_type))
                break
            except ValueError:
                print("Expected type of:", type_variable)
                try:
                    print("Type got:", str(type(check_type)))
                except NameError:
                    pass
                continue
        return variable_to_load
    
    @staticmethod
    def __get_type_of_argument(argument):
        try:
            data = str(type(argument))
            data = data.split("'")
            data = data[1]
            # EVAL WITH USER TYPE DATA
            data = eval(data)
            logging_warn("Incorrect data type has been correctly repaired")
            return data
        except NameError:
            raise NameError("Incorrect data type hasn't repaired")
        except TypeError:
            raise TypeError("Error with type(probably casting string)")


while True:
    try:
        start = DealWithIt()
        print("Try it again? 1 to accept. Other number to decline")
        exit_or_no = 0
        exit_or_no = LoadUserData.load(exit_or_no, type(exit_or_no))
        print(exit_or_no)
        if exit_or_no is not 1:
            break
    except KeyboardInterrupt:
        print("Program has been interrupted by keyboard")
        break
        
print("Thank for use. Created by:{}".format('Szymon Ryl'))
