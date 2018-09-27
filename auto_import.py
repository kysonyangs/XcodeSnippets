import os
import shutil

target_path = os.path.expanduser("~/Library/Developer/Xcode/UserData/")
code_snippet =  "CodeSnippets"

target_path_ = os.path.join(target_path, code_snippet)
if not os.path.exists(target_path_):
    os.makedirs(target_path_)

current_path = os.getcwd()
current_codesnippet_path = os.path.join(current_path, code_snippet)
f_list = os.listdir(current_codesnippet_path)

for file in f_list:
    old_path = os.path.join(current_codesnippet_path, file)
    new_path = os.path.join(target_path_, file)
    if not os.path.exists(new_path):
        shutil.copyfile(old_path, new_path)
        print(old_path + "\n复制到\n"+ new_path)



