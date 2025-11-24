from google.adk.agents import Agent
from google.adk.tools import exit_loop

GEMINI_MODEL = "gemini-2.5-flash"

initial_writer_agent = Agent(
    name="InitialWriterAgent",
    model=GEMINI_MODEL,
    instruction="""당신은 창의적인 글쓰기 도우미입니다. 요청에 맞는 짧은 이야기(2~4 문장)를 작성하세요.""",
    output_key="story",
)

critic_agent = Agent(
    name="CriticAgent",
    model=GEMINI_MODEL,
    instruction="""당신은 짧은 이야기 초안을 검토하는 건설적인 비평가입니다.
다음 이야기를 검토하고, 개선할 수 있는 명확하고 실행 가능한 방법이 있다면
그에 대한 구체적인 제안을 제공하세요.
**검토할 이야기:**
```
{story}
```
**작업 가이드:**
문서의 명확성, 몰입도 및 기본적인 일관성을 검토합니다.
독자의 몰입도를 높이기 위한 명확한 방안이 있으면 1-2가지 제안하세요.
예: "더 강력한 도입 문장이 필요하다", "캐릭터의 목표를 명확히 하라".
구체적이고 간결한 제안을 제공하세요.
더 이상 수정할 사항이 없다면 *정확히* "No major issues found."라는 문구를
정확히 출력하세요.
비평 내용만 출력하고 추가 설명은 하지 마세요.
""",
    output_key="criticism",
)

refiner_agent = Agent(
    name="RefinerAgent",
    model=GEMINI_MODEL,
    instruction="""당신은 피드백을 기반으로 이야기를 다듬거나 프로세스를 종료하는
창의적인 글쓰기 도우미입니다.
**이야기:**
{story}
**비평/제안:****작업 가이드:**
'비평/제안'을 분석합니다. 비평이 *정확히* "No major issues found."라면,
'exit_loop' 함수를 호출하세요. 이 경우 추가 텍스트를 출력하지 마세요.
그렇지 않으면, 비평에서 제안된 개선 사항을 신중하게 적용하여 이야기를 개선하세요.
개선된 문서만 출력하고, 'exit_loop' 함수를 호출하지 마세요.
""",
    output_key="story",
    tools=[exit_loop],
)
