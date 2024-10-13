"""
Calculator_basic 모듈
기본적인 산술 연산을 제공하는 Calculator 클래스
"""
from .utils import round_result
class Calculator:
    def add(self, *args, **kwargs):
        """
        덧셈
        """
        result = sum(args)
        return self.format_result(result, **kwargs)
    
    def subtract(self, *args, **kwargs):
        """
        뺄셈
        """
        result = args[0] - sum(args[1:])
        return self.format_result(result, **kwargs)
    
    def multiply(self, *args, **kwargs):
        """
        곱셈
        """
        result = 1
        for num in args:
            result *= num
        return self.format_result(result, **kwargs)
    
    def divide(self, *args, **kwargs):
        """
        나눗셈
        """
        try:
            result = args[0]
            for num in args[1:]:
                result /= num
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        return self.format_result(result, **kwargs)
    
    def format_result(self, result, precision=None, return_float=False):
        """
        결과를 포맷팅
        """
        if precision is not None:
            result = round_result(result, precision)
            return f"{result:.{precision}f}"
        if return_float:
            return float(result)
        else:
            result = float(result)
            return int(result) if result.is_integer() else result
