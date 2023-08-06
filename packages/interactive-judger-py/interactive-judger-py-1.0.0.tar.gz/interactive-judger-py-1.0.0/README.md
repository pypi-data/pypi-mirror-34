# Interactive Judger for Python3
[![Build Status](https://travis-ci.org/AD1024/InteractiveJudgerPy.svg?branch=master)](https://travis-ci.org/AD1024/InteractiveJudgerPy)

This project was initially being used to help me with the Python course I taught at Algorithm 101, CSE. I modified it to a more friendly version during my spare time.

# Functions
- [x] Safe Data Loading
- [x] Automatic Testing
- [x] TLE Testing
- [x] User Custom Data Directory
- [ ] MLE Testing
- [ ] Time Measuring

# Usage
### Step 1
Use `conf_generator.py` generate judger config by following the instructions.

### Step 2
Save your test cases(parameters for method being tested) in a file and place it into `data` folder. Copy python files you want to test into `src` folder, and finally, copy your answers(corresponding with the test case) into a file and move it into `data` folder.

### Step 3
Run `judge.py` and follow the instructions.