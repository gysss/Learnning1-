#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	string s1 = "Hello World";
	cout<<"s1 is \"Hello World\""<<endl;
	string s2 = s1;
	cout<<"s2 is initialized by s1"<<endl;
	string s3(s1);
	cout<<"s3 is initialized by s1"<<endl;

	cout<<"Compared by '==':"<<endl;
	cout<<"s1 and \"Hello World\":"<<(s1 == "Hello World")<<endl;
	cout<<"s1 and s2:"<<(s1 == s2)<<endl;
	cout<<"s1 and s3:"<<(s1 == s3)<<endl;

	cout<<"Compared by 'compare':"<<endl;
	cout<<"s1 and \"Hello World\":"<<!s1.compare("Hello World")<<endl;
	cout<<"s1 and s2:"<<!s1.compare(s2)<<endl;
	cout<<"s1 and s3:"<<!s1.compare(s3)<<endl;

	s1[5] = ',';
	cout<<s1<<endl;
	s1+="!";
	cout<<s1<<endl;
	cout<<"The position of first 'o' is:"<<s1.find('o')<<endl;
	cout<<"The position of last 'o' is:"<<s1.rfind('o')<<endl;
	cout<<s1.substr(6,5)<<endl;
	return 0;
}