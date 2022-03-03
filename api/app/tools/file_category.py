import os
import shutil
from pathlib import Path
from filecmp import cmp

src = Path('~/Downloads')
des = Path('~/2020')


# 按文件的类型分类
def file_category(src, des):
    files = src.glob('*')
    for f in files:
        if f.is_file():
            des = des / f.suffix.strip('.')
            if not des.exists():
                des.mkdir(parents=True)
            f.replace(des / f.name)


# 删除重复文件
def delete_duplicate_file(src, des):
    if not des.exists():
        des.mkdir(parents=True)

    result = list(src.glob('*'))
    file_list = []
    for f in result:
        if f.is_file():
            file_list.append(f)

    for m in file_list:
        for n in file_list:
            if m != n and m.exists() and n.exists():
                if cmp(m, n):
                    n.replace(des / n.name)
