from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 필요한 패키지를 여기에 나열하세요
    ],
    author='Choi GyuHwi', # 작성자
    author_email='myckh527@gmail.com', # 이메일
    description='A package for basic, engineering, and complex number calculations', # 설명
    long_description=open('README.md').read(), # 설명
    long_description_content_type='text/markdown', # 설명 타입
    url='https://github.com/yourusername/calculator', # 깃허브 주소
    classifiers=[   
        'Programming Language :: Python :: 3', # 파이썬 버전
        'License :: OSI Approved :: MIT License', # 라이선스
        'Operating System :: OS Independent', # 운영체제
    ],
    python_requires='>=3.8', # 파이썬 버전
)