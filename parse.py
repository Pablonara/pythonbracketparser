import argparse
import code
import readline
import io
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--interactive", help="Interactive Mode (like how running python3 gives you a shell)")
args = parser.parse_args()

def process(code):
    lines = code.split('\n')
    converted = []
    indentLevel = 0
    indentSize = 4
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Split the line by semicolons first
        segments = line.split(';')
        for segment in segments:
            segment = segment.strip()
            if not segment:
                continue
            
            while '{' in segment or '}' in segment:
                if '{' in segment:
                    before, after = segment.split('{', 1)
                    converted.append(' ' * (indentLevel * indentSize) + before.strip() + ':')
                    indentLevel += 1
                    segment = after.strip()
                elif '}' in segment:
                    before, after = segment.split('}', 1)
                    converted.append(' ' * (indentLevel * indentSize) + before.strip())
                    indentLevel -= 1
                    segment = after.strip()
            
            # Append the processed segment with proper indentation
            if segment:
                converted.append(' ' * (indentLevel * indentSize) + segment)
        
        # Add a blank line after processing each line if it ends with a semicolon
        if line.endswith(';'):
            converted.append('')
    
    return '\n'.join(converted)

# Test case
testCase = """
a = {"key": ["a", "b", "c"]};
print(a); print(b);
if a {print("hello")}
def helloWorld() {print("Hello World!")};
print("Arch user btw uwu"); for i in range(5) {print(i)}
"""
# if args.interactive == 'y':
#     console = code.InteractiveConsole()
#     buffer = []
#     while True:
#         a = input("> ")
#         processed = a
#         print("processed: ")
#         print(processed)
#         output = io.StringIO()
#         lines = processed.split('\n')
#         for line in lines:
#             buffer.append(line)
#             code = '\n'.join(buffer)
#             sys.stdout = output
#             sys.stderr = output
#             more = console.push(code)
#             sys.stdout = sys.__stdout__
#             sys.stderr = sys.__stderr__
#             if not more: 
#                 buffer = []
#                 print(output.getvalue)
#             else:
#                 pass
#         if not more:
#             print(output.getvalue())

if args.interactive == 'y':
    console = code.InteractiveConsole()
    
    while True:
        try:
            uinput = input('~> ')
            if uinput.strip() == 'exit()':
                print("Exiting interactive console.")
                break
            processed = process(uinput)
            # this works and I have no idea why
            oldOut = sys.stdout
            oldErr = sys.stderr
            newOut = io.StringIO()
            newErr = io.StringIO()
            sys.stdout = newOut
            sys.stderr = newErr
            
            try:
                console.push(processed)
            finally:
                # Restore original stdout and stderr
                sys.stdout = oldOut
                sys.stderr = oldErr

            output = newOut.getvalue()
            error = newErr.getvalue()

            if output:
                print(output, end='')
            if error:
                print(error, end='')
        except (EOFError, KeyboardInterrupt):
            print("\nExiting interactive console.")
            break
        except Exception as e:
            print(f"Error: {e}")
else:

    converted = process(testCase)
    print(converted)
