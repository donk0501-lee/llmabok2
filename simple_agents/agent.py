from .lambda_agent import LambdaAgent
from .json_input_agent import JsonInputAgent
from .while_agent import WhileAgent
from google.adk.agents import SequentialAgent


def update_fib_pair(fib_pair):
    if fib_pair is None:
        return (0, 1)
    a, b = fib_pair
    return (b, a + b)

fib_pair_update_agent = LambdaAgent(name="fib_update_agent",
                         func=update_fib_pair,
                         input_keys=["fib_pair"],
                         output_key="fib_pair")

init_num_iter_agent = LambdaAgent(name="init_num_iter_agent",
                            func=lambda: 0,
                            input_keys=[],
                            output_key="num_iter")

incr_num_iter_agent = LambdaAgent(name="incr_num_iter_agent",
                         func=lambda x: 0 if x is None else x + 1,
                         input_keys=["num_iter"],
                         output_key="num_iter")

fib_while_agent = WhileAgent(
    name="FibonacciWhileAgent",
    description="An agent that generates Fibonacci numbers until the first number exceeds 100.",
    condition="num_iter <= n",
    sub_agents=[fib_pair_update_agent, incr_num_iter_agent],
)

json_input_agent = JsonInputAgent(name="FibonacciInputAgent")

root_agent = SequentialAgent(name="FibonacciAgent",
                                description="An agent that generates Fibonacci numbers up to the n-th number.",
                                sub_agents=[json_input_agent, init_num_iter_agent,
                                            fib_while_agent])

