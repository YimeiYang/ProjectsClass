/*
 * Main program to receive the input and construct a polynomial
 * ****************************************************************
 * *Author	Dept.	Date		NOTES
 * ***************************************************************
 * Yimei Y.	Cog.Sci	Apr 13 2020	initial version
 * yimei Y.	Cog.Sci	Apr 14 2020	error correction
 * */
#include "utils.h"
#include "poly.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	//check number of arguments
	if(argc != 2){
		fprintf(stderr, "Error, there should be 1 argument\n");
		return -1;
	}
	//open the file
	char* filename = argv[1];
	FILE *file = fopen(filename, "r");
	//if can't find the file, return 100
	if(file == NULL){
		fprintf(stderr, "Error, unable to locate the data file %s\n", filename);
		return 100;
	}
	//loop through the file to get
	int* co;
	int* ex;	
	char line[99];
	while(fgets(line,98,file) != NULL){
		parse(line, &co, &ex);
		addPolyTerm(*co, *ex);	
	}
	sortList(head);
	displayPolynomial();
	int a = evaluatePolynomial(-2);
	int b = evaluatePolynomial(-1);
	int c = evaluatePolynomial(0);
	int d = evaluatePolynomial(1);
	int e = evaluatePolynomial(2);
	printf("for x=-2, y=%d\n", a);
	printf("for x=-1, y=%d\n", b);
	printf("for x=0, y=%d\n", c);
	printf("for x=1, y=%d\n", d);
	printf("for x=2, y=%d\n", e);
	return 0;
}	

