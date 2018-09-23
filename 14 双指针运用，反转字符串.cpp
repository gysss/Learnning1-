//编写一个函数，其作用是将输入的字符串反转过来。

class Solution {
public:
    string reverseString(string s) {
        int i = 0;
        int j = s.length()-1;
        while(i<j){
            swap(s[i],s[j]);
            i++;
            j--;
        }
        return s;
    }
};