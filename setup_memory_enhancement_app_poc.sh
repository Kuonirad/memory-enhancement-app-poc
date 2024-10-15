#!/bin/bash

# =============================================================================
# Script Name: setup_memory_enhancement_app_poc.sh
# Description: Automates the setup, dependency installation, testing, and
#              version control steps for the memory-enhancement-app-poc project.
# =============================================================================

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display messages
function echo_info {
    echo -e "\e[34m[INFO]\e[0m $1"
}

function echo_success {
    echo -e "\e[32m[SUCCESS]\e[0m $1"
}

function echo_error {
    echo -e "\e[31m[ERROR]\e[0m $1"
    exit 1
}

# =============================================================================
# Step 1: Navigate to Project Directory
# =============================================================================
echo_info "Navigating to project directory..."
cd ~/memory-enhancement-app-poc || echo_error "Project directory not found."

# =============================================================================
# Step 2: Activate Virtual Environment
# =============================================================================
echo_info "Activating virtual environment..."
if [ -d "venv" ]; then
    source venv/bin/activate
    echo_success "Virtual environment activated."
else
    echo_error "Virtual environment 'venv' does not exist. Please create it using 'python3 -m venv venv'."
fi

# =============================================================================
# Step 3: Install Required Dependencies
# =============================================================================
echo_info "Installing required dependencies: qiskit, qiskit-aer, numpy..."
pip install --upgrade pip
pip install qiskit qiskit-aer numpy
echo_success "Dependencies installed successfully."

# =============================================================================
# Step 4: Re-run Qiskit Functionality Test
# =============================================================================
echo_info "Running Qiskit functionality test..."
if [ -f "simple_qiskit_test.py" ]; then
    python simple_qiskit_test.py
    echo_success "Qiskit functionality test completed."
else
    echo_error "'simple_qiskit_test.py' not found."
fi

# =============================================================================
# Step 5: Re-run Quantum-Inspired Optimization Tests
# =============================================================================
echo_info "Running quantum-inspired optimization tests..."
TEST_SCRIPT="src/enhancements/quantum_inspired_optimization/test_quantum_inspired_optimization.py"
if [ -f "$TEST_SCRIPT" ]; then
    python "$TEST_SCRIPT"
    echo_success "Quantum-inspired optimization tests passed."
else
    echo_error "Test script '$TEST_SCRIPT' not found."
fi

# =============================================================================
# Step 6: Check Git Status
# =============================================================================
echo_info "Checking git status..."
git status

# =============================================================================
# Step 7: Review Untracked Files
# =============================================================================
echo_info "Listing untracked Python test files..."
ls -l check_*.py qiskit_*.py simple_qiskit_test.py 2>/dev/null || echo "No matching untracked files found."

# =============================================================================
# Step 8: Update .gitignore
# =============================================================================
echo_info "Updating .gitignore to exclude virtual environment and Python cache files..."
{
    echo ""
    echo "# Virtual environment"
    echo "venv/"
    echo ""
    echo "# Python cache files"
    echo "__pycache__/"
    echo "*.pyc"
} >> .gitignore
echo_success ".gitignore updated."

# =============================================================================
# Step 9: Stage Necessary Files
# =============================================================================
echo_info "Staging updated .gitignore and new test files..."
git add .gitignore simple_qiskit_test.py qiskit_aer_direct_test.py
echo_success "Files staged successfully."

# =============================================================================
# Step 10: Final Git Status Check
# =============================================================================
echo_info "Final git status after staging:"
git status
echo_success "Setup and testing process completed successfully."
