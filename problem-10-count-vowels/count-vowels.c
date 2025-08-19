#include <stdio.h>
int main() {
    #include <ctype.h>
    char s[100]; scanf("%s",s); 
    int c=0; 
    for(int i=0;s[i];i++)
    { 
        char ch=tolower(s[i]);
         if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') c++; } 
         printf("%d",c);
    return 0;
}
