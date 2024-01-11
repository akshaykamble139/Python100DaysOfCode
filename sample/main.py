with open("es_50k.txt") as file:
    content = file.readlines()
    new_content = ""
    for line in content:
        new_content += line.split()[0] + "\n"

    with open("words.txt", "w") as new_file:
        new_file.write(new_content)