class DivisionByNull:

    @staticmethod
    def div_by_null(a, b):
        try:
            return a / b
        except:
            return f"Деление на ноль недопустимо"


print(DivisionByNull.div_by_null(10, 0))
print(DivisionByNull.div_by_null(10, 5))
print(DivisionByNull.div_by_null(100, -5))

