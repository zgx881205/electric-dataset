import numpy as np
# # 读取包含用空格分隔的数据的文件
# with open('ratings.txt', 'r') as file:
#     lines = file.readlines()
#
# # 将数据转换为使用制表符分隔的格式
# tab_delimited_lines = [line.strip().replace(' ', '\t') for line in lines]
#
# # 将转换后的数据写入到新文件中
# with open('ratings_final.txt', 'w') as file:
#     file.write('\n'.join(tab_delimited_lines))
# txt转csv
# import pandas as pd
#
# # 读取TXT文件
# df = pd.read_csv("ratings_final.txt", delimiter="\t")  # 假设文件使用制表符作为分隔符
#
# # 将数据写入CSV文件
# df.to_csv("ratings.csv", index=False)
# 初始化计数器
# count_1 = 0
# count_2 = 0
# count_3 = 0
# count_4 = 0
# count_5 = 0
# with open('ratings_final.txt', 'r') as file:
#     # 逐行读取文件内容
#     for line in file:
#         # 切分每行内容为三列
#         columns = line.split()
#         # 获取第三列的值，并转换为整数类型
#         value = int(columns[2])
#         # 根据第三列的值增加相应的计数器
#         if value == 1:
#             count_1 += 1
#         elif value == 2:
#             count_2 += 1
#         elif value == 3:
#             count_3 += 1
#         elif value == 4:
#             count_4 += 1
#         elif value == 5:
#             count_5 += 1
#
# # 打印统计结果
# print("Number of rows with third column value 1:", count_1)
# print("Number of rows with third column value 2:", count_2)
# print("Number of rows with third column value 3:", count_3)
# print("Number of rows with third column value 4:", count_4)
# print("Number of rows with third column value 5:", count_5)
# # 定义阈值
THRESHOLD = 3

# 初始化存储正向和负向评分的字典
user_pos_ratings = {}
user_neg_ratings = {}

# 打开文件并逐行读取数据
with open('ratings.txt', 'r') as file:
    for line in file:
        # 分割每一行数据
        user, item, rating = line.strip().split(' ')

        # 将评分转换为整数
        rating = int(rating)

        # 根据评分判断是正向还是负向评分，并将其添加到相应的字典中
        if rating >= THRESHOLD:
            if user not in user_pos_ratings:
                user_pos_ratings[user] = set()
            user_pos_ratings[user].add(item)
        else:
            if user not in user_neg_ratings:
                user_neg_ratings[user] = set()
            user_neg_ratings[user].add(item)
#
# # 计算正向评分和负向评分的数据量
# num_pos_ratings = sum(len(items) for items in user_pos_ratings.values())
# num_neg_ratings = sum(len(items) for items in user_neg_ratings.values())
#
# # 输出结果
# print("正向评分数据量：", num_pos_ratings)
# print("负向评分数据量：", num_neg_ratings)
# print("正向评分：", user_pos_ratings)
# print("负向评分：", user_neg_ratings)
import random

import random

# 定义文件名
# output_file = "user_ratings.txt"
#
# # 打开文件以写入模式
# with open(output_file, 'w') as file:
#     # 遍历正向评分字典
#     for user, pos_items in user_pos_ratings.items():
#         # 写入用户正向评分的项目，并标记为1
#         for item in pos_items:
#             file.write(f"{user}\t{item}\t1\n")  # 1 表示正向评分
#
#         # 获取用户负向评分的项目（与正向评分不重复）
#         neg_items = user_neg_ratings.get(user, set()) - pos_items
#
#         # 随机选择与正向评分不重复的项目，并写入文件，并标记为0
#         for item in neg_items:
#             file.write(f"{user}\t{item}\t0\n")  # 0 表示负向评分
#
# print("已生成用户-项目-评分文件：", output_file)

item_dict = {}
# 打开文件
# 打开文件
with open('item_list.txt', 'r', encoding='utf-8') as file:
    # 创建一个空字典来存储结果
    item_dict = {}
    # 读取标题行
    headers = file.readline().strip().split('\t')  # 根据实际情况修改分隔符
    # print(headers)
    # 逐行读取文件
    for line in file:
        # 拆分每行，根据标题行的内容来解析
        values = line.strip().split('\t')  # 根据实际情况修改分隔符
        # 如果拆分后的部分数量不等于标题行的列数，则跳过这行
        if len(values) != len(headers):
            continue
        # 使用标题行的标题作为键，当前行的值作为对应键的值
        item_info = dict(zip(headers, values))
        # 将当前行数据存入字典中
        item_dict[item_info['item_dec']] = item_info['item_id']

# 打印字典
# print(item_dict)
item_set = set(item_dict.values())
# print(item_set)
item_set = {int(item) for item in item_set}
# print(item_set)

# print(item_set)
with open('item_set.txt', 'w', encoding='utf-8') as output_file:
    for item in item_set:
        output_file.write(item + '\n')

write_file =  "user_ratings_latest.txt"
# # logging.info("converting rating file to: %s", write_file)
writer = open(write_file, 'w', encoding='utf-8')
writer_idx = 0
user_cnt = 0
user_index_old2new = dict()
# for user, pos_item_set in user_pos_ratings.items():
#     pos_item_set = {int(item) for item in pos_item_set}  # Convert set of strings to set of integers
#     print(user, pos_item_set)


for user_index_old, pos_item_set in user_pos_ratings.items():
    # print(user_index_old)
    pos_item_set = {int(item) for item in pos_item_set}
    print(user_index_old2new)
    if user_index_old not in user_index_old2new:
        user_index_old2new[user_index_old] = user_cnt
        user_cnt += 1
    user_index = user_index_old2new[user_index_old]
    # print(user_index)
    for item in pos_item_set:
        writer_idx += 1
        writer.write('%d\t%d\t1\n' % (user_index, item))
    # print(item_set)
    # print(pos_item_set)
    unwatched_set = item_set - pos_item_set
    # print(unwatched_set)
    if user_index_old in user_neg_ratings:
        unwatched_set -= user_neg_ratings[user_index_old]
    for item in np.random.choice(list(unwatched_set), size=len(pos_item_set), replace=False):
        writer_idx += 1
        writer.write('%d\t%d\t0\n' % (user_index, item))
writer.close()
file_path = "user_ratings_latest.txt"
# file_path = "ratings_final.txt"
# 初始化计数器
count_0 = 0
count_1 = 0

# 逐行读取文件并统计
with open(file_path, "r") as file:
    for line in file:
        # 按制表符 '\t' 分割每一行，取第三列的值
        third_column_value = line.strip().split('\t')[2]
        if third_column_value == '0':
            count_0 += 1
        elif third_column_value == '1':
            count_1 += 1

print("第三列值为 0 的个数:", count_0)
print("第三列值为 1 的个数:", count_1)
