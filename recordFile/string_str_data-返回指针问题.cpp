#include <iostream>
#include <string>
#include <cstring>
using namespace std;


char* fun(char* chr){
    string str2 = "abcd";
    cout << ":::" << str2 << endl;
    //return const_cast<char*> (str2.c_str());
    char ch[5];
    strcpy(chr, str2.c_str());
    //ch[5] = '\0';
    return chr;
}
int main()
{
   string str = "123456";
   cout << "c_str:" << str.c_str() ;
   cout << "data :" << str.data();
   cout << "size:" << str.size() << endl;
   
   char* chr = const_cast<char*> (str.c_str());
   cout << "size..." << strlen(chr) << endl << endl;
   //fun(const_cast<char*>(str.c_str()));
   //fun(chr);
   //chr[0] = 'a';
   //fun(chr);
   
   //char* rch = fun(nullptr);
   //rch[1] = '1';
   //rch[4] ='\0';
   //cout << ".........." << rch << endl;
   
   cout << endl;
   char ch[5];
   char* rrch = fun(ch);
   cout << "$$$$$$$$$$$$$$ " << rrch << endl;
   return 0;
}

