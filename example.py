import pandas as pd

# 读取 TXT 文件，使用空格 ' ' 分隔，并设置 header=None 表示没有标题行，指定文件编码为 GBK
# file_path = 'item_index2entity_id.txt'  # 替换为你的 TXT 文件路径
file_path = 'ratings_final.txt'  # 替换为你的 TXT 文件路径
df = pd.read_csv(file_path, sep='\t', header=None, encoding='UTF-8')  # 假设 TXT 文件中的列是以空格分隔的，并且没有标题行

# 打印 DataFrame 的头几行数据
print(df.head())
# 查看每列的数据类型
print(df.dtypes)



