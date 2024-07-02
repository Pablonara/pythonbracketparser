def process(code):
    lines = code.split('\n')
    converted = []
    indentLevel = 0
    indentSize = 4
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        while '{' in line or '}' in line:
            if '{' in line:
                before, after = line.split('{', 1)
                converted.append(' ' * (indentLevel * indentSize) + before.strip() + ':')
                indentLevel += 1
                line = after.strip()
            elif '}' in line:
                before, after = line.split('}', 1)
                converted.append(' ' * (indentLevel * indentSize) + before.strip())
                indentLevel -= 1
                line = after.strip()
        
        if line:
            converted.append(' ' * (indentLevel * indentSize) + line)
    return '\n'.join(converted)

# Test case
testcase = """
def helloworld() {print("Hello World!")}
"""

converted = process(testcase)
print(converted)
