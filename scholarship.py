def scholarship(college, GPA, highschool, YN):
    text = ''  # 초기 점수 설정
    if college == '연대생':
        if GPA >= 2.0:
            text = '국가 근로장학금'
            
        elif highschool == '과학고' :
            if YN_science_highschool == '네':
                text = '대통령과학장학금'

    elif college == '숙대생':
        if GPA >= 3.5:
            score = 90  # 숙대생은 GPA 3.5 이상일 때 90점
        elif 3.0 <= GPA < 3.5:
            score = 80
        elif 2.5 <= GPA < 3.0:
            score = 70
        else:
            score = 60  # GPA가 2.5 미만일 경우

    print(f"당신는 해당 장학금을 수여할 수 있습니다: {text}.")

# 사용자 입력 받기
user_college = input("당신은 연대생이신가요, 숙대생이신가요? ")
user_GPA = float(input("당신의 학점을 입력하세요: "))  # 학점을 실수형으로 변환
user_highschool = input("당신은 과학고, 일반고, 영재학교 중에서 어디를 나오셨나요?")
user_YN_science_highschool = input("당신은 석차 4등급 이내 과목 10과목 이상 또는 24단위 이상 이수하셨나요?")


# 함수 호출
scholarship(user_college, user_GPA)
