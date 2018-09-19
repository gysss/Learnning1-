
/*在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1*/
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int max = -1;
        int index = -1;
        for(int i = 0;i<nums.size();i++)
        {
            if(max<nums[i]) {
                max = nums[i];
                index = i;
            }
        }
        for(int i=0;i<index;i++){
            if(max<2*nums[i]) return -1;
        }
        for(int i = index+1;i<nums.size();i++){
            if(max<2*nums[i]) return -1;
        }
        return index;
    }
};