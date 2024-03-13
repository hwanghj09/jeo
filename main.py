# 재오화이팅 언어 인터프리터

class 재오화이팅Interpreter:
    def __init__(self):
        self.변수들 = {}

    def 실행(self, 파일명):
        with open(파일명, 'r') as 파일:
            코드 = 파일.read()
            self.해석(코드)

    def 해석(self, 코드):
        명령어들 = 코드.split('\n')
        for 명령어 in 명령어들:
            self.실행명령어(명령어)

    def 실행명령어(self, 명령어):
        명령어 = 명령어.strip()  # 불필요한 공백 제거
        
        # 주석 또는 빈 줄인 경우 무시
        if not 명령어 or 명령어.startswith('#'):
            return

        토큰 = 명령어.split(maxsplit=1)
        
        if len(토큰) == 2:
            명령어_구분, 나머지 = 토큰
            if 명령어_구분 == '정수재오':
                self.정수변수_생성(나머지)
            elif 명령어_구분 == '실수재오':
                self.실수변수_생성(나머지)
            elif 명령어_구분 == '문자재오':
                self.문자변수_생성(나머지)
            elif 명령어_구분 == '출력재오':
                self.출력(나머지)
            else:
                print(f"에러: 알 수 없는 명령어 - {명령어}")
        else:
            print(f"에러: 잘못된 명령어 형식 - {명령어}")

    def 정수변수_생성(self, 명령어):
        변수명, 값 = 명령어.split('=')
        self.변수들[변수명.strip()] = int(값.strip())

    def 실수변수_생성(self, 명령어):
        변수명, 값 = 명령어.split('=')
        self.변수들[변수명.strip()] = float(값.strip())

    def 문자변수_생성(self, 명령어):
        변수명, 값 = 명령어.split('=')
        self.변수들[변수명.strip()] = 값.strip('\"')


    def 출력(self, 변수명):
        값 = self.변수들.get(변수명)
        if 값 is not None:
            print(값)
        else:
            print(f"에러: {변수명} 변수를 찾을 수 없습니다.")

# 사용자로부터 파일명 입력 받기
if __name__ == "__main__":
    파일명 = input("실행할 파일명을 입력하세요: ")
    interpreter = 재오화이팅Interpreter()
    interpreter.실행(파일명)
