from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 42
        b = 6
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 48
        assert result == expected

    def test_substract(self):
        # arrange
        a = 42
        b = 6
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 36
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 42
        b = 6
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 252
        assert result == expected
    
    def test_divide(self):
        # arrange
        a = 42
        b = 6
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 7
        assert result == expected

    def test_divideerror(self):
        # arrange
        a = 42
        b = 0
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = "Division by zero error"
        assert result == expected
