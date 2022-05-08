print("------ 여기 아래 부터 실행 결과 입니다 -----")
print("[예제] 기본 응용 - 점수 평가")

cutline = 60


def is_pass(target_point):
    if target_point >= cutline:
        return True
    else:
        return False


points = [
    ["영어", 61],
    ["국어", 80],
    ["수학", 55],
    ["국사", 30],
    ["과학", 65],
]

print("점수 표 :", points)
print(f"커트라인 {cutline} 점 이상")
print()

totalPoint = 0
testCount = len(points)
winCount = 0

for point in points:
    totalPoint = totalPoint + point[1]
    if is_pass(point[1]):
        print(f"{point[0]} {point[1]}점으로 합격입니다")
        winCount = winCount + 1
    else:
        print(f"{point[0]} {point[1]}점으로 불합격입니다")

print()
print(f"총점 : {totalPoint}점 / 평균 : {totalPoint / testCount}점({testCount}과목) / 합격 수 : {winCount}")
