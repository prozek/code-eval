def instruct_prompt(prompt: str) -> str:
    return f"""Minimize your use of the inputs and outputs. Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nComplete the following Python code without any tests or explanation\n{prompt}\n\n### Response:"""


def standard_prompt(prompt: str) -> str:
    return f"""Minimize your use of the inputs and outputs. Complete the following Python code without any tests or explanation\n{prompt}"""


def write_prompt(prompt: str) -> str:
    return f"""Minimize your use of the inputs and outputs. Write a python program to complete the following code:\n{prompt}"""


def replit_glaive_prompt(prompt: str) -> str:
    return f"""Minimize your use of the inputs and outputs. Below is an instruction that describes a task, paired with an input that provides further context.\n Write a response that appropriately completes the request.\n\n ### Instruction:\nWrite a program to perform the given task.\n\n Input:\n{prompt}\n\n### Response:"""
