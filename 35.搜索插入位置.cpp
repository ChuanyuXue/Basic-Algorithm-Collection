/*
 * @lc app=leetcode.cn id=35 lang=cpp
 *
 * [35] 搜索插入位置
 */
#include<vector>
#include<iostream>
using namespace std;


// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto left_index=0, right_index = static_cast<int>(nums.size());
        while(left_index < right_index){
            auto half = (right_index - left_index) / 2 + left_index;
            if(nums[half] == target){
                return half;
            }else if(nums[half] > target){
                right_index = half;
            }else{
                left_index = half + 1;
            }
        }
        return left_index;
    }
};
// @lc code=end

int main(){
    auto nums = vector<int> {1,3,5,6};
    Solution a;
    auto result = a.searchInsert(nums, 0);
    cout << result << endl;
    return 0;
}


