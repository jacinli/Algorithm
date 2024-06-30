from typing import List

# 思路： 通过map 来进行查找
# 建一个map, 从头遍历list，将这个list转换为map<value,index>, 然后直接遍历map,对target - map[i]进行查找
# 需要注意的点：

#  从头遍历数组，然后在map查找，找到map<target - nums[i]>的值，然后返回这两个值的index,如果找不到就插入到map中


def twoSum(nums: List[int], target: int) -> List[int]:
    mapa = {}
    for i in range(len(nums)):
        if target - nums[i] in mapa:
            return [mapa[target - nums[i]], i]
        else:
            mapa[nums[i]] = i
    return []


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))
