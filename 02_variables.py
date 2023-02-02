# def s():
#     a = 1
#     b = 2
#     print(a + b)



class Interpreter:
    def __init__(self):
        self.stack = []
        self.enviroment = {}
    
    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.enviroment[name] = val

    def LOAD_VALUE(self, name):
        val = self.enviroment[name]
        self.stack.append(val)

    def parse_argument(self, instruction, argument, what_to_execute):
        """ Understand what the argument to each instruction means."""
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_VALUE", "STORE_NAME"]

        if instruction in numbers:
            argument = what_to_execute['numbers'][argument]
        elif instruction in names:
            argument = what_to_execute["names"][argument]
        return argument

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)

    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]

        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)

            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instruction == "STORE_NAME":
                self.STORE_NAME(argument)
            elif instruction == "LOAD_NAME":
                self.LOAD_VALUE(argument)

    def execute(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.parse_argument(instruction, argument, what_to_execute)
            bytecode_method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)

what_to_execute = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("STORE_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("STORE_VALUE", 1),
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None)],
    "numbers": [1, 2],
    "names": ["a", "b"] }

interpreter = Interpreter()
interpreter.execute(what_to_execute)