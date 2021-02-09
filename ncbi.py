# -*- coding = utf-8 -*-
# @Time :2021-02-08 15:49
# @Author : Broth Yang
# @File :NCBI.py
# @Software :PyCharm

import requests


def Write_Fasta(Key, data):
    fileName = Key + '.fasta'
    with open('./fasta/'+fileName, 'w', encoding='utf-8') as fp:
        fp.write(data)


def Get_Data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'
    }
    Key_word = str(input('请输入要搜索的关键词:'))
    url = 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?' + 'id=' + Key_word + '&db=nuccore&report=fasta&extrafeat=null&conwithfeat=on&hide-cdd=on&retmode=html&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=1000000'
    res = requests.get(url=url, headers=headers, timeout=4)
    page_text = res.text
    Write_Fasta(Key_word, page_text)
    print('文件下载成功')


if __name__ == '__main__':
    Get_Data()

