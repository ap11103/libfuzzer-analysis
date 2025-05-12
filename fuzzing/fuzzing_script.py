import os
import subprocess
import time
import shutil


#compiled C program 
program_name = 'program'
#a directory for seed inputs
corpus_dir = 'corpus_dir'
#after the fuzzing process, a .profraw file will be generated
coverage_raw_file = 'coverage_data.profraw'
#after processing to .profdata
coverage_data_file = 'coverage_data.profdata'

#compile the program will fuzzer
def compile_program():
    print("Compiling the program with libFuzzer and sanitizers...")
    compile_command = [
        'clang++', 
        '-fsanitize=address,undefined', 
        '-fsanitize-coverage=trace-pc-guard', 
        '-g', '-O1', '-fno-omit-frame-pointer', 
        '-o', program_name, 'fuzzing/program.c', '-lFuzzer'
    ]
    subprocess.run(compile_command, check=True)
    print("Compilation complete.")

#run the fuzzer
def run_fuzzer():
    print("Running libFuzzer...")
    fuzz_command = [
        f'./{program_name}', corpus_dir, '-max_len=2048', '-runs=100000'
    ]
    subprocess.run(fuzz_command, check=True)
    print("Fuzzing completed.")

#using llvm to convert to profdata
def convert_profraw_to_profdata():
    print("Converting .profraw to .profdata...")
    llvm_profdata_command = [
        'llvm-profdata', 'merge', '-sparse', coverage_raw_file, '-o', coverage_data_file
    ]
    subprocess.run(llvm_profdata_command, check=True)
    print(f"Coverage data saved to {coverage_data_file}")

#need to cleanup the files
def clean_up():
    print("Cleaning up generated files...")
    if os.path.exists(program_name):
        os.remove(program_name)
    if os.path.exists(coverage_raw_file):
        os.remove(coverage_raw_file)
    print("Clean up completed.")

#main
def collect_coverage_data():
    try:
        #create corpus_dir, if it doesn't exists already
        if not os.path.exists(corpus_dir):
            os.makedirs(corpus_dir)
            print(f"Created corpus directory: {corpus_dir}")
        
        #compile
        compile_program()

        #run fuzzer
        run_fuzzer()

        #convert data
        convert_profraw_to_profdata()

    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")
    finally:
        #if exists, clean up all the unncessary files
        clean_up()

if __name__ == '__main__':
    collect_coverage_data()
