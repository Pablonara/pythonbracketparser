import argparse
import code
import readline

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
if args.interactive == 'y':
    console = code.InteractiveConsole()
    while True:
        a = input("> ")
        processed = process(a)
        print(processed)
        for line in processed.split('\n'):
            console.push(line)

converted = process(testCase)
print(converted)
