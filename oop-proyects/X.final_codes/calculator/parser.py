#!/usr/bin/python3

from operadores import add, subtract, multiply, divide


class Parser:
    def evaluate(self, expression):
        # Convertir el texto en una lista
        tokens = expression.split()

        tokens = self.resolve_mul_div(tokens)

        result = self.resolve_add_sub(tokens)

        return result

    def resolve_mul_div(self, tokens):
        new_list = []
        a = 0

        while a < len(tokens):
            token = tokens[a]

            if token == "*":
                last = float(new_list.pop())
                next_number = float(tokens[a + 1])
                result = multiply(last, next_number)
                new_list.append(str(result))
                a += 2

            elif token == "/":
                last = float(new_list.pop())
                next_number = float(tokens[a + 1])
                result = divide(last, next_number)
                new_list.append(str(result))
                a += 2

            else:
                new_list.append(token)
                a += 1

        return new_list

    def resolve_add_sub(self, tokens):
        result = float(tokens[0])
        a = 1

        while a < len(tokens):
            operator = tokens[a]
            number = float(tokens[a + 1])

            if operator == "+":
                result = add(result, number)
            elif operator == "-":
                result = subtract(result, number)

            a += 2

        return result
