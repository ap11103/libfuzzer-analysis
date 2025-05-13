# LibFuzzer Crash Clustering, Coverage Visualization, and Mutation Analysis

This project enhances **libFuzzer** by integrating tools for visualizing coverage data, tracking input mutations, and clustering crashes. The goal is to analyze and understand the relationship between different mutations and the resulting crashes during fuzz testing, helping developers optimize fuzzing strategies.

## Features:
- **Coverage Visualization**: Visualize which parts of the code were exercised during fuzzing using a heatmap.
- **Mutation Analysis**: Track how different input mutations lead to crashes and represent these relationships in a directed graph.
- **Crash Clustering**: Use KMeans clustering to group similar crashes based on features such as stack trace hash and memory address.

## Prerequisites:
- **clang** with **libFuzzer** support for compiling C/C++ programs.
- **LLVM tools** (`llvm-profdata`, `llvm-cov`) for processing coverage data.
- **Python** and various libraries for analysis and visualization.

### **Installation Instructions**:

1. **Install LLVM and libFuzzer**:
   - On Ubuntu-based systems:
     ```bash
     sudo apt-get update
     sudo apt-get install clang llvm llvm-profdata llvm-cov
     ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/libfuzzer-analysis.git
   cd libfuzzer-analysis

3. **Set up Python dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Build the C program with libFuzzer**:
    (this approach wasn't reliable)
     -  Build as C++
    You need to link against LibFuzzer, and you should ensure the C++ standard library is linked as well. Since LibFuzzer is part of LLVM's C++ tools, it requires a C++ compilation environment even if your code is in C.
    [
    clang++ -fsanitize=address,undefined -fsanitize-coverage=trace-pc-guard -g -O1 -fno-omit-frame-pointer -o program program.c -lFuzzer]
   
    ```bash
    clang++ -fsanitize=address,undefined -fsanitize-coverage=trace-pc-guard -g -O1 -fno-omit-frame-pointer -o program program.cpp -lFuzzer -lstdc++



5. **Run the Fuzzer**
    ```bash
    ./program -max_len=2048 -runs=100000 -seed=12345

6. **Convert .profraw to .profdata**
    ```bash
    llvm-profdata merge -sparse coverage_data.profraw -o coverage_data.profdata

7. **Run the python script**
    ```bash
    python3 fuzzing_script.py


## **Main Files**:
- program.c: The C program that is fuzzed with libFuzzer
- fuzzing_script.py: Python script that orchestrates fuzzing, coverage data collection, and visualization
- coverage_visualization: Python script for visualizing the code coverage during fuzzing by generating heatmaps
- mutation_analysis: Python script for visualizing and analyzing mutations and their relation to crashes
- crash_clustering: Python script to perform KMeans clustering on crash data



## **Visualization**:
- Mutation Analysis: Visualize the relationship between input mutations and their resulting crashes.
- Crash Clustering: Visualize the distribution of crashes and group them based on their features (stack trace, memory address, etc.).
- Coverage Visualization: Heatmap of code coverage during fuzzing to show which parts of the code were tested.


## **Troubleshooting**:
If you encounter issues during fuzzing or visualization process; 
- The LLVM tools are properly installed and available in yout PATH. 
- The program.c is compiled correctly with libFuzzer enabled. 
- The .profraw file is correctly generated after fuzzing and avalaible for processing. 


