#include <iostream>
using namespace std;
#define size 10
struct stackexp
{
 int top=-1;
 char stk[size];
}s;
void push(char x)
{
 s.top=s.top+1;
 s.stk[s.top]=x;
}
char pop()
{
 char c;
 c=s.stk[s.top];
 s.top=s.top-1;
 return c;
}
int isfull()
{
 if(s.top==size)
 return 1;
 else
 return 0;
}
int isempty()
{
 if(s.top==-1)
 return 1;
 else
 return 0;
}
int main()
{
 char exp[20],ch;
int i=0;

 cout << "\n\t!! Parenthesis Checker..!!!!" << endl; // prints !!!Hello World!!!

 cout<<"\nEnter the expression to check whether it is in well form or not : ";

 cin>>exp;

 if((exp[0]==')')||(exp[0]==']')||(exp[0]=='}'))

 {

 cout<<"\n Invalid Expression.....\n";

 return 0;

 }

 else

 {

 while(exp[i]!='\0')

 {

 ch=exp[i];

 switch(ch)

 {

 case '(':push(ch);break;

 case '[':push(ch);break;

 case '{':push(ch);break;

 case ')':pop();break;

 case ']':pop();break;

 case '}':pop();break;

 }

 i=i+1;

 }

 }

 if(isempty())

 {

 cout<<"\nExpression is well parenthesised...\n";

 }

 else

 {

 cout<<"\nSorry !!! Invalid Expression or not in well parenthesized....\n";

 }

 return 0;

}
