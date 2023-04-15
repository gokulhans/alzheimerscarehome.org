with open("sample.txt", "r") as f:
    lines = f.readlines()

with open("output.txt", "w") as f:
    for line in lines:
        word = line.split("=")[0].strip()
        output = f'id = "{word}"\n'
        f.write(output)
