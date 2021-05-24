# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import pandas as pd
# import numpy as np
# from string import digits
#
# pd.set_option('display.max_columns', 23)
# pd.set_option('display.width', 1500)
# pd.set_option('max_colwidth', 100)
# pd.set_option('display.max_rows', None)
#
#
# file = "C:\\Users\\netuser\\Desktop\\新建文件夹\\2021-05\\肾穿病理文本文件.txt"
#
# pathology_data = pd.DataFrame(columns=[
#     '病理号', '姓名', '性别', '年龄', '住院号', '送检日期', '医院', '科室', '病区', '临床诊断', '送检者',
#     '肾小球总数', '球性硬化小球数',  '节段性硬化数目','体积', '毛细血管丛','内皮细胞','管壁','基底膜','管腔','系膜区','嗜复红蛋白','肾小球囊', '其它',
#     '肾小管','上皮细胞','基底膜',
#     '间质','血管',
#     '免疫荧光','种类','特点','部位','诊断','诊断系数','评述'
# ])
#
# with open(file, encoding='utf8') as f:
#     for i, line in enumerate(f.readlines()):
#         if line != '\n':
#             content = line.split(':')[0].replace(' ', '')
#             if content == '病理号':
#                 pathology_data = pathology_data.append({'病理号': line.split(':')[1].split(' ')[0]}, ignore_index=True)
#                 print(line.split(':')[1].split(' ')[0])
#             if content == '姓名':
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '姓名'] = \
#                     line.split(':')[1].split(' ')[0].replace('\n', '')
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '性别'] = \
#                     line.split(':')[2].split(' ')[0].replace('\n', '')
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '年龄'] = \
#                     line.split(':')[3].split(' ')[0].replace('\n', '')
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '住院号'] = \
#                     line.split(':')[4].split(' ')[0].replace('\n', '')
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '送检日期'] = \
#                     line.split(':')[5].split(' ')[0].replace('\n', '')
#             if content == '医院':
#                 if len(line.split(':')) == 6:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '医院'] = \
#                         line.split(':')[1].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '科室'] = \
#                         line.split(':')[2].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '病区'] = \
#                         line.split(':')[3].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '临床诊断'] = \
#                         line.split(':')[4].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '送检者'] = \
#                         line.split(':')[5].split(' ')[0].replace('\n', '')
#                 if len(line.split(':')) == 5:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '医院'] = \
#                         line.split(':')[1].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '科室'] = \
#                         line.split(':')[2].split(' ')[0]
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '病区'] = \
#                         line.split(':')[3].split(' ')[0].replace('\n', '')
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '临床诊断'] = \
#                         line.split(':')[4].split(' ')[0].replace('\n', '')
#             if content == '肾小球':
#                 if pathology_data.iloc[len(pathology_data) - 1]['肾小球总数'] is np.nan:
#                     if '节段性硬化' in line:
#                         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球总数'] = \
#                             line.split('数量 ')[1].split(' ')[0].replace('\n', '')
#                         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '球性硬化小球数'] = \
#                             line.split('球性硬化 ')[1].split(' ')[0].replace('\n', '')
#                         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '节段性硬化数目'] = \
#                             line.split('节段性硬化 ')[1].split(' ')[0].replace('\n', '')
#                     else:
#                         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球总数'] = \
#                             line.split('数量 ')[1].split(' ')[0].replace('\n', '')
#                         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '球性硬化小球数'] = \
#                             line.split('球性硬化 ')[1].split(' ')[0].replace('\n', '')
#             if content == '体积':
#                 if pathology_data.iloc[len(pathology_data) - 1]['体积'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '体积'] = \
#                         line.split('体积:')[1].replace('\n', '')
#             if content == '毛细血管丛':
#                 if pathology_data.iloc[len(pathology_data) - 1]['毛细血管丛'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '毛细血管丛'] = \
#                         line.split('毛细血管丛:')[1].replace('\n', '')
#             if content == '内皮细胞':
#                 if pathology_data.iloc[len(pathology_data) - 1]['内皮细胞'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '内皮细胞'] = \
#                         line.split('内皮细胞:')[1].replace('\n', '')
#             if content == '管壁':
#                 if pathology_data.iloc[len(pathology_data) - 1]['管壁'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '管壁'] = \
#                             line.split('管壁:')[1].replace('\n', '')
#             if content == '基底膜':
#                 if pathology_data.iloc[len(pathology_data) - 1]['基底膜'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '基底膜'] = \
#                         line.split('基底膜:')[1].replace('\n', '')
#             if content == '管腔':
#                 if pathology_data.iloc[len(pathology_data) - 1]['管腔'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '管腔'] = \
#                         line.split('管腔:')[1].replace('\n', '')
#             if content == '系膜区':
#                 if pathology_data.iloc[len(pathology_data) - 1]['系膜区'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '系膜区'] = \
#                         line.split('系膜区:')[1].replace('\n', '')
#             if content == '嗜复红蛋白':
#                 if pathology_data.iloc[len(pathology_data) - 1]['嗜复红蛋白'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '嗜复红蛋白'] = \
#                         line.split('嗜复红蛋白:')[1].replace('\n', '')  # 免疫复合物，此处将描述全部取出
#             if content == '肾小球囊':
#                 if pathology_data.iloc[len(pathology_data) - 1]['肾小球囊'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球囊'] = \
#                         line.split('肾小球囊:')[1].replace('\n', '')
#             if content == '其它':
#                 if pathology_data.iloc[len(pathology_data) - 1]['其它'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '其它'] = \
#                         line.split('其它:')[1].replace('\n', '')
#             if content == '肾小管':
#                 if pathology_data.iloc[len(pathology_data) - 1]['肾小管'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小管'] = \
#                         line.split('肾小管:')[1].replace('\n', '')
#             if content == '上皮细胞':
#                 if pathology_data.iloc[len(pathology_data) - 1]['上皮细胞'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '上皮细胞'] = \
#                         line.split('上皮细胞:')[1].replace('\n', '')
#             if content == '基底膜':
#                 if pathology_data.iloc[len(pathology_data) - 1]['基底膜'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '基底膜'] = \
#                         line.split('基底膜:')[1].replace('\n', '')
#             if content == '间质':
#                 if pathology_data.iloc[len(pathology_data) - 1]['间质'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '间质'] = \
#                         line.split('间质:')[1].replace('\n', '')
#             if content == '血管':
#                 if pathology_data.iloc[len(pathology_data) - 1]['血管'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '血管'] = \
#                         line.split('血管:')[1].replace('\n', '')
#             if content == '免疫荧光':
#                 if pathology_data.iloc[len(pathology_data) - 1]['免疫荧光'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '免疫荧光'] = \
#                         line.split('免疫荧光:')[1].replace('\n', '')
#             if content == '种类':
#                 if pathology_data.iloc[len(pathology_data) - 1]['种类'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '种类'] = \
#                         line.split('种类:')[1].replace('\n', '')
#             # if content == '种类':
#             #     if pathology_data.iloc[len(pathology_data) - 1]['种类'] is np.nan:
#             #        if '种类' in line:
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '种类'] =\
#             #                line.split('种类 ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgG'] = \
#             #                line.split('IgG ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgA'] = \
#             #                 line.split('IgA ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgM'] = \
#             #                 line.split('IgM ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'C3'] = \
#             #                 line.split('C3 ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'C1q'] = \
#             #                 line.split('C1q ')[1].split(' ')[0].replace('\n', '')
#             #            pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'Fg'] = \
#             #                 line.split('Fg ')[1].split(' ')[0].replace('\n', '')
#             #         else:
#             #             pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '种类'] = \
#             #                 line.split('种类 ')[1].split(' ')[0].replace('\n', '')
#             #             pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgG'] = \
#             #                 line.split('IgG ')[1].split(' ')[0].replace('\n', '')
#             #             pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgA'] = \
#             #                 line.split('IgA ')[1].split(' ')[0].replace('\n', '')
#             #             pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), 'IgM'] = \
#             #                 line.split('IgM ')[1].split(' ')[0].replace('\n', '')
#             #种类分类会报错，不划分情况直接输出不会出现问题。应该是在一开始的列里面没有在这个时候分类新出现的数值。
#             if content == '特点':
#                 if pathology_data.iloc[len(pathology_data) - 1]['特点'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '特点'] = \
#                         line.split('特点:')[1].replace('\n', '')
#             if content == '部位':
#                 if pathology_data.iloc[len(pathology_data) - 1]['部位'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '部位'] = \
#                         line.split('部位:')[1].replace('\n', '')
#             if content == '诊断':
#                 if pathology_data.iloc[len(pathology_data) - 1]['诊断'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '诊断'] = \
#                         line.split('诊断:')[1].replace('\n', '')
#             if content == '诊断系数':
#                 if pathology_data.iloc[len(pathology_data) - 1]['诊断系数'] is np.nan:
#                     pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '诊断系数'] = \
#                         line.split('诊断系数:')[1].replace('\n', '')
#             #          if content == '诊断':
#             #     if pathology_data.iloc[len(pathology_data) - 1]['诊断'] is np.nan:
#             #         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '诊断'] = \
#             #             line.split(':')[1].split(' ')[0].replace('\n', '')
#             #         pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '诊断系数'] = \
#             #             line.split(':')[2].split(' ')[0].replace('\n', '')
#             # 这里的诊断系数在诊断一栏里出现，并未出现在诊断系数所在的行内。修改过后会报错。
#         if content == '评述':
#             if pathology_data.iloc[len(pathology_data) - 1]['评述'] is np.nan:
#                 pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '评述'] = \
#                     line.split('评述:')[1].replace('\n', '')
#
# pathology_data.head()
# pathology_data.to_excel("C:\\Users\\netuser\\Desktop\\新建文件夹\\2021-05\\肾穿病理文本文件2.1.xlsx",encoding='utf8', index=False)
#
#
# pathology_data = pd.read_excel("C:\\Users\\netuser\\Desktop\\新建文件夹\\2021-05\\肾穿病理文本文件2.1.xlsx",encoding='utf8')
#
# #肾小球囊需要提取，先转换成字符串类型进行提取，再查看可能出现的情况，情况可以自己查看不写出来。再将没有数字的列用0填充，使每一列都不存在没有数字的空列
# #进行操作之后再转换类型就会得到存在数字的每一列，将不同的列相加，得到新列之后再与获取的新月体小球数目进行对比，再取二者之中的最大值
# pathology_data['肾小球囊'] = pathology_data['肾小球囊'].astype(str)
# pathology_data['肾小球囊'] = pathology_data['肾小球囊'].apply(lambda x: x.replace(' ', ''))
# pathology_data.loc[585, '肾小球囊'] = '未见明显改变'#根据出现的情况进行改变
# pathology_data[['肾小球囊a', '肾小球囊b']] = pathology_data['肾小球囊'].str.extract('(\d+)\D*(\d+)')
# pathology_data[['肾小球囊a', '肾小球囊b']] = pathology_data[['肾小球囊a', '肾小球囊b']].fillna(0)
# pathology_data[['肾小球囊a', '肾小球囊b']] = pathology_data[['肾小球囊a', '肾小球囊b']].astype(int)
# pathology_data['肾小球囊ab'] = pathology_data['肾小球囊a'] + pathology_data['肾小球囊b']  #肾小球囊新月体是相加起来的
# pathology_data = pathology_data.drop(pathology_data[['肾小球囊a', '肾小球囊b']], axis=1) #删除这两列，axis=0表示行，axis=1表示列。
# pathology_data['新月体小球数目'] = pathology_data['肾小球囊'].str.extract('(\d+)') #抽取匹配的数据
# pathology_data['新月体小球数目'] = pathology_data['新月体小球数目'].fillna(0)  #填充一下NAN，使其存在一个值（值是0）
# pathology_data['新月体小球数目'] = pathology_data['新月体小球数目'].astype(int)
# pathology_data['新月体小球数目'] = pathology_data.apply(lambda x: max(x['新月体小球数目'], x['肾小球囊ab']), axis=1) #在列中进行对比，并在表格输出二者中较大的那个数
# del pathology_data['肾小球囊ab']  #输出新月体数目以后删除掉多余的列
#
#
# # 根据Word文档标注，内皮细胞的话增生分四种情况：未见明显变化、轻、中、重，分别对应0,1,2,3四个数字。提取的原理与肾小球囊差不多。
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].astype(str)
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace(' ', ''))
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.translate(str.maketrans('', '', digits)))  #因为四种情况是用0，1。2。3。四个数字代替的，所有去除多余的数字后面进行数字与情况配对的时候就不会存在干扰
# #增生是等级的标准，需要找到匹配的项，运用lambda函数求每一列中的这几个关键字
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('增生', '1增生'))
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('轻', '0轻'))
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('中', '1中'))
# pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('重', '2重'))
# #取了之后创建新的列，以此来获得内皮细胞的数据
# neipixibao = pathology_data[pathology_data['内皮细胞'].str.contains('增生')][['病理号', '内皮细胞']]
# neipixibao[['内皮细胞a', '内皮细胞b']] = neipixibao['内皮细胞'].str.extract('(\d+)\D*(\d+)')
# neipixibao[['内皮细胞a', '内皮细胞b']] = neipixibao[['内皮细胞a', '内皮细胞b']].fillna(0)
# neipixibao[['内皮细胞a', '内皮细胞b']] = neipixibao[['内皮细胞a', '内皮细胞b']].astype(int)
# neipixibao['内皮细胞ab'] = neipixibao['内皮细胞a'] + neipixibao['内皮细胞b']
# neipixibao = neipixibao.drop(neipixibao[['内皮细胞a', '内皮细胞b']], axis=1)
# neipixibao['内皮细胞增生'] = neipixibao['内皮细胞'].str.extract('(\d+)')
# neipixibao['内皮细胞增生'] = neipixibao['内皮细胞增生'].fillna(0)
# neipixibao['内皮细胞增生'] = neipixibao['内皮细胞增生'].astype(int)
# neipixibao['内皮细胞增生'] = neipixibao.apply(lambda x: max(x['内皮细胞增生'], x['内皮细胞ab']), axis=1)
# del neipixibao['内皮细胞ab']
# pathology_data = pd.merge(pathology_data, neipixibao, on=['病理号', '内皮细胞'], how='left').fillna(0)  #left左连接，将现在得到的数据与原来的表格进行合并汇总.用right能输出，但是结果只是内皮细胞增生，得不到需要的结果。
#
#
# #根据Word文档的要求，还要提取出毛细血管管腔，分为狭窄和闭塞两种情况，狭窄分为轻，中，重；闭塞分为有和无。
# # 标注为未见明显改变、狭窄轻、狭窄中、狭窄重和闭塞，分别用0,1,2,3,4表示。
# #提取原理与肾小球类似，但是需要考虑以下几种情况：1.只有狭窄相关 2.只有闭塞（暂时还不知道是否有） 3.又有狭窄又有闭塞
#
# pathology_data['管腔'] = pathology_data['管腔'].astype(str)
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace(' ', ''))
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('狭窄', '1狭窄'))
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('轻', '0轻'))
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('中', '1中'))
# pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('重', '2重'))
# print(len(pathology_data[pathology_data['管腔'].str.contains('狭窄') & pathology_data['管腔'].str.contains('闭塞')]))  #看是否有狭窄和闭塞同时存在的情况
# xiazhai = pathology_data[pathology_data['管腔'].str.contains('狭窄')][['病理号', '管腔']]
# xiazhai[['管腔a', '管腔b']] = xiazhai['管腔'].str.extract('(\d+)\D*(\d+)')
# xiazhai[['管腔a', '管腔b']] = xiazhai[['管腔a', '管腔b']].fillna(0)
# xiazhai[['管腔a', '管腔b']] = xiazhai[['管腔a', '管腔b']].astype(int)
# xiazhai['管腔c'] = xiazhai['管腔a'] + xiazhai['管腔b']
# xiazhai = xiazhai.drop(xiazhai[['管腔a', '管腔b']], axis=1)
# xiazhai['毛细血管管腔'] = xiazhai['管腔'].str.extract('(\d+)')  #将管腔中的值存储在毛细血管管腔中，后面是将空列用0填充，在后面好进行对比
# xiazhai['毛细血管管腔'] = xiazhai['毛细血管管腔'].fillna(0)
# xiazhai['毛细血管管腔'] = xiazhai['毛细血管管腔'].astype(int)
# xiazhai['毛细血管管腔'] = xiazhai.apply(lambda x: max(x['毛细血管管腔'], x['管腔c']), axis=1)
# del xiazhai['管腔c']
# pathology_data = pd.merge(pathology_data, xiazhai, on=['病理号', '管腔'], how='left').fillna(0)  #仍然是左连接进行列表信息的合并汇集，用right也不会出现想要的结果。
# pathology_data.loc[pathology_data['管腔'].str.contains('闭塞'), '毛细血管管腔'] = 3 #整理一下看看有没有出现为闭塞情况的，有的话将注释改变一下
#
# #根据文档可知免疫复合物的指标是嗜复红蛋白，嗜复红蛋白会出现两种情况：无明显可见和有。无明显可见用0表示，嗜复红蛋白沉积用1表示。
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].astype(str)
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace(' ', ''))
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# #嗜复红蛋白会出现无明显表示，在毛细血管沉积等等。通过对情况的分析，提取出嗜复红蛋白所在的所有区域
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('毛细血管壁', '2毛细血管壁'))
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('系膜区', '1系膜区'))
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('内皮下', '1内皮下'))
# pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('硬化区', '2硬化区'))
# pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']] = pathology_data['嗜复红蛋白'].str.extract('(\d+)\D*(\d+)')
# pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']] = pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']].fillna(0)
# pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']] = pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']].astype(int)
# pathology_data['嗜复红蛋白c'] = pathology_data['嗜复红蛋白a'] + pathology_data['嗜复红蛋白b']
# pathology_data = pathology_data.drop(pathology_data[['嗜复红蛋白a', '嗜复红蛋白b']], axis=1)
# pathology_data['免疫复合物'] = pathology_data['嗜复红蛋白'].str.extract('(\d+)')
# pathology_data['免疫复合物'] = pathology_data['免疫复合物'].fillna(0)
# pathology_data['免疫复合物'] = pathology_data['免疫复合物'].astype(int)
# pathology_data['免疫复合物'] = pathology_data.apply(lambda x: max(x['免疫复合物'], x['嗜复红蛋白c']), axis=1)
# del pathology_data['嗜复红蛋白c']
#
#
#
# # 肾小管萎缩有未见明显改变和萎缩，0表示未见明显变化，肾小管萎缩用百分数表示。根据比例分为轻，中，重，用1,2,3表示。
# # （1）将“肾小管”列转换为str类型
# pathology_data['肾小管'] = pathology_data['肾小管'].astype(str)
# pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace(' ', ''))
# pathology_data['肾小管萎缩'] = pathology_data['肾小管'].str.extract('(\d+)')
# pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('轻', '1轻'))
# pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('中', '2中'))
# pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('重', '3重'))
# shenxiaoguanweisuo = pathology_data[pathology_data['肾小管萎缩'].isna()][['病理号', '肾小管']]
# shenxiaoguanweisuo['肾小管萎缩a'] = shenxiaoguanweisuo['肾小管'].str.extract('(\d+)')
# pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'].fillna('0')
# # （9）将“肾小管萎缩”列值添加%
# pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'] + '%'
# pathology_data = pd.merge(pathology_data, shenxiaoguanweisuo, on=['病理号', '肾小管'], how='left')
# for i in range(len(pathology_data)):
#     if pathology_data.iloc[i]['肾小管萎缩'] == '0%':
#         pathology_data.loc[i, '肾小管萎缩'] = pathology_data.iloc[i]['肾小管萎缩a']
# del pathology_data['肾小管萎缩a']
# pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'].fillna('0')
#
#
# # 根据Word文档了解到间质纤维化分为未见明显改变和纤维化。用0表示未见明显改变，1表示纤维化轻，2是纤维化中，3是纤维化重。
# pathology_data['间质'] = pathology_data['间质'].astype(str)
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace(' ', ''))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('纤维化', '1纤维化'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('轻', '0轻'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('中', '1中'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('重', '2重'))
# jianzhixianweihua = pathology_data[pathology_data['间质'].str.contains('纤维化')][['病理号', '间质']]
# jianzhixianweihua[['间质a', '间质b']] = jianzhixianweihua['间质'].str.extract('(\d+)\D*(\d+)')
# jianzhixianweihua[['间质a', '间质b']] = jianzhixianweihua[['间质a', '间质b']].fillna(0)
# jianzhixianweihua[['间质a', '间质b']] = jianzhixianweihua[['间质a', '间质b']].astype(int)
# jianzhixianweihua['间质c'] = jianzhixianweihua['间质a'] + jianzhixianweihua['间质b']
# jianzhixianweihua = jianzhixianweihua.drop(jianzhixianweihua[['间质a', '间质b']], axis=1)
# jianzhixianweihua['间质纤维化'] = jianzhixianweihua['间质'].str.extract('(\d+)')
# jianzhixianweihua['间质纤维化'] = jianzhixianweihua['间质纤维化'].fillna(0)
# jianzhixianweihua['间质纤维化'] = jianzhixianweihua['间质纤维化'].astype(int)
# jianzhixianweihua['间质纤维化'] = jianzhixianweihua.apply(lambda x: max(x['间质纤维化'], x['间质c']), axis=1)
# del jianzhixianweihua['间质c']
# pathology_data = pd.merge(pathology_data, jianzhixianweihua, on=['病理号', '间质'], how='left').fillna(0)
#
# # 间质炎症细胞浸润的标注是间质细胞浸润，分为未见明显改变（用0表示）、单个细胞核浸润轻（用1表示）、单个细胞核浸润中（用2表示）、单个细胞核浸润重（用3表示）
# #先前间质已经读过一遍，现在只要提取关键字就行了，仍然是需要去除多余数字防止干扰。但是也出现了淋巴细胞浸润的情况，也需要提出来。淋巴细胞浸润和炎症细胞浸润的表示数字相同
# #但是这里炎症细胞和淋巴细胞不一样，需要考虑情况为：炎症细胞浸润，淋巴细胞浸润，炎症细胞和淋巴细胞都浸润
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('单个核细胞浸润', '1单个核细胞浸润'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('淋巴细胞浸润', '1淋巴细胞浸润'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('轻', '0轻'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('中', '1中'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('重', '2重'))
# pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('大量', '2大量'))
# print(len(pathology_data[pathology_data['间质'].str.contains('单个核细胞浸润') & pathology_data['间质'].str.contains('淋巴细胞浸润')]))
# xibaojinrun = pathology_data[pathology_data['间质'].str.contains('单个核细胞浸润') |
#                             pathology_data['间质'].str.contains('淋巴细胞浸润')][['病理号', '间质']]
# xibaojinrun[['间质a', '间质b']] = xibaojinrun['间质'].str.extract('(\d+)\D*(\d+)')
# xibaojinrun[['间质a', '间质b']] = xibaojinrun[['间质a', '间质b']].fillna(0)
# xibaojinrun[['间质a', '间质b']] = xibaojinrun[['间质a', '间质b']].astype(int)
# xibaojinrun['间质c'] = xibaojinrun['间质a'] + xibaojinrun['间质b']
# xibaojinrun = xibaojinrun.drop(xibaojinrun[['间质a', '间质b']], axis=1)
# xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质'].str.extract('(\d+)')
# xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质炎症细胞浸润'].fillna(0)
# xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质炎症细胞浸润'].astype(int)
# xibaojinrun['间质炎症细胞浸润'] = xibaojinrun.apply(lambda x: max(x['间质炎症细胞浸润'], x['间质c']), axis=1)
# del xibaojinrun['间质c']
# pathology_data = pd.merge(pathology_data, xibaojinrun, on=['病理号', '间质'], how='left').fillna(0)
#
#
# # 根据Word文档，硬化小球比例：球性硬化小球数/肾小球总数，要考虑分母为0的情况，分母为零就是不存在为空值。需要填充值进去，用inf值进行填充。
# pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].astype(str)
# pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].apply(lambda x: x.replace(',', ''))
# pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].astype(int)
# pathology_data['肾小球总数'] = pathology_data['肾小球总数'].astype(str)
# pathology_data['肾小球总数'] = pathology_data['肾小球总数'].apply(lambda x: x.split('(')[0])
# pathology_data['肾小球总数'] = pathology_data['肾小球总数'].astype(int)
# pathology_data['硬化小球比例'] = pathology_data['球性硬化小球数'] / pathology_data['肾小球总数']
# pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# pathology_data['硬化小球比例'] = pathology_data['硬化小球比例'].fillna(0)
#
# # 文档有节段硬化小球比例=节段性硬化数目/肾小球总数，也要考虑相加为0不存在的情况，需要用inf填充
# pathology_data['节段硬化小球比例'] = pathology_data['节段性硬化数目'] / pathology_data['肾小球总数']
# pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# pathology_data['节段硬化小球比例'] = pathology_data['节段硬化小球比例'].fillna(0)
#
# # 在文档中新月体小球比例=新月体小球数目/肾小球总数。仍旧要考虑填充的问题。
# pathology_data['新月体小球比例'] = pathology_data['新月体小球数目'] / pathology_data['肾小球总数']
# pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# pathology_data['新月体小球比例'] = pathology_data['新月体小球比例'].fillna(0)
#
# pathology_data.to_excel("C:\\Users\\netuser\\Desktop\\新建文件夹\\2021-05\\肾穿病理文本文件2.2.xlsx",encoding='utf8', index=False)
#



# import pandas as pd
# import numpy as np
# from string import digits
#
# pd.set_option('display.max_columns',23)
# pd.set_option('display.width',1500)
# pd.set_option('max_colwidth',100)
# pd.set_option('display.max_rows',None)
#
# sz_data=pd.read_excel('C:\\Users\\netuser\\Desktop\\新建文件夹\\2021-05\\HIS系统病理筛选.xlsx')
# #print(sz_data)  #这里是查看全部数据
# is_guangjing = sz_data[sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('光镜：')]
# #print(is_guangjing)  #查看光镜的全部情况
#
# #切片分割，获取含有光镜相关信息的字符串。（应该是只存放光镜冒号后面的相关信息）(打印了一下，是的。只输出光镜后面的信息)
# a=sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'] = sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].apply(lambda x: x.split('光镜：')[1])
# #print(a)   #这个a先删除了，需要输出的时候再填补在上一行的最前面，即a=sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].apply(lambda x:x.split('光镜：')[1])
# print(len(sz_data[sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('小结')]))  #这里结果是1191，原先是1195，证明有四条内容是没有小结的
# sz_data['诊断'] = sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.extract('.*?小结：([\d\D*|\D*]+)') #其实这个小结这里有点没太懂，是不是说看这段里面是否有特殊的字符串啥的，百度比较少，先整理一下
# print(sz_data[sz_data['诊断'].isna()])  #这里其实是输出没有小结的记录，查看四条没有小结的数据的具体内容
# sz_data['诊断'] = sz_data['诊断'].fillna('无')  #填充了nan值，应该是待会删除的时候方便操作不会报错
#
#
# sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'] = sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].apply(lambda x: x.split('小结')[0]) #防止后面会出现的总结有重复内容会跟小结有冲突，所以去除小结的内容
# print(len(sz_data[sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('小结')]))   #这个是检查还有没有存在小结，不存在了，显示为0
# #
# print(len(sz_data[sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('未见肾小球')]))  #这里的打印出现了17，开始怪了。为啥是17啊，我不明白
# sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'] = sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].apply(lambda x: x.replace('未见肾小球', '0个未见肾小球'))
# print(len(sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('(未见[\u4E00-\u9FA5]+肾小球)'))) #这里我没看懂，为什么要查看这个记录
# sz_data['肾小球总数'] = sz_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.extract('[，。？！,.?!]*(\d+|[一二三四五六七八九十]+)\D*肾小球')
# print(sz_data[sz_data['肾小球总数'].isna()])  #这里我有两条，一个是皮质肾组织2条，镜下仅见9个废弃球。肾小管间质慢性病变重度，斑片状小管萎缩、基膜增厚，未萎缩小管代偿性肥大。另一个是皮髓质肾组织1条，仅见一个完全硬化的小球。
# sz_data.loc[804, '肾小球总数'] = '1'
# sz_data.loc[523, '肾小球总数'] = '12'
# sz_data.loc[737, '肾小球总数'] = '9'
# print(sz_data[sz_data['肾小球总数'] == '0'])
# sz_data['肾小球总数'] = sz_data['肾小球总数'].astype(int)

