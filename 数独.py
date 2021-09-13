import copy


class shudu_number:
    number = 0
    might_number_list = []
    list_number_count = 0


test = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]
shudu_list = [
    0, 0, 6, 0, 4, 2, 0, 0, 3,
    0, 0, 4, 3, 6, 8, 0, 0, 7,
    0, 0, 0, 5, 0, 0, 0, 0, 0,
    4, 0, 0, 0, 0, 0, 0, 0, 0,
    5, 0, 0, 0, 0, 3, 2, 0, 0,
    0, 0, 2, 6, 0, 0, 0, 5, 9,
    1, 0, 0, 0, 0, 0, 0, 7, 0,
    0, 2, 5, 8, 0, 0, 0, 0, 0,
    0, 7, 3, 0, 1, 0, 0, 0, 0
]


# 消除行列，3*3的格子中不可能的数
def delete_might(delete_shudu_list, delete_might_number_location, delete_might_number):
    function_number_hang = int(delete_might_number_location / 9)
    function_number_lie = delete_might_number_location % 9
    # 消除行
    for process_delete_might_location in range(function_number_hang * 9, function_number_hang * 9 + 9):
        if delete_might_number in delete_shudu_list[process_delete_might_location].might_number_list:
            delete_shudu_list[process_delete_might_location].might_number_list.remove(delete_might_number)
            delete_shudu_list[process_delete_might_location].list_number_count -= 1
    process_delete_might_location = function_number_lie
    # 消除列
    while process_delete_might_location < 81:
        if delete_might_number in delete_shudu_list[process_delete_might_location].might_number_list:
            delete_shudu_list[process_delete_might_location].might_number_list.remove(delete_might_number)
            delete_shudu_list[process_delete_might_location].list_number_count -= 1
        process_delete_might_location += 9
    # 消除3*3
    function_delete_fangge_hang = int(function_number_hang / 3) * 3
    function_delete_fangge_lie = int(function_number_lie / 3) * 3
    for a in range(0, 3):
        for b in range(0, 3):
            process_delete_might_location = (function_delete_fangge_hang + a) * 9 + function_delete_fangge_lie + b
            if delete_might_number in delete_shudu_list[process_delete_might_location].might_number_list:
                delete_shudu_list[process_delete_might_location].might_number_list.remove(delete_might_number)
                delete_shudu_list[process_delete_might_location].list_number_count -= 1


# 赋值函数
def evaluation(evaluation_shudu_list, evaluation_location, evaluation_number):
    evaluation_shudu_list[evaluation_location].number = evaluation_number
    evaluation_shudu_list[evaluation_location].might_number_list.clear()
    evaluation_shudu_list[evaluation_location].list_number_count = 0
    delete_might(evaluation_shudu_list, evaluation_location, evaluation_number)


def eliminate_impossible(function_shudu_list, depth):
    # 这里的flag来判断是否进行了变化
    flag = 1
    while flag == 1:
        flag = 0
        for function_i in range(0, 81):
            if function_shudu_list[function_i].list_number_count == 1:
                flag = 1
                number = function_shudu_list[function_i].might_number_list[0]
                print("在第{}次循环中该格子只有一个值的时候，修改的是第{}个，将值赋值为{}".format(depth, function_i, number))
                evaluation(function_shudu_list, function_i, number)
                # print(function_shudu_list[function_i].number)
        # 3*3方格中只有一个值,或者通过两个同行同列的数来消除备选项的。
        for function_i in range(0, 9):
            might_number_dict = {}
            fangge_hang = int(function_i / 3) * 3
            fangge_lie = function_i % 3 * 3
            # 寻找方格中出现的数的次数
            for a in range(0, 3):
                for b in range(0, 3):
                    j = (fangge_hang + a) * 9 + fangge_lie + b
                    if function_shudu_list[j].list_number_count != 0:
                        for number in function_shudu_list[j].might_number_list:
                            if number in might_number_dict.keys():
                                might_number_dict[number] += 1
                            else:
                                might_number_dict[number] = 1
            for might_number in might_number_dict.keys():
                # 如果有3*3方格中只有一个的出现，那么就去寻找那一个并赋值
                if might_number_dict[might_number] == 1:
                    flag = 1
                    for a in range(0, 3):
                        for b in range(0, 3):
                            j = (fangge_hang + a) * 9 + fangge_lie + b
                            if function_shudu_list[j].list_number_count != 0 and might_number in function_shudu_list[
                                j].might_number_list:
                                number = might_number
                                print("在第{}次循环中，在该3*3范围内只有一个值的时候，修改的是第{}个，将值赋值为{}".format(depth, j, number))
                                evaluation(function_shudu_list, j, number)
                                # print(function_shudu_list[j].number)
                # 利用同行或者同列的效应消除备选项。
                elif might_number_dict[might_number] == 2:
                    j1 = -1
                    j2 = -1
                    is_find_two = 0
                    for a in range(0, 3):
                        for b in range(0, 3):
                            j = (fangge_hang + a) * 9 + fangge_lie + b
                            if function_shudu_list[j].list_number_count != 0 and might_number in function_shudu_list[
                                j].might_number_list:
                                if j1 == -1:
                                    j1 = j
                                else:
                                    j2 = j
                                    is_find_two = 1
                                    break
                        if is_find_two == 1:
                            break
                    #                     找到那两个值后
                    if j2 - j1 < 3:  # 那么就同行
                        number_hang = int(j1 / 9)
                        number = might_number
                        for k in range(number_hang * 9, number_hang * 9 + 9):
                            if k != j1 and k != j2 and number in function_shudu_list[k].might_number_list:
                                print("在第{}次循环中，发现{}和{}在同一行中，值为{}，故将第{}个可能的数字去掉".format(depth, j2, j1,
                                                                                        might_number, k))
                                flag = 1
                                function_shudu_list[k].might_number_list.remove(number)
                                function_shudu_list[k].list_number_count -= 1
                    if (j2 - j1) % 9 == 0:  # 那么就同列
                        number_lie = j1 % 9
                        k = number_lie
                        number = might_number
                        while k < 81:
                            if k != j1 and k != j2 and number in function_shudu_list[k].might_number_list:
                                print("在第{}次循环中，发现{}和{}在同一列中，值为{}，故将第{}个可能的数字去掉".format(depth, j2, j1,
                                                                                        might_number, k))
                                flag = 1
                                function_shudu_list[k].might_number_list.remove(number)
                                function_shudu_list[k].list_number_count -= 1
                            k += 9
    return "完成能做到的变化"


# 对多叉树进行假设的函数。
def provided_shudu(function_shudu_list, depth):
    # 得到含所有可能值的预处理后的数独数组
    eliminate_impossible(function_shudu_list, depth)
    print("第{}次循环中处理完数独".format(depth))
    # 消除结束后还是不行的时候暂时只能考虑进行回溯
    # function_result_shudu_list = []
    # for one in python_shudu_list:
    #     print(one.might_number_list)
    #     function_result_shudu_list.append(one.number)
    # print(function_result_shudu_list)
    # 判断是否完成
    function_full_count = 0
    for function_i in function_shudu_list:
        if function_i.number == 0 and function_i.list_number_count == 0:
            print("发现错误，{}个候选项有{}，值为{}".format(function_i.list_number_count,function_shudu_list.index(function_i),function_i.number))
            return -1
        if function_i.number != 0:
            function_full_count += 1
    print(function_full_count)
    if function_full_count == 81:
        print(function_full_count, "可以走")
        return function_shudu_list
    else:
        for function_i in range(0, 81):
            function_one_shudu_number = function_shudu_list[function_i]
            if function_one_shudu_number.number == 0 and function_one_shudu_number.list_number_count != 0:
                for function_j in range(0, function_one_shudu_number.list_number_count):
                    print(function_j)
                    print("函数有{}条路可以走".format(function_one_shudu_number.list_number_count))
                    print("分别是", function_one_shudu_number.might_number_list)
                    function_one_might_number = function_one_shudu_number.might_number_list[function_j]
                    function_provided_shudu_list = copy.deepcopy(function_shudu_list)
                    # 赋值为一个可能值
                    evaluation(function_provided_shudu_list, function_i, function_one_might_number)
                    A = provided_shudu(function_provided_shudu_list, depth + 1)
                    if A == -1:
                        print("这条路走不通")
                    else:
                        print("此路可以走")
                        return A
                print("两种都不行，返回上一层，如果在最后一行出现，则数独错误")
                return -1


def preprocess(pre_shudu_list):
    for i in range(0, 81):
        number = shudu_list[i]
        if number != 0:
            #         移除那一行，一列，和3*3方格中相同的可能值
            number_hang = int(i / 9)
            for j in range(number_hang * 9, number_hang * 9 + 9):
                if number in pre_shudu_list[j].might_number_list:
                    pre_shudu_list[j].might_number_list.remove(number)
                    pre_shudu_list[j].list_number_count -= 1
            number_lie = i % 9
            j = number_lie
            while j < 81:
                if number in pre_shudu_list[j].might_number_list:
                    pre_shudu_list[j].might_number_list.remove(number)
                    pre_shudu_list[j].list_number_count -= 1
                j += 9
            fangge_hang = int(number_hang / 3) * 3
            fangge_lie = int(number_lie / 3) * 3
            for a in range(0, 3):
                for b in range(0, 3):
                    j = (fangge_hang + a) * 9 + fangge_lie + b
                    try:
                        if number in pre_shudu_list[j].might_number_list:
                            pre_shudu_list[j].might_number_list.remove(number)
                            pre_shudu_list[j].list_number_count -= 1
                    except:
                        exit(0)


def init_deep_shudu(init_shudu_list):
    full_count = 0
    init_python_shudu_list = []
    for i in init_shudu_list:
        shudu_one_number = shudu_number()
        shudu_one_number.number = i
        if i != 0:
            full_count += 1
        else:
            shudu_one_number.might_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            shudu_one_number.list_number_count = 9
        init_python_shudu_list.append(shudu_one_number)
    print(full_count)
    return init_python_shudu_list


if __name__ == '__main__':
    # 初始化的定义
    python_shudu_list = init_deep_shudu(shudu_list)
    # 进行第一步预处理
    preprocess(python_shudu_list)
    result_shudu_list = []
    # 找到两个可能的选择进行唯二性判断，类似于二叉树的结构, 推翻，，，，但是由于情况的复杂性，改为多叉树
    python_shudu_list = provided_shudu(python_shudu_list, 0)
    for one in python_shudu_list:
        result_shudu_list.append(one.number)
    print(result_shudu_list)
