//
//  main.cpp
//  数组与字符串
//
//  Created by 高源 on 2018/9/18.
//  Copyright © 2018年 高源. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // Initialize
    int a0[5];
    int a1[5] = {1, 2, 3};
    // Get Length
    int size = sizeof(a1) / sizeof(*a1);
    cout<<"The size of a1 is: "<<size<<endl;
    // Acess Element
    cout<<"The first element is: "<<a1[0]<<endl;
    // Iterate all element
    cout<<"[Version 1] The contents of a1 are:";
    for (int i=0; i<size; ++i) {
        cout<<" "<<a1[i];
    }
    cout<<endl;
    cout<<"[Version 2] The contents of a1 are:";
    for(int &item: a1) {
        cout<<" "<<item;
    }
}
