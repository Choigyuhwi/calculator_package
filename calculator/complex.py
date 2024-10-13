import cmath

class ComplexCalculator:
    def add(self, z1, z2):
        """
        두 복소수의 합을 계산합니다.
        """
        return z1 + z2

    def subtract(self, z1, z2):
        """
        두 복소수의 차를 계산합니다.
        """
        return z1 - z2

    def multiply(self, z1, z2):
        """
        두 복소수의 곱을 계산합니다.
        """
        return z1 * z2

    def divide(self, z1, z2):
        """
        두 복소수의 나눗셈을 계산합니다.
        """
        try:
            return z1 / z2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def magnitude(self, z):
        """
        복소수의 절대값을 계산합니다.
        """
        return abs(z)

    def argument(self, z):
        """
        복소수의 편각을 계산합니다.
        """
        return cmath.phase(z)

    def to_polar(self, z):
        """
        복소수를 극 좌표계로 변환합니다.
        """
        return cmath.polar(z)

    def to_rectangular(self, r, theta):
        """
        극 좌표계를 복소수로 변환합니다.
        """
        return cmath.rect(r, theta)
        