from google.adk.agents import Agent

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b



root_agent = Agent(
    name="math_agent",
    model="gemini-2.5-flash",
    instruction="""4칙 연산 도구를 사용해서 사용자가 요청한 수식을 계산하고, 결과를 답하세요.""",
    tools=[add, subtract, multiply, divide],
)
