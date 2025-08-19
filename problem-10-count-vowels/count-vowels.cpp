#include <bits/stdc++.h>
using namespace std;
int main() {
    string s; cin>>s; 
    int c=0; for(char ch:s)\
    { 
        ch=tolower(ch); 
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') c++; 
    
    } cout<<c;
    return 0;
}
