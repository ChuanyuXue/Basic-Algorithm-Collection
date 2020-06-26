/*
 * @lc app=leetcode.cn id=32 lang=cpp
 *
 * [32] 最长有效括号
 */
#include<string>
#include<vector>
#include<iostream>
using namespace std;

// @lc code=start
// class Solution {
// public:
//     int longestValidParentheses(string s) {
//         if(s.length() == 0){
//             return 0;
//         }
//         vector<int> dp(s.length(), 0);
        
//         int max_val = 0;
//         for(int i=1; i != s.length(); i++){
//             if(s[i] == ')'){
//                 if(s[i-1] == '('){
//                     dp[i] = 2;
//                     if(i - 2 >= 0){
//                         dp[i] = dp[i - 2] + dp[i];
//                     }
//                 }else if(s[i - dp[i-1] - 1] == '('){
//                     dp[i] = dp[i - 1] + 2;
//                     if(i - dp[i - 1] - 2 >= 0){
//                         dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2];
//                     }   
//                 }
            
//                 if(dp[i] > max_val){
//                     max_val = dp[i];
//                 }
//             }
//         }
//         return max_val;
//     }
// };

class Solution {
public:
    int longestValidParentheses(string s) {
        int size = s.length();
        vector<int> dp(size, 0);

        int maxVal = 0;
        for(int i = 1; i < size; i++) {
            if (s[i] == ')') {
                if (s[i - 1] == '(') {
                    dp[i] = 2;
                    if (i - 2 >= 0) {
                        dp[i] = dp[i] + dp[i - 2];
                    }
                } else if (dp[i - 1] > 0) {
                    if ((i - dp[i - 1] - 1) >= 0 && s[i - dp[i - 1] - 1] == '(') {
                        dp[i] = dp[i - 1] + 2;
                        if ((i - dp[i - 1] - 2) >= 0) {
                            dp[i] = dp[i] + dp[i - dp[i - 1] - 2];
                        }
                    }
                }
            }
            maxVal = max(maxVal, dp[i]);
        }
        return maxVal;
    }
};

// @lc code=end

int main(){
    auto a = Solution();
    string input_val = ")()())";
    auto result = a.longestValidParentheses(input_val);
    cout << result << endl;
    return 0;
}