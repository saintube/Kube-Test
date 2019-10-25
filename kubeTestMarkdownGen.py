#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os, sys
import time
import yaml
import json
from random import choice



root_folder = './'  # 将被递归的文件夹根目录
save_txt = './paths.txt'  # 记录路径的文档
suffix_name = '.log'  # 后缀名


#读取yaml文件统计信息
def readYaml():
    save_file = open('./caseLogPath.txt', 'w',encoding='UTF-8')
    for name in os.listdir(os.path.abspath(root_folder)):
        if os.path.isdir(os.path.join(os.path.abspath(root_folder), name)):
            record(os.path.join(os.path.abspath(root_folder), name), './caseLogPath.txt')
        elif name.endswith('-result.yaml'):
            save_file.write('{}\n'.format(os.path.join(os.path.abspath(root_folder), name)))
    save_file.close()
    res_dict = []

    f = open('./caseLogPath.txt', "r")
    lines = f.readlines()
    print(len(lines))
    result_pass = 0
    for line in lines:
        dict = {}
        #print(lines[i])
        line = line.strip('\n')
        with open(line, "r") as yaml_file:
            yaml_obj = yaml.load(yaml_file.read())
            #print(yaml_obj)
            caseName = yaml_obj['metadata']['name']
            chaostype = yaml_obj['spec']['testMetadata']['chaostype']
            result = yaml_obj['spec']['testStatus']['result']
            if result == 'Pass':
                result_pass += 1

            dict['caseName'] = caseName
            dict['chaostype'] = chaostype
            dict['result'] = result
        res_dict.append(dict)

    #print(res_dict)

    article_info = {}
    data = json.loads(json.dumps(article_info))
    data["cicounts"] = "10 times"
    data["successes"] = str(result_pass) + "cases"
    data["errors"] = str(len(res_dict) - int(result_pass)) + "cases"
    data["timecost"] = "13.2mins"

    article2 = {"labels":['Last 8','Last 7','Last 6','Last 5','Last 4','Last 3','Last 2','Latest'],
                "series":[[20, 20, 40, 40, 60, 80, 100, 100]],
                }
    data["building_history"] = article2

    article3 = {"labels":[str(result_pass/len(res_dict)*100)+'%', str((1-result_pass/len(res_dict))*100)+'%'],
                "series":[result_pass/len(res_dict), 1-result_pass/len(res_dict)]
    }
    #data["dataPie"][ "labels"] = [result_pass/len(res_dict), 1-result_pass/len(res_dict)]
    #data["dataPie"]["labels"] = [result_pass/len(res_dict), 1-result_pass/len(res_dict)]

    data["dataPie"] = article3
    article = json.dumps(data,ensure_ascii=False)
    #print(article)

    with open('datashboard.json', 'w') as f:
        json.dump(data,f)

    #return dict


# Clear blank line
def clearBlankLine(file):
    file1 = open(file, 'r', encoding='utf-8')
    file2 = open('./text2.txt', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            elif "===" in line:
                pass
            else:
                file2.write(line)
    finally:
        file1.close()
        file2.close()

# clear colour
def clearColour(rawString):
    List = ['[0;30m', '[0;31m', '[0;32m', '[0;33m', '[0;34m', '[0;35m', '[0;36m'
        , '[1;30m', '[1;31m', '[1;32m', '[1;33m', '[1;34m', '[1;35m', '[1;36m']
    for m in List:
        rawString = rawString.strip(m)
    if '[0m\n' in rawString:
        rawString = rawString.replace('[0m', '')
    if '' in rawString:
        rawString = rawString.replace('', '')
    return rawString


def clearStr(rawString):
    if '*' in rawString:
        rawString = rawString.replace('*', '')
        # print(ss.replace('\n', ''))
    return rawString


def markdownFileGen(filename):
    file1 = open('./text2.txt', 'r', encoding='utf-8')
    file2 = open(filename, 'w', encoding='utf-8')
    #f = open("./text2.txt", "r")
    lines = f.readlines()
    try:
        for line in file1.readlines():
            res = clearColour(line)
            res = clearStr(res)
            if "TASK" in res:
                res = '``` \n' + '\n## ' + res + '``` \n'
            elif re.match(r'^9-', res) is not None:
                res = "time:" + '201' + res
            file2.write(res)
    finally:
        file1.close()
        file2.close()

def statisticalInfo(filename):
    '''
    Return to run results
    '''
    result = []
    file = open(filename, 'r', encoding='utf-8')
    # temp = file.readlines()
    for line in file.readlines():

        if "ok=" in line:
            okindex = int(line.index("ok=")) + 3
            okstr = ''
            while okindex < len(line) and line[okindex] != ' ':
                okstr += line[okindex]
                okindex += 1
            result.append(int(okstr))
            # result['ok']=int(okstr)
            #print("ok = ",int(okstr))

        if "changed=" in line:
            changeindex = line.index("changed=") + 8
            changestr = ''
            while changeindex < len(line) and line[changeindex] != ' ':
                changestr += line[changeindex]
                changeindex += 1
            result.append(int(changestr))
            # result['change']=int(changestr)
            #print("change = ", int(changestr))

        if "unreachable=" in line:
            unreachableindex = line.index("unreachable=") + 12
            unreachablestr = ''
            while unreachableindex < len(line) and line[unreachableindex] != ' ':
                unreachablestr += line[unreachableindex]
                unreachableindex += 1
            result.append(int(unreachablestr))
            # result['unreachable']=int(unreachablestr)
            #print("unreachable = ", int(unreachablestr))

        if "failed=" in line:
            failedindex = line.index("failed=") + 7
            failedstr = ''
            while failedindex < len(line) and line[failedindex] != '   ':
                failedstr += line[failedindex]
                failedindex += 1
            result.append(int(failedstr))
            # result['failed']=int(failedstr)
            #print("failed = ", int(failedstr))
        file.close()
        # print(result)
        # print(json.dumps(result, sort_keys=True, separators=(',', ':')))
    return result


def removeFile():
    if os.path.exists('./text2.txt'):
        os.remove('./text2.txt')
    # print("Done !")


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    # return str(timeSruct)
    return time.strftime('%Y-%m-%dT%H:%M:%S', timeStruct)


def get_FileCreateTime(filePath):
    # filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def record(folder, save_txt):
    save_file = open(save_txt, 'a')
    for name in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, name)):
            record(os.path.join(folder, name), save_txt)
        elif name.endswith(suffix_name):
            save_file.write('{}\n'.format(os.path.join(folder, name)))
    save_file.close()


def recordDir():
    try:
        os.remove(save_txt)
    except OSError:
        pass
    record(os.path.abspath(root_folder), save_txt)


def writeStatisticalInfo(list, file_rawname, filename):
    with open(filename, "r+") as f:
        old = f.read()
        f.seek(0)

        f.write('=== \n')
        f.write('\n')
        f.write('标题： CommitID: ')
        with open(filename, 'r') as fp:
            lines = fp.readlines()
            last_line = lines[-1].strip('\n')
        GITHUB_SHA = last_line
        f.write(GITHUB_SHA)
        #f.write(']')
        f.write(get_FileCreateTime(file_rawname))
        f.write('\n标签： ')

        Listtag = ['app-pod-failure', 'pod-delete', 'network-delete']
        f.write(choice(Listtag))

        #f.write(get_FileCreateTime(file_rawname))
        f.write('\n\n')
        #print(get_FileCreateTime(file_rawname))
        f.write('=== \n')
        f.write('\n')

        f.write('# Summary report \n')
        f.write('| Task status | number |\n')
        f.write('| ------------ | ------------ |\n')

        f.write('|      ok |      ')
        f.write(str(list[0]))
        f.write('\n')

        f.write('|      change |      ')
        f.write(str(list[1]))
        f.write('\n')

        f.write('|      unreachable |      ')
        f.write(str(list[2]))
        f.write('\n')

        f.write('|      failed |      ')
        f.write(str(list[3]))
        f.write('\n')

        f.write('# Info report \n ``` \n')

        f.write(old)
        f.write('``` \n')


if __name__ == '__main__':
    recordDir()  # 获取log日志路径
    f = open(save_txt, "r")
    lines = f.readlines()  # 读log日志的路径列表
    res_list = []
    readYaml()
    for i in range(len(lines)):
        line = lines[i].strip('\n')
        clearBlankLine(line)
        fileName_temp = './posts/' + get_FileCreateTime(line)
        if not os.path.exists(fileName_temp):
            os.makedirs(fileName_temp)
        fileName = fileName_temp + '/article.md'
        markdownFileGen(fileName)
        res = statisticalInfo(fileName)
        res_list.append(res)
        removeFile()
        writeStatisticalInfo(res, line, fileName)
    #print(res_list)
