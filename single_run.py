# PR marked
from human_eval.data import write_jsonl, stream_jsonl

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import jsonlines 

def single_run(problem_number, model):
    
    problems = []

    with jsonlines.open('human-eval/data/HumanEval.jsonl') as reader:
        for obj in reader:
            problems.append(obj)

    print(len(problems))
    print(problems[0].keys())

    for key in problems[problem_number].keys():
        print(key)
        print(problems[problem_number][key])
        print('\n ========== MARKER ========== \n')


    #print('your mom has ' + str(problem_number) + ' problems, but' + model + ' ain\'t one')
    pass

single_run(1, "gpt2")
