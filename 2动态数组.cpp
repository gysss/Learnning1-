//
//  main.cpp
//  2动态数组
//
//  Created by 高源 on 2018/9/18.
//  Copyright © 2018年 高源. All rights reserved.
//

#include <iostream>
using namespace std;
#include <vector>

int main(int argc, const char * argv[]) {
    // 1. initialize
    vector<int> v0;
    vector<int> v1(5, 0);
    // 2. make a copy
    vector<int> v2(v1.begin(), v1.end());
    vector<int> v3(v2);
    // 2. cast an array to a vector
    int a[5] = {0, 1, 2, 3, 4};
    vector<int> v4(a,*(&a+1));
    //3. get length
    cout<<"The size of v4 is: "<<v4.size()<<endl;
    //4. access element
    cout<<"The first element in v4 is :"<<v4[0]<<endl;
    // 5. iterate the vector
    cout<<"[Version 1] The contents of v4 are:";
    for (int i = 0; i<v4.size(); ++i) {
        cout<<" "<<v4[i];
    }
}
