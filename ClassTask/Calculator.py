class Calculate:
    def __init__(self, firstNumber, secondNumber, operand):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        self.thirdNumber = operand

    def calculator(self):
        result = 0
        match self.operand:
            case '+':
                result = self.firstNumber + self.secondNumber
                return result
            case '-':
                result = self.firstNumber - self.secondNumber
                return result
            case '/':
                result = self.firstNumber / self.secondNumber
                return result
            case '*':
                result = self.firstNumber * self.secondNumber
        return result

    def __str__(self):
        return f"{self.firstNumber} {self.secondNumber}"


calc = Calculate(3, 4, "-")
print(calc.calculator())
