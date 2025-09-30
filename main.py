import os
import importlib
import argparse


def main(step, use_case, end_user, purchaser, base_year, geo):
    fn = f'prompts.step_{str(step).zfill(2)}'
    step = importlib.import_module(fn)
    prompt = step.step['step']
    prompt += '\n\nGoal: ' + step.step['goal']
    prompt += '\n\nPrompt:' + step.step['prompt']

    prompt = prompt.format(SEGMENT=use_case, END_USER=end_user, PURCHASER=purchaser, GEO=geo, BASE_YEAR=base_year)
    prompt = prompt.replace('\n    ', '\n').lstrip()
    return prompt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_case', type=str, default='residential decking')
    parser.add_argument('--end_user', type=str, default='homeowners')
    parser.add_argument('--purchaser', type=str, default='homeowners')
    parser.add_argument('--base_year', type=int, default=2025)
    parser.add_argument('--geo', type=str, default='United States')
    args = parser.parse_args()
    
    os.makedirs('output_prompts', exist_ok=True)
    for step in range(0, 11):
        filled_prompt = main(step, args.use_case, args.end_user, args.purchaser, args.base_year, args.geo)
        with open(f'output_prompts/step_{str(step).zfill(2)}.txt', 'w') as f:
            f.write(filled_prompt)