num1,num2 = int(input()),int(input()) # i'm t@king the two inputs needed for the problem.
# cre@ting @ function n@med power sum
def power_sum(num,count,total,pair_count):
    """

    :param num: number for which you w@nt to find the answer
    :param count:
    :param total:
    :param pair_count:
    :return:
    """

    powered_num = num**num2
    if powered_num==total:
        return pair_count+1
    if powered_num < total:
        return power_sum(num+1,count-1,total-powered_num,pair_count) + power_sum(num+1,count,total,pair_count)
    return pair_count
limit=(num1**(1/float(num2)))
print(power_sum(1,limit,num1,0))