# 从本地判断图片是否损坏
# forked from https://www.cnblogs.com/helongBlog/p/11608579.html

import os

def check_jpg(path):
    ''' 检查jpeg文件是否损坏 '''
    try:
        fileObj = open(path, 'rb')  # 以二进制形式打开
        buf = fileObj.read()
        if not buf.startswith(b'\xff\xd8'):  # 是否以\xff\xd8开头
            return False
        elif buf[6:10] in (b'JFIF', b'Exif'):  # “JFIF”的ASCII码
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):  # 是否以\xff\xd9结尾
                return False
        else:
            try:
                Image.open(fileObj).verify()
            except Exception as e:
                return False
    except Exception as e:
        return False
    return True

for root, dirs, files in os.walk(r"/root/bw/datasets/SKU110K_fixed/images"):
    for file in files:
        if file[-4:] != '.jpg': continue
        file_path = os.path.join(root,file)
        flag = check_jpg(file_path)
        if not flag:
            print(file_path)
            os.remove(file_path)

# /root/bw/datasets/SKU110K_fixed/images/train_4222.jpg
# /root/bw/datasets/SKU110K_fixed/images/train_340.jpg
# /root/bw/datasets/SKU110K_fixed/images/train_882.jpg
# /root/bw/datasets/SKU110K_fixed/images/test_274.jpg
# /root/bw/datasets/SKU110K_fixed/images/train_924.jpg
# /root/bw/datasets/SKU110K_fixed/images/test_853.jpg
# /root/bw/datasets/SKU110K_fixed/images/train_3556.jpg
