import os
import shutil

target_path = os.path.expanduser("~/Library/Developer/Xcode/UserData/")
code_snippet =  "CodeSnippets"

choice = input('请输入是否覆盖同名文件：0.不覆盖 1.覆盖\n').strip()

target_path_ = os.path.join(target_path, code_snippet)
if not os.path.exists(target_path_):
    print("Xcode 下没有 CodeSnippets 目录")
    exit()

current_path = os.getcwd()
current_codesnippet_path = os.path.join(current_path, code_snippet)

f_list = os.listdir(target_path_)

for file in f_list:
    new_path = os.path.join(current_codesnippet_path, file)
    old_path = os.path.join(target_path_, file)
    if not os.path.exists(new_path):
        shutil.copyfile(old_path, new_path)
        print(old_path + "\n复制到\n"+ new_path)


exit()
