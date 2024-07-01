#!/bin/bash

CONDA_ENV="ExpenseTracker"
# Check if the OS is Windows or Linux
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Activate Conda environment on Windows
    source activate "$CONDA_ENV"
else
    # Activate Conda environment on Linux
    conda activate "$CONDA_ENV"
fi

# Execute the command to run streamlit
streamlit run UI.py
