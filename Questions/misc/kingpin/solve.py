import subprocess
import time
from tqdm import tqdm

def run_binary(binary_path, input_data):
    start_time = time.perf_counter()
    
    # Run the binary and send input
    process = subprocess.Popen(binary_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate(input_data.encode())
    
    end_time = time.perf_counter()
    
    execution_time = (end_time - start_time) * 1000  # in milliseconds
    print(execution_time)
    return output.decode(), execution_time

def guess_pin(binary_path):
    pin_length = 10
    pin = ['0'] * pin_length
    max_execution_times = []
    
    for i in range(pin_length):
        max_avg_execution_time = 0
        max_digit = None
        
        for digit in tqdm(range(10), desc="Guessing digit {}".format(i)):
            total_execution_time = 0
            for _ in range(10):  # Run the binary 10 times for each digit guess
                pin[i] = str(digit)
                input_data = ''.join(pin) + "\n"
                _, execution_time = run_binary(binary_path, input_data)
                total_execution_time += execution_time
            
            avg_execution_time = total_execution_time / 10
            if avg_execution_time > max_avg_execution_time:
                max_avg_execution_time = avg_execution_time
                max_digit = digit
        
        max_execution_times.append(max_avg_execution_time)
        pin[i] = str(max_digit)
        print("Found digit:", max_digit, "at position", i)
        print("Current pin:", ''.join(pin))
        print("Average execution time for digit {}: {:.3f} milliseconds\n".format(i, max_avg_execution_time))
    
    max_pin = ''.join(pin)
    max_avg_execution_time = max(max_execution_times)
    print("Final pin:", max_pin)
    print("Maximum average execution time:", max_avg_execution_time)

if __name__ == "__main__":
    binary_path = "./kingpin"  # Replace with your binary's path
    
    guess_pin(binary_path)
