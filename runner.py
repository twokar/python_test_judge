#!/usr/bin/env python3
import subprocess
import time
import sys

def compile_cpp(source_file, executable_file):
    """编译 C++ 源码到可执行文件，失败则打印 CE 并退出。"""
    compile_cmd = ["g++", "-O2", "-std=c++17", "-o", executable_file, source_file]
    try:
        subprocess.run(compile_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        # Compilation Error
        print("CE")
        sys.exit(0)

def run_and_check(executable_file, expected_output):
    """运行可执行文件并检查输出，失败或输出不符打印相应结果。"""
    try:
        start_time = time.time()
        result = subprocess.run([executable_file], check=True, capture_output=True, text=True)
        exec_time = time.time()-start_time
    except subprocess.CalledProcessError:
        # Runtime Error
        print("CE")
        sys.exit(0)

    # 去除行尾换行，严格比对
    output = result.stdout.strip()
    if output == expected_output:
        print("Accepted")
    else:
        print("Wrong Answer")
    print("{:.6f}".format(exec_time))

def main():
    source_file     = "/home/src/main.cpp"
    executable_file = "/home/src/app"
    expected_output = "Hello, GitHub!"

    # 1. 编译
    compile_cpp(source_file, executable_file)

    # 2. 运行并检查
    run_and_check(executable_file, expected_output)

if __name__ == "__main__":
    main()
