import re

# 定义函数来统计出现次数
def count_occurrences(file_path, names_file, pronouns):
    name_count = 0
    pronoun_count = 0

    # 从 names 文件中读取人名
    with open(names_file, 'r') as file:
        names = [line.strip() for line in file.readlines()]

    # 读取主文件并统计出现次数
    with open(file_path, 'r') as file:
        for line in file:
            line = line.lower()  # 将行转换为小写以进行不区分大小写的匹配
            line_name_count = set()
            line_pronoun_count = set()

            for name in names:
                if re.search(r'\b' + re.escape(name.lower()) + r'\b', line):
                    line_name_count.add(name)

            for pronoun in pronouns:
                if re.search(r'\b' + re.escape(pronoun.lower()) + r'\b', line):
                    line_pronoun_count.add(pronoun)

            if(len(line_name_count)!=0): name_count = name_count + 1
            if(len(line_pronoun_count)!=0): pronoun_count = pronoun_count + 1

    return name_count, pronoun_count


# 定义要统计的代词
pronouns = ["herself", "hers", "her", "she"]

# 统计文件中的出现次数
name_count, pronoun_count = count_occurrences('female_1.txt', 'female_name.txt', pronouns)

# 打印结果
print(f"Total occurrences of names: {name_count}")
print(f"Total occurrences of pronouns (aerself, aers, aer, ae): {pronoun_count}")
