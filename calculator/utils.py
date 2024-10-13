"""
utils 모듈
이 모듈은 공통으로 사용되는 유틸리티 함수
"""

import math

def round_result(value, precision):
    """
    결과값을 지정된 정밀도로 반올림
    value: 반올림할 값
    precision: 반올림할 소수점 자리수 
    """
    return round(value, precision)

def convert_to_radians(angle, unit):
    """
    각도를 라디안으로 변환
    angle: 변환할 각도
    unit: 각도의 단위
    """
    if unit == 'degree':
        return math.radians(angle)
    return angle
    