import pandas as pd
import re
import ast 
# Đọc file CSV
df = pd.read_csv('du_lieu.csv')  # Thay bằng tên file thật của bạn

# Hàm làm sạch nội dung cột 'tweet'
def clean_tweet(text):
    if isinstance(text, str):
        # Thay ký tự không phải chữ, số, khoảng trắng, # hoặc ' bằng dấu cách
        text = re.sub(r"[^a-zA-Z0-9\s#']", ' ', text)
        # Làm gọn khoảng trắng dư thừa
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return text

# Chỉ xử lý cột 'tweet'
df['tweet'] = df['tweet'].apply(clean_tweet)

# Hàm trích xuất hashtag, giữ cả hashtag chứa số, chuẩn hóa lowercase
def extract_hashtags(text):
    if not isinstance(text, str):
        return []
    hashtags = re.findall(r"#\w+", text)
    return [tag.lower() for tag in hashtags] 

# Tạo cột mới 'hashtag'
df['hashtag'] = df['tweet'].apply(extract_hashtags)

df = df.drop(columns=['tweet'])
# Chuyển chuỗi list về list thực sự
df['hashtag'] = df['hashtag'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])

# Bỏ các dòng có hashtag rỗng
df_hashtag_only = df[df['hashtag'].apply(lambda x: len(x) > 0)]

# Ghi kết quả ra file mới
df.to_csv('du_lieu_sach.csv', index=False)

