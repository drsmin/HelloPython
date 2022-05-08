print("------ 여기 아래 부터 실행 결과 입니다 -----")
print("[예제] 제어문")

point = 60
cutline = 80

print(f"점수 : {point} / 커트라인 : {cutline}")
print("if문 테스트 START")

if point > cutline:
    print("점수가 커트라인을 넘었습니다")
else:
    print("점수가 커트라인을 넘지 못했습니다")

print("if문 테스트 END")

print()
print()
print("for문 테스트 START")
for idx in range(0, 10):
    print("for문 테스트 중입니다", idx, "번째")
print("for문 테스트 END")
