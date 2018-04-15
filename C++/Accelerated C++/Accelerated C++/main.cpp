//  Accelerated C++
//
//  Created by newbiejasper on 2017/12/25.
//  Copyright © 2017年 newbiejasper. All rights reserved.

//第0章

//注释只能是一行
/* 这个注释可以使多行，结束*/

#include <iostream> //请求使用所指定的标准库iostream,输入输出流
#include <string>

//main函数是C++程序运行时，被调用来相应请求的函数
int main() {
    // 花括号里是主函数语句
    
    //std是标准库iostreamm里的名称空间
    //std::cout指标准输出流，实现程序输出
    //std::endl输出语句行的结束
    std::cout << "请输入你的名字：";
    
    std::string name;
    std::cin >> name;
    
    std::cout << "hello," << name << "!" << std::endl;
    //返回值为0，代表运行成功
    return 0;
}
