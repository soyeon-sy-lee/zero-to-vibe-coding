# 여러 할 일을 저장할 빈 리스트입니다.
todos = []

while True:
    print()
    print("===== Todo 앱 =====")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 종료")

    choice = input("메뉴를 선택하세요: ").strip()

    if choice == "1":
        todo = input("추가할 할 일을 입력하세요: ").strip()

        if todo == "":
            print("빈 할 일은 추가할 수 없습니다.")
            continue

        todos.append(todo)
        print("할 일이 추가되었습니다.")

    elif choice == "2":
        print()
        print("===== 할 일 목록 =====")

        if len(todos) == 0:
            print("아직 할 일이 없습니다.")
        else:
            for number, todo in enumerate(todos, start=1):
                print(f"{number}. {todo}")

    elif choice == "3":
        print("Todo 앱을 종료합니다.")
        break

    else:
        print("1, 2, 3 중에서 선택해주세요.")
