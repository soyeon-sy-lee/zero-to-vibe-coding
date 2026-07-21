import random

answer = random.randint(1, 100)
attempts = 0

print("숫자 맞추기 게임을 시작합니다!")
print("1부터 100 사이의 숫자를 맞춰보세요.")
print("종료하려면 q를 입력하세요.")

while True:
    guess = input("숫자를 입력하세요: ").strip()

    if guess.lower() == "q":
        print(f"게임을 종료합니다. 정답은 {answer}였습니다.")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("1부터 100 사이의 정수를 입력해주세요.")
        continue

    if guess < 1 or guess > 100:
        print("1부터 100 사이의 정수를 입력해주세요.")
        continue

    attempts += 1

    if guess < answer:
        print("더 큰 숫자입니다.")
    elif guess > answer:
        print("더 작은 숫자입니다.")
    else:
        score = max(0, 100 - (attempts - 1) * 5)
        print("정답입니다! 축하합니다!")
        print(f"{attempts}번 만에 맞혔습니다.")
        print(f"점수: {score}점")
        break
