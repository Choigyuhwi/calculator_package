"""
Calculator_Engineering 모듈
공학용 계산 기능을 제공하는 EngineeringCalculator 클래스
"""

import math
from .basic import Calculator
from .utils import round_result, convert_to_radians

class EngineeringCalculator(Calculator):
    def square_root(self, x, **kwargs):
        """
        제곱근
        """
        result = math.sqrt(x)
        return self.format_result(result, **kwargs)
    
    def power(self, x, y, **kwargs):
        """
        거듭제곱
        """
        result = math.pow(x, y)
        return self.format_result(result, **kwargs)
    
    def log(self, x, base=10, **kwargs):
        """
        로그
        """
        result = math.log(x, base)
        return self.format_result(result, **kwargs)
    
    def sin(self, x, angle_unit='degree', **kwargs):
        """
        사인
        """
        x = convert_to_radians(x, angle_unit)
        result = math.sin(x)
        return self.format_result(result, **kwargs)
    
    def cos(self, x, angle_unit='degree', **kwargs):
        """
        코사인
        """
        x = convert_to_radians(x, angle_unit)
        result = math.cos(x)
        return self.format_result(result, **kwargs)
    
    def tan(self, x, angle_unit='degree', **kwargs):
        """
        탄젠트
        """
        x = convert_to_radians(x, angle_unit)
        result = math.tan(x)
        return self.format_result(result, **kwargs)
    
    def divide(self, *args, **kwargs):
        try:
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    return "Error: Division by zero is not allowed."
                result /= num
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        return self.format_result(result, **kwargs)
