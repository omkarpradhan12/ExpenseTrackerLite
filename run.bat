@echo off

set CONDA_ENV=ExpenseTracker

:: Check if the OS is Windows
if "%OS%"=="Windows_NT" (
    :: Activate Conda environment on Windows
    call activate %CONDA_ENV%
) else (
    :: Activate Conda environment on Linux
    conda activate %CONDA_ENV%
)

:: Execute the command to run streamlit
streamlit run UI.py
