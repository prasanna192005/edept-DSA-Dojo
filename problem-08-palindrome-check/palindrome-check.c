#include <stdio.h>
int main() {
    #include <string.h>
    char s[100]; 
    scanf("%s",s); 
    int i=0,j=strlen(s)-1,ok=1; 
    while(i<j){ if(s[i++]!=s[j--]) ok=0; } 
    printf(ok?"Yes":"No");
    return 0;
}
