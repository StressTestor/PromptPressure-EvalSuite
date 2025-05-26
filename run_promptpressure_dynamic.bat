@echo off
pushd "%~dp0"
echo Running PromptPressure Eval Suite from: %cd%
python run_eval.py --config config.yaml
pause
