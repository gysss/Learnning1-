//给定一个含有 n 个正整数的数组和一个正整数 s ，
// 找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
// 如果不存在符合条件的连续子数组，返回 0。
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int len = nums.size();
        int minlen = len + 1;
        vector<int> sum(len + 1);
        for(int i = 1; i <= len; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        }
        for(int i = 0; i <= len; i++) {
            for(int j = i + 1; j <= len; j++) {
                if(sum[j] - sum[i] >= s) {
                    minlen = min(minlen, j - i);
                    break;
                }
            }
        }
        if(minlen == len + 1)
            return 0;
        return minlen;
    }
};