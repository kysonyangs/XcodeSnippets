import os
import re

code_snippet =  "CodeSnippets"
current_path = os.getcwd()
current_codesnippet_path = os.path.join(current_path, code_snippet)
f_list = os.listdir(current_codesnippet_path)

for file in f_list:
    path = os.path.join(current_codesnippet_path, file)
    src = open(path, 'r+')
    content = src.read().strip()

    pattern = re.compile("<key>IDECodeSnippetTitle</key>.*?<string>(.*?)</string>", re.S)
    items = re.findall(pattern, content)

    if len(items) > 0:
        print(items[0])
        name = items[0].strip() + ".codesnippet"
        old_name = path
        new_name = os.path.join(current_codesnippet_path, name)
        os.rename(old_name, new_name)

        print(name + " --- " + file)
        if name != file:
            print(old_name + "\n重命名\n"+ new_name)
