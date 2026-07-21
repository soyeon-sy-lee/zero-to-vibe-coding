"""
Zero to Vibe Coding
코딩을 한 번도 해본 적 없는 사람을 위한 대화형 Python·Codex 입문서
"""

from dataclasses import dataclass

PYTHON_DOWNLOAD_URL = "https://www.python.org/downloads/"
CODEX_DOWNLOAD_URL = "https://developers.openai.com/codex/app"


@dataclass
class Step:
    title: str
    description: list[str]
    action: str
    expected: str | None = None
    faq: str | None = None


def line() -> None:
    print("\n" + "=" * 72)


def small_line() -> None:
    print("-" * 72)


def wait() -> None:
    input("\n여기까지 했다면 Enter를 눌러 다음으로 넘어가세요...")


def show_step(number: int, step: Step) -> None:
    line()
    print(f"STEP {number}. {step.title}")
    for paragraph in step.description:
        print(f"\n{paragraph}")
    print("\n직접 해보기")
    small_line()
    print(step.action.strip())
    small_line()
    if step.expected:
        print("\n정상적으로 되었다면")
        small_line()
        print(step.expected.strip())
        small_line()
    if step.faq:
        print("\n🙋 초보자가 자주 묻는 질문")
        small_line()
        print(step.faq.strip())
        small_line()
    wait()


def ask(message: str) -> str:
    return input(f"\n{message}\n> ").strip()


def yes_no(message: str) -> bool:
    while True:
        answer = ask(f"{message} (y/n)").lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("y 또는 n을 입력해주세요.")


def show_intro() -> None:
    line()
    print("🚀 Zero to Vibe Coding")
    print("코딩을 한 번도 해본 적 없는 사람을 위한 AI 개발 입문")
    print()
    print("이 튜토리얼은 정말 아무것도 모른다고 가정합니다.")
    print("터미널이 무엇인지, 파일이 어디에 생기는지 몰라도 괜찮습니다.")
    print()
    print("오늘의 목표:")
    print("내 컴퓨터에서 Python 파일을 만들고 실행한 뒤,")
    print("Codex에게 자연어로 코드를 수정시켜보기")


def mac_steps() -> list[Step]:
    return [
        Step(
            "Python 설치하기",
            [
                "Python은 우리가 작성한 코드를 컴퓨터가 실행할 수 있게 해주는 프로그램입니다.",
                "웹 브라우저를 열고 아래 Python 공식 다운로드 페이지로 이동하세요.",
                PYTHON_DOWNLOAD_URL,
                "페이지의 Download Python 버튼을 누르고 설치 파일을 실행하세요.",
                "이미 Anaconda를 설치했다면 Python이 함께 설치되어 있을 수 있으므로 다음 단계에서 먼저 확인해도 됩니다.",
            ],
            "브라우저 주소창에 입력:\n\nhttps://www.python.org/downloads/\n\n설치가 끝나면 이 프로그램으로 돌아오세요.",
            "설치가 끝났다는 화면이 보이면 됩니다. Python을 직접 열 필요는 없습니다.",
            "Q. Anaconda가 이미 있는데 Python을 또 설치해야 하나요?\n\nA. 꼭 그렇지는 않습니다. 터미널에서 python이 실행되면 우선 그대로 진행해도 됩니다.",
        ),
        Step(
            "Codex 설치하기",
            [
                "Codex는 프로젝트 폴더의 파일을 읽고 수정하며 실행까지 도와주는 AI 개발 도구입니다.",
                "아래 OpenAI 공식 안내 페이지에서 앱을 설치하세요.",
                CODEX_DOWNLOAD_URL,
                "설치 후 ChatGPT 계정으로 로그인하세요.",
            ],
            "브라우저 주소창에 입력:\n\nhttps://developers.openai.com/codex/app\n\n안내에 따라 앱을 설치하고 로그인하세요.",
            "앱에서 프로젝트 폴더를 선택할 수 있는 화면이 보이면 준비된 것입니다.",
            "Q. Codex가 내 컴퓨터의 모든 파일을 마음대로 바꾸나요?\n\nA. 처음에는 연습용으로 새로 만든 작은 폴더만 프로젝트로 여세요.",
        ),
        Step(
            "터미널 열기",
            ["터미널은 글자로 컴퓨터에게 명령을 내리는 앱입니다."],
            "1. Command(⌘) + Space를 누릅니다.\n2. Terminal 또는 터미널을 검색합니다.\n3. Enter를 누릅니다.",
            "(base) 사용자이름@MacBook:~ $\n\n모양이 조금 달라도 마지막에 $ 또는 %가 보이면 괜찮습니다.",
            "Q. (base)가 보여도 괜찮나요?\n\nA. 괜찮습니다. Anaconda 환경이 켜져 있다는 뜻입니다.",
        ),
        Step(
            "Python 실행 확인",
            ["명령을 입력한 뒤 Enter를 눌러야 실행됩니다."],
            "터미널에 입력:\n\npython\n\n안 되면:\n\npython3",
            "Python 3.x.x ...\n>>>\n\n>>>가 보이면 Python이 정상적으로 실행된 것입니다.",
            "Q. >>>가 나오고 원래 화면으로 돌아가지 않아요.\n\nA. Python 대화형 화면입니다. 다음 단계에서 빠져나옵니다.",
        ),
        Step(
            "Python 화면에서 빠져나오기",
            [">>>가 보이는 화면에서 일반 터미널로 돌아갑니다."],
            ">>> 뒤에 입력:\n\nexit()",
            ">>>가 사라지고 다시 $ 또는 %가 보입니다.",
        ),
        Step(
            "바탕화면으로 이동하기",
            ["cd는 Change Directory의 약자로 폴더를 이동하는 명령입니다."],
            "터미널에 입력:\n\ncd ~/Desktop",
            "성공해도 아무 메시지가 나오지 않을 수 있습니다.",
            "Q. 아무것도 출력되지 않았는데 실패한 건가요?\n\nA. 아닙니다. 터미널 명령은 성공하면 조용한 경우가 많습니다.",
        ),
        Step(
            "프로젝트 폴더 만들기",
            ["mkdir은 Make Directory의 약자로 새 폴더를 만듭니다."],
            "터미널에 입력:\n\nmkdir my-first-python",
            "바탕화면에 my-first-python 폴더가 생깁니다.",
        ),
        Step(
            "프로젝트 폴더로 들어가기",
            ["앞으로 이 폴더 안에서 파일을 만들고 실행합니다."],
            "터미널에 입력:\n\ncd my-first-python",
            "터미널 앞부분에 my-first-python이 보일 수 있습니다.",
            "Q. 이제 폴더 밖으로 나가야 하나요?\n\nA. 아니요. 지금 그대로 있는 것이 맞습니다.",
        ),
        Step(
            "현재 위치 확인하기",
            ["pwd는 현재 위치를 보여줍니다."],
            "터미널에 입력:\n\npwd",
            "/Users/사용자이름/Desktop/my-first-python\n\n사용자 이름은 사람마다 다릅니다.",
        ),
        Step(
            "첫 Python 파일 만들기",
            ["touch는 빈 파일을 만들고, ls는 현재 폴더의 파일을 보여줍니다."],
            "터미널에 차례대로 입력:\n\ntouch main.py\nls",
            "main.py가 보입니다.",
        ),
        Step(
            "파일을 TextEdit으로 열기",
            ["open -e는 macOS에서 파일을 TextEdit으로 여는 명령입니다."],
            "터미널에 입력:\n\nopen -e main.py",
            "TextEdit이 열리고 빈 main.py가 보입니다.",
            "Q. 터미널은 닫아도 되나요?\n\nA. 닫지 않는 편이 좋습니다. 저장 후 같은 터미널에서 실행합니다.",
        ),
        Step(
            "첫 코드 작성하기",
            ["print는 괄호 안의 글자를 화면에 출력합니다."],
            'TextEdit에 입력:\n\nprint("안녕하세요! 첫 번째 파이썬 프로그램입니다.")\n\nCommand(⌘) + S로 저장하세요.',
            "main.py 안에 코드 한 줄이 저장되어 있으면 됩니다.",
        ),
        Step(
            "첫 프로그램 실행하기",
            ["Python에게 main.py를 읽고 실행하라고 명령합니다."],
            "터미널에 입력:\n\npython main.py\n\n안 되면:\n\npython3 main.py",
            "안녕하세요! 첫 번째 파이썬 프로그램입니다.\n\n이 문장이 보이면 성공입니다.",
        ),
        Step(
            "사용자 입력받기",
            ["input은 사용자가 입력한 값을 받아옵니다. name은 그 값을 저장하는 변수입니다."],
            '다시 파일 열기:\n\nopen -e main.py\n\n아래 두 줄로 바꾸고 저장:\n\nname = input("이름을 입력하세요: ")\nprint("안녕하세요!", name)\n\n실행:\n\npython main.py',
            "이름을 입력하세요: 소연\n안녕하세요! 소연",
        ),
        Step(
            "Codex에서 프로젝트 폴더 열기",
            ["Codex 앱에서 프로젝트 추가 또는 폴더 열기를 선택하세요."],
            "바탕화면의 my-first-python 폴더를 선택하세요.",
            "Codex 화면에 my-first-python 프로젝트와 채팅 입력창이 보입니다.",
        ),
        Step(
            "Codex에게 첫 수정 요청하기",
            ["아래 요청은 그대로 복사해도 됩니다. 처음부터 프롬프트를 직접 잘 쓸 필요는 없습니다."],
            """Codex 입력창에 붙여넣기:

나는 파이썬을 배우는 초보자야.

현재 프로젝트의 main.py를 수정해줘.
현재는 이름만 입력받는데 이름과 나이를 입력받도록 바꿔줘.
기존 파일은 삭제하지 말고, 수정 후 직접 실행해서 오류가 없는지 확인해줘.
마지막에는 변경한 코드를 초보자도 이해할 수 있게 설명해줘.""",
            "Codex가 main.py를 수정하고 실행 결과와 설명을 보여줍니다.",
            "Q. 항상 이렇게 길게 써야 하나요?\n\nA. 아닙니다. 익숙해지면 짧게 요청하고 결과를 보며 다시 수정하면 됩니다.",
        ),
    ]


def windows_note() -> None:
    line()
    print("Windows 사용자를 위한 간단 안내")
    print("\n이 첫 버전은 macOS 실습 흐름을 중심으로 작성되었습니다.")
    print("- 터미널: 시작 메뉴에서 PowerShell 검색")
    print("- 바탕화면 이동: cd $HOME\\Desktop")
    print("- 빈 파일 만들기: New-Item main.py")
    print("- 파일 열기: 메모장 또는 VS Code")


def next_project() -> None:
    line()
    print("🎮 다음 프로젝트: 숫자 맞추기 게임")
    print("\nCodex에 아래처럼 요청해보세요.")
    small_line()
    print("""현재 프로젝트에 number_game.py 파일을 새로 만들어줘.

1부터 100 사이의 숫자를 맞추는 게임을 만들어줘.
정답보다 작으면 더 큰 숫자라고 알려주고,
정답보다 크면 더 작은 숫자라고 알려줘.
정답을 맞히면 축하 메시지를 출력하고 종료해줘.
초보자가 이해하기 쉽게 작성하고 직접 테스트해줘.""")
    small_line()


def main() -> None:
    show_intro()
    if not yes_no("macOS를 사용하고 있나요?"):
        windows_note()
        return
    if not yes_no("튜토리얼을 시작할까요?"):
        print("\n준비됐을 때 다시 실행해주세요.")
        return
    for number, step in enumerate(mac_steps(), start=1):
        show_step(number, step)
    next_project()
    line()
    print("🎉 첫 번째 바이브코딩 입문 과정을 완료했습니다.")
    print("\n처음부터 모든 코드를 이해할 필요는 없습니다.")
    print("원하는 기능을 말하고, 결과를 실행하고, 불편한 점을 다시 요청하면 됩니다.")


if __name__ == "__main__":
    main()
