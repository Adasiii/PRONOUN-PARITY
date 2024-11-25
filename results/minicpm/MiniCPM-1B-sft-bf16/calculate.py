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
        content = file.read().lower()  # 将内容转换为小写以进行不区分大小写的匹配
        for name in names:
            name_count += len(re.findall(r'\b' + re.escape(name.lower()) + r'\b', content))
        for pronoun in pronouns:
            pronoun_count += len(re.findall(r'\b' + re.escape(pronoun.lower()) + r'\b', content))

    return name_count, pronoun_count


# 定义要统计的代词
pronouns = ["aerself", "aers", "aer", "ae"]

# 统计文件中的出现次数
name_count, pronoun_count = count_occurrences('ae_responses.txt', 'unisex.txt', pronouns)

# 打印结果
print(f"Total occurrences of names: {name_count}")
print(f"Total occurrences of pronouns (emself, ems, e's, e, em, es): {pronoun_count}")
