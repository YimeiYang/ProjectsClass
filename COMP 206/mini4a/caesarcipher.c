/*
 * Program to implement a basic version of Caesar's cipher
 * *******************************************************************
 * *Author		Dept.		Date		Notes
 * *******************************************************************
 * *Yimei Y		Cog.Science.	Feb 15 2020	Initial version.
 * *Yimei Y		Cog.Science.	Feb 16 2020	Added error handling.
 * */
#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
int main(int argc, char *argv[]){
	if(argc != 2){
		puts("Error: usage is caesarcipher <offset>");
		return 1;
	}
	else{
		char *shiftS = argv[1];
		int shiftI = atoi(shiftS);
		char message[100];
		scanf("%[^\r]", message);
		int i;
		char str[100];
		int whatEver;
		for(i=0; message[i] != EOF; i++){
			if(message[i] >= 97 && message[i] <= 122){
				whatEver = message[i]+shiftI;
				if(whatEver > 122){
					whatEver = whatEver - 26;
					str[i] = (char)whatEver;

				}
				else if(whatEver < 'a'){
					whatEver = whatEver + 26;
					str[i] = (char)whatEver;
				}
				else{
					str[i] = (char)whatEver;
				}
			}
			else if(message[i] < 97 || message[i]> 122){
				str[i] = message[i];
			}
		
		}
		str[i+1] = '\0';
		printf("%s", str);
	}
	
}
