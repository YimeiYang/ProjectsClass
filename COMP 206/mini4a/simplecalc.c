/*
 * Program to implement a simple calculator 
 * **********************************************************
 * * Author	Dept.		Date		Notes
 * **********************************************************	
 * * Yimei Y	Cog. Science.	Feb 12 2020	Initial version.
 * * Yimei Y    Cog. Science.   Feb 15 2020     Added error handling.
 * */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	if(argc != 4){
		puts("Error: usage is simplecalc <x> <op> <y>");
		return 1;
	}
	else{
		int a, x, y, z;
		char *firC = argv[1];
		char *secC = argv[3];
		char ope = argv[2][0];
		int firI = atoi(firC);
		int secI = atoi(secC);

		switch(ope){
			case 45:
				x = firI-secI;
				printf("%d\n", x);
				return 0;
				break;
			case 43:
				y = firI+secI;
				printf("%d\n", y);
				return 0;
				break;
			case 42:
				z = firI*secI;
				printf("%d\n", z); 
				return 0;
				break;
			case 47:
				a = firI/secI;
				printf("%d\n", a);
				return 0;
				break;
			default:
				printf("%c is not a valid operator.\n", ope);
				return 2;
				break;
		}
	}		
}


