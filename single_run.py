# PR marked
from human_eval.data import write_jsonl, stream_jsonl

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

def single_run(problem_number, model):
    problems = stream_jsonl('human_eval/data/HumanEval.jsonl.gz')
    print(problems[0])


    print('your mom has ' + str(problem_number) + ' problems, but' + model + ' ain\'t one')
    pass

single_run(1, "gpt2")