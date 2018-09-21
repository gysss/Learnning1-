/*在杨辉三角中，每个数是它左上方和右上方的数的和。*/

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> v(numRows);
        if(numRows == 0) return v;
        for(int i=0;i<numRows;i++){
            v[i].resize(i+1);
        }
        v[0][0] = 1;
        if(numRows == 1) return v;
        v[1][0] = 1;
        v[1][1] = 1;
        for(int i=2;i<numRows;i++){
            v[i][0] = 1;
            v[i][i] = 1;
        }
        for(int i=2;i<numRows;i++){
            for(int j = 1;j<i;j++){
                v[i][j] = v[i-1][j-1] + v[i-1][j];
            }
        }
        return v;
    }
};