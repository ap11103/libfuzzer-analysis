import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt

#if in case, the .profraw files and .prodata files are not accessibile
#converting .profraw to .profdata using llvm-profdata
def convert_profraw_to_profdata():
    coverage_raw_file = "coverage_data.profraw"
    coverage_data_file = "coverage_data.profdata"
    
    #check if .profraw file exists
    if not os.path.exists(coverage_raw_file):
        print(f"Error: {coverage_raw_file} does not exist!")
        return None
    
    #run llvm-profdata to merge the .profraw file into a .profdata file
    llvm_profdata_command = [
        "llvm-profdata", "merge", "-sparse", coverage_raw_file, "-o", coverage_data_file
    ]
    subprocess.run(llvm_profdata_command, check=True)
    print(f"Coverage data saved to {coverage_data_file}")
    return coverage_data_file

#parse .profdata to extract coverage data for visualization
def parse_coverage_data(coverage_data_file):
    if not os.path.exists(coverage_data_file):
        print(f"Error: {coverage_data_file} does not exist!")
        return None
    
    #use llvm-cov to extract the raw coverage information from the .profdata file
    llvm_cov_command = [
        "llvm-cov", "show", "-instr-profile", coverage_data_file, "--format=csv"
    ]
    
    result = subprocess.run(llvm_cov_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error during coverage data extraction: {result.stderr}")
        return None
    
    #parsing the output into a 2D numpy array (assuming CSV format)
    lines = result.stdout.splitlines()
    coverage_data = []
    
    for line in lines[1:]:
        coverage_data.append([float(x) for x in line.split(',')[1:]])  # Assuming coverage data starts from second column
    
    coverage_data = np.array(coverage_data)
    return coverage_data

#visualize the coverage data using a heatmap
def visualize_coverage(coverage_data):
    if coverage_data is None:
        print("Error: No coverage data to visualize!")
        return
    
    plt.figure(figsize=(8, 6))
    plt.imshow(coverage_data, cmap='hot', interpolation='nearest')
    plt.colorbar(label="Coverage Level")
    plt.title("Fuzzing Coverage Heatmap")
    plt.xlabel("Code Unit")
    plt.ylabel("Code Unit")
    plt.show()

def main():
    #conver, parse, and visualize
    coverage_data_file = convert_profraw_to_profdata()    
    if coverage_data_file:
        coverage_data = parse_coverage_data(coverage_data_file)
        visualize_coverage(coverage_data)

if __name__ == "__main__":
    main()
