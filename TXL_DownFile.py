import os
import pandas as pd
from datasets import load_dataset

# Đổi cache sang ổ D để tránh dùng ổ C
# os.environ["HF_DATASETS_CACHE"] = r"D:\hf_cache"

# Thư mục lưu CSV đầu ra
save_dir = r"D:\Data_TimeSeries"
os.makedirs(save_dir, exist_ok=True)

# Số phần bạn muốn chia (mỗi phần là 10%)
num_parts = 10  # 10 phần tương ứng 10% mỗi phần

for i in range(num_parts):
    start = i * 10
    end = (i + 1) * 10
    print(f"Đang tải phần {i+1}/{num_parts}: {start}% đến {end}%")

    # Tải phân đoạn dataset
    split_str = f"train[{start}%:{end}%]"
    dataset = load_dataset("enryu43/twitter100m_tweets", split=split_str)

    # Chuyển thành DataFrame
    df = dataset.to_pandas()

    # Giữ lại 2 cột cần thiết
    df = df[["tweet", "date"]]

    # Lưu file CSV cho từng phần
    save_path = os.path.join(save_dir, f"twitter100m_part{i+1:02}.csv")
    df.to_csv(save_path, index=False)

    print(f"Đã lưu {save_path}\n")
