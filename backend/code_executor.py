import subprocess
import threading

class CodeExecutor:
    def __init__(self):
        self.output = None
        self.error = None

    def run(self, code):
        thread = threading.Thread(target=self.execute_code, args=(code,))
        thread.start()  # Start the thread to run the code
        thread.join()  # Wait for the thread to complete

    def execute_code(self, code):
        try:
            # Use subprocess to execute the code
            process = subprocess.Popen(['python3', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.output, self.error = process.communicate()
        except Exception as e:
            self.error = str(e)

    def get_output(self):
        return self.output.decode('utf-8') if self.output else None

    def get_error(self):
        return self.error.decode('utf-8') if self.error else None

# Example usage:
# executor = CodeExecutor()
# executor.run("print('Hello, World!')")
# print('Output:', executor.get_output())
# print('Error:', executor.get_error())