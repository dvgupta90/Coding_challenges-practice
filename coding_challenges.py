"""1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if item + item2 == target:
                    return [i,i2]

################# method 2 using dict ########################################

    

    def twoSum(self, nums, target):

        complement_num_dict = {}
            
        for i in range(len(nums)):
            if nums[i] in complement_num_dict: #checking if num in given list is also in dict keys
                return [complement_num_dict[nums[i]],i]
            else:
                complement_num_dict[target - nums[i]] = i



#2. Reverse a string using STACK

def revstring(string):

    from pythonds.basic.stack import Stack
    new_stack = Stack()
    rev_string = ""

    for char in string:
        new_stack.push(char)

    while not new_stack.is_empty():
        rev_string = rev_string + new_stack.pop()

    return rev_string
    


#3. Convert Decimal to Binary using Stack
def conv_binary(decimal_num):
    from pythonds.basic.stack import Stack
    new_stack = Stack()
    binary_num = ""

    while decimal_num is > 0:
        remainder = decimal_num%2
        new_stack.push(remainder)
        decimal_num = decimal_num//2

    while not new_stack.is_empty():
        binary_num = binary_num + str(new_stack.pop())

    return binary_num       



                    
