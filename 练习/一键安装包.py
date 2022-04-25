import os

libs = {'requests', 'turtle', 'numpy', 'lxml', 'bs4', 'cvs', 'pygame', 'scrapy', 'portia', 'cola', 'selenium',
        'pymongo', 'openpyxl', 'PIL'}
for lib in libs:
    try:
        os.system("pip install " + lib)
        print("Success")
    except:
        print("没有安装" + lib)
