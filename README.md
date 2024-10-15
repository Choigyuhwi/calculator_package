# Calculator 패키지
이 패키지는 기본 계산기, 공학용 계산기, 복소수 계산기를 제공하며, 다양한 수학적 연산을 간편하게 수행할 수 있습니다. 이 문서에서는 각 계산기의 사용법과 주요 기능을 설명합니다.

## 목차

- [환경](https://github.com/Choigyuhwi/calculator_package/blob/master/README.md#환경)
- [프로젝트 개요](https://github.com/Choigyuhwi/calculator_package/blob/master/README.md#프로젝트-개요)
- [디렉토리 구조](https://github.com/Choigyuhwi/calculator_package/blob/master/README.md#디렉토리-구조)
- [패키지 설치](https://github.com/Choigyuhwi/calculator_package/blob/master/README.md#패키지-설치)
- [사용법](https://github.com/Choigyuhwi/calculator_package/blob/master/README.md#사용법)

## 환경
- Python 3.10.14
- git version 2.25.1

## 프로젝트 개요
이 프로젝트에는 계산기 패키지를 구성하는 기본 계산기, 공학용 계산기, 복소수 계산기의 코드가 포함되어 있습니다.

- 기본 계산기: 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지, 제곱, 제곱근, 로그, 삼각함수, 지수함수 등의 기본적인 수학 연산을 제공합니다.
- 공학용 계산기: 기본 계산기의 기능에 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지, 제곱, 제곱근, 로그, 삼각함수, 지수함수 등의 기본적인 수학 연산을 제공합니다.
- 복소수 계산기: 복소수의 합, 차, 곱, 나눗셈, 크기, 각도, 극좌표 변환 등의 복소수 연산을 제공합니다.

## 디렉토리 구조

```
calculator_package/
├── calculator/
│   ├── __init__.py
│   ├── basic.py
│   ├── engineering.py
│   ├── complex.py
│   └── utils.py  
├── test/
│   ├── __init__.py
│   ├── test_basic.py
│   ├── test_engineering.py
│   ├── test_complex.py
``` 

## 패키지 설치

```bash
git clone https://github.com/Choigyuhwi/calculator_package.git
cd AI-calculator_package
```

## 사용법

### 기본 계산기

```python

from calculator import Calculator

calc = Calculator()

print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: 50.000
```

### 공학용 계산기

```python

from calculator import EngineeringCalculator

eng_calc = EngineeringCalculator()

print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
print(eng_calc.log(100, precision=4))  # 출력: 2.0000
print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000
print(eng_calc.divide(5, 0)) "Division by zero is not allowed"
```

### 복소수 계산기

```python

from calculator import ComplexCalculator

complex_calc = ComplexCalculator()
z1 = 1+2j
z2 = 3+4j
print(complex_calc.add(z1, z2))  # 출력: (4+6j)
print(complex_calc.magnitude(z1))  # 출력: 2.23606797749979
print(complex_calc.argument(z1))  # 출력: 1.1071487177940904
print(complex_calc.to_polar(z1))  # 출력: (2.23606797749979, 1.1071487177940904)
print(complex_calc.to_rectangular(2.23606797749979, 1.1071487177940904))  # 출력: (1.0000000000000002+2j)
```

### 모듈 구성

- basic.py: 기본 계산기 모듈
- engineering.py: 공학용 계산기 모듈
- complex.py: 복소수 계산기 모듈
- utils.py: 공통으로 사용되는 유틸리티 함수 모듈

