registers = {}

class Interpreter:
    def execute(self, instruction):
        instruction = what_to_execute["instructions"]
        parts = instruction.strip().split(" ")
        print(f"{parts}")
        if len(parts) == 3:
            op, arg1, arg2 = parts
            if op == "ADD":
                if arg1.isdigit():
                    arg1 = int(arg1)
                else:
                    arg1 = registers[arg1]

                if arg2.isdigit():
                    arg2 = int(arg2)
                else:
                    arg2 = registers[arg2]
                result = arg1 + arg2
                print(f"{arg1} + {arg2} = {result}")
            else:
                raise Exception(f"Unsupported operation: {op}")
        else:
            raise Exception(f"Invalid instruction: {instruction}")

what_to_execute = {
    "instructions": ["ADD 10 20"]
}

interpreter = Interpreter()
interpreter.execute(what_to_execute)

# while True:
#     instruction = input("Enter instruction: ")
#     if instruction == "exit":
#         break
#     execute(instruction)


# registers = {}

# def execute(instruction):
#     parts = instruction.strip().split(" ")
#     if len(parts) == 3:
#         op, arg1, arg2 = parts
#         if op == "ADD":
#             if arg1.isdigit():
#                 arg1 = int(arg1)
#             else:
#                 if arg1 in registers:
#                     arg1 = registers[arg1]
#                 else:
#                     raise Exception(f"Invalid register name: {arg1}")

#             if arg2.isdigit():
#                 arg2 = int(arg2)
#             else:
#                 if arg2 in registers:
#                     arg2 = registers[arg2]
#                 else:
#                     raise Exception(f"Invalid register name: {arg2}")

#             result = arg1 + arg2
#             return result
#         else:
#             raise Exception(f"Unsupported operation: {op}")
#     else:
#         raise Exception(f"Invalid instruction: {instruction}")

# while True:
#     instruction = input("Enter instruction: ")
#     if instruction == "exit":
#         break
#     parts = instruction.strip().split(" ")
#     if len(parts) == 3 and parts[0] == "ADD":
#         result = execute(instruction)
#         register_name = parts[-1]
#         registers[register_name] = result
#         print(f"{register_name} = {result}")
#     else:
#         raise Exception(f"Invalid instruction: {instruction}")
