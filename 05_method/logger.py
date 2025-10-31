import logging
# import logging에 대해서 알아보자
# - 파이썬 기본 라이브러리 중 하나
# - 로그 찍는 기능을 제공하는 모듈
# - logging은 레벨, 시간, 모듈, 이름, 파일 저장 등 체계적으로 관리된다.
# - 진짜 서비스는 파일로 남기고, 서버 밖으로도 보내고, 경고만 따로 모으고 이런거 한다

class Logger:
# Logger라는 "틀(클래스)"을 하나 만듬
# "로그 세팅을 해주고, 실제로 쓸 수 있는 로거 객체를 뽑아주는 도구"
# 현실비유:
# -> Logger = 공장
# -> get_logger = 공장에서 제품 꺼내오는 함수
# -> 제품 = 진짜로 로그를 찍는 녀석

    logging.basicConfig(
        level=logging.INFO
        ,format='%(levelname)s: %(asctime)s %(message)s - [%(name)s]'
        ,datefmt='%H:%M:%S'
    )
# basicConfig는 "로깅 시스템의 기본 설정"
# 만든 Logger 클래스 안에서 이걸 한 번만 설정해주면 프로그램 전체가 이 스타일대로 로그를 찍는다

# 1) level=logging.INFO
# 로그에는 단계(심각도)가 있다
# level : debug > info > warning > error > critical
# level=logging.INFO 라는 것은 "INFO 이상부터는 출력하라"는 뜻
# DEBUG는 보여주지 말고 INFO, WARNING, ERROR, CRITICAL 은 보여줘 라는 의미

# 2) format='%(levelname)s: %(asctime)s %(message)s - [%(name)s]'
# "로그 한 줄을 어떤 형식으로 보여줄지"
# 각 의미:
# %(levelname)s -> 로그 레벨(INFO / ERROR 등)
# %(asctime)s -> 찍힌 시각
# %(message)s -> 우리가 남긴 메세지
# %(name)s -> 이 로그를 남긴 로거의 이름

# 3) datefmt='%H:%M:%S'
# 시간 표시 형식
# %H:%M:%S -> 시:분:초

    def get_logger(self,name):
        return logging.getLogger(name)

# 해석:
# - logging.getLogger(self,name) 은 이름이 name 인 로거 객체를 돌려줘
# - 이 로거 객체를 이용해서 .info(), .error() 이런 걸 호출할 수 있다

# 중요 포인트:
# name에 뭘 주느냐에 따라 로그에 찍히는 [name] 부분이 달라짐
# 보통은 __name__
# __name__ 은 현재 파이썬 파일 이름이라고 생각하면 됨
# 그래서 로그에서 "이 메세지가 어느 파일에서 찍힌 건지" 까지 자동으로 남는다.

# 요약하면 Logger 클래스의 역할은:
# - 한번 기본세팅(basicConfig)을 해주고...
# - 필요할 때마다 이름을 넣은 로거 객체를 받아서 쓸 수 있게 하는 도구