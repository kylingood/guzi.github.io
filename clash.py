import os
import requests
import datetime
import pytz  # 添加 pytz

# 获取当前脚本所在目录（GitHub Actions 里会是仓库根目录）
project_dir = os.path.dirname(os.path.abspath(__file__))

# 文件存储目录（确保目录存在）
save_yaml_path = os.path.join(project_dir, "yaml")
save_txt_path = os.path.join(project_dir, "txt")
os.makedirs(save_yaml_path, exist_ok=True)  # 创建 yaml 文件夹
# 生成当前日期
# 设置时区为北京时间（UTC+8）
beijing_tz = pytz.timezone('Asia/Shanghai')
today = datetime.datetime.now(beijing_tz).strftime("%Y/%m/%d")
year, month, day = today.split("/")

# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.yaml"
    url = f"https://node.freeclashnode.com/uploads/{year}/{month}/{file_name}"
    save_file = os.path.join(save_yaml_path, f"{i}.yaml")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.yaml"
    url = f"https://potatsolite.github.io/uploads/{year}/{month}/{file_name}"
    save_file = os.path.join(save_yaml_path, f"{i}.yaml")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.txt"
    url = f"https://node.freeclashnode.com/uploads/{year}/{month}/{file_name}"
    save_file = os.path.join(save_txt_path, f"{i}.txt")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")


# 遍历 0-4 生成文件名
for i in range(5):
    file_name = f"{i}-{year}{month}{day}.txt"
    url = f"https://potatsolite.github.io/uploads/{year}/{month}/{file_name}"
    save_file = os.path.join(save_txt_path, f"{i}.txt")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        with open(save_file, "wb") as f:
            f.write(response.content)

        print(f"✅ 成功下载: {save_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ 下载失败: {url} - {e}")
