from urllib.parse import urlparse

def count_top_level_dirs(urls):
    # 创建一个字典来存储每个一级目录的出现次数
    dir_counts = {}

    for url in urls:
        # 解析 URL
        parsed_url = urlparse(url)
        
        # 获取一级目录
        top_level_dir = parsed_url.path.split('/')[1] if len(parsed_url.path.split('/')) > 1 else ''
        
        # 统计次数
        if top_level_dir in dir_counts:
            dir_counts[top_level_dir] += 1
        else:
            dir_counts[top_level_dir] = 1

    return dir_counts

def read_urls_from_file(file_path):
    # 从文件中读取 URLs
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file]

    return urls

# 从文件中读取 URLs
file_path = 'urls.txt'
urls_from_file = read_urls_from_file(file_path)

# 统计一级目录出现次数
result = count_top_level_dirs(urls_from_file)

# 按出现次数从大到小排序
sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

# 打印排序后的结果
for dir, count in sorted_result.items():
    print(f"{dir}: {count} 次")

