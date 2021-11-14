/*
 * Program to implement a simple banking application
 * *******i****************************************
 * *Author	Dept.	Date		Notes
 * ****************************************************
 * Yimei Y	Cog.Sci	Mar 4 2020	initial version.
 * Yimei Y	Cog.Sci Mar 9 2020	Added error correction
 * */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//A function to get a specific field
char* getfield(char* line, int num){
	int i;
	int len = strlen(line);
	int count = 0;
        char result[99];
	char* field;
	int index[99];
	//loop through the line to find ",". The field i am looking for is associated with the number of ",".
	for(i = 0; i<len; i++){
		if(line[i] == ','){
			count = count + 1;
			index[count-1] = i;
			int f=0;
			//field 1
			if(count == num && num == 1){
				for(int j = 0; j<i; j++){
					result[j] = line[j];
					f++;
				}
				result[f] = '\0';
			}
			//field 2
			else if(count == num && num==2){
				int a = index[0]+1;
				int tmp = a;
				for(a; a<index[1]; a++){
					result[a-tmp] = line[a];
					f++;					
				}
				result[f] = '\0';
			}
			//field 3
			else if(count == num && num==3){
				int b = index[1]+1;
				int tmp = b;
				for(b; b<index[2]; b++){
					result[b-tmp] = line[b];
					f++;
				}
				result[f] = '\0';
			}
			//field 4
			else if( num==4){
				int c = index[2]+1;
				int tmp = c;
				for(c; c<len; c++){
					result[c-tmp] = line[c];
					f++;
				}
				result[f] = '\0';
			}
		}	
	}
       //return the field	
	field = result;
	return field;
}

//A function to create an account for a new person
int createAccount(int argc, FILE *before, char* statement, char* acctNum, char* Name){
	if(strcmp(statement, "-a") == 0){
		//check number of arguments
                if(argc != 4){
                        fprintf(stderr, "Error, incorrect usage!\n");
                        fprintf(stderr, "-a ACCTNUM NAME\n");
                        return 1;
                }
                else{
                        char line[99];
			//loop through the file to find whether the input person has already had an account or not
                        while(fgets(line,98,before) != NULL){
                                if(strcmp(getfield(line,1), "AC") == 0 && strcmp((getfield(line,2)), acctNum) == 0){
                                        fprintf(stderr, "Error, account number %s already exists.\n", acctNum);
                                        return 50;
                                }
				
			}
			//if no, add an new account
			fprintf(before, "AC,%s,%s\n", acctNum, Name);
		}
	}
	return 0;

}

//An function to deposit money into an pre-existing account
int deposit(int argc, FILE *before, char*statement, char* acctNum, char* Date, char* depositP){
	if(strcmp(statement, "-d") == 0){
		//check number of arguments
		if(argc != 5){
			fprintf(stderr, "Error, incorrect Usage!\n");
			fprintf(stderr, "-d ACCTNUM DATE AMOUNT\n");
			return 1;
		}
		else{
			char line[99];
			int boolean = 1;
			//loop through the file to find whether the input person has already had an account or not
			while(fgets(line,98,before) != NULL){
				if(strcmp((getfield(line,2)), acctNum) == 0){
					boolean = 0;
				}
			}
			//if yes, deposit the money
			if(boolean == 0){
				fprintf(before, "TX,%s,%s,%s\n", acctNum, Date, depositP);
				return 0;
			}
			// if no, give an error.
			else{
				fprintf(stderr, "Error, account number %s does not exists.\n", acctNum);
				return 50;
			}
		}

	}
}

//An function to withdrawal money from an pre-existing account
int withdrawal(int argc, FILE *before, char* statement, char* acctNum, char* Date, char* withdrl){
	if(strcmp(statement, "-w") == 0){
		//check number of arguments
		if(argc != 5){
			fprintf(stderr, "Error, incorrect usage!\n");
			fprintf(stderr, "-w ACCTNUM DATE AMOUNT\n");
			return 1;
		}
		else{
			char line[99];
			float balance = 0.00;
			float withd = atof(withdrl);
			int count = 0;
			//loop through the file to find whether the input person has already had an account or not and calculate the overall money in that account
			while(fgets(line,98,before) != NULL){
				if(strcmp((getfield(line,2)), acctNum) == 0){
					if(strcmp((getfield(line,1)), "TX") == 0){
						float transaction = atof(getfield(line,4));
						balance = balance + transaction;
						count = count + 1;
					}
					else{
						count = count + 1;
					}
				}
			}
			//if there is no account, give an error
			if(count == 0){
				fprintf(stderr, "Error, account number %s does not exists.\n", acctNum);
				return 50;
			}
			//if there is not enough money from the account to withdrawal, give an error
			if(balance - withd < 0){
				fprintf(stderr, "Error, acctoun number %s has only %.2f.\n", acctNum, balance);
				return 60;
			}
			//if both conditions are met, withdrawal the money
			else{
				fprintf(before, "TX,%s,%s,-%s\n", acctNum, Date, withdrl);
				return 0;
			}
		}
	}		
}

int main(int argc, char* argv[]){
	//check number of arguments
	if(argc == 1){
		fprintf(stderr, "Error, incorrect usage!\n");
		fprintf(stderr, "-a ACCTNUM NAME\n");
		fprintf(stderr, "-d ACCTNUM DATE AMOUNT\n");
		fprintf(stderr, "-w ACCTNUM DATE AMOUNT\n");
		return 1;
	}
	char* statement = argv[1];
	char* acctNum = argv[2];
	//open the file
	FILE *before = fopen("bankdata.csv", "r+");
	//if the file does not exist, give an error
	if(before == NULL){
		fprintf(stderr, "Error, unable to locate the data file bankdata.csv\n");
		return 100;
	}
	//if the switch is "-a", create an account
	if(strcmp(statement, "-a") == 0){
		char* Name = argv[3];
		int code = createAccount(argc, before, statement, acctNum, Name);
		return code;
	}
	//if the switch is "-d", deposit the money.
	if(strcmp(statement, "-d") == 0){
		char* Date = argv[3];
		char* depositP = argv[4];
		int code = deposit(argc, before, statement, acctNum, Date, depositP);
		return code;
	}
	//if the switch is "-w", withdrawal the money.
	if(strcmp(statement, "-w") == 0){
		char* Date = argv[3];
		char* withdrl = argv[4];
		int code = withdrawal(argc, before, statement, acctNum, Date, withdrl);
		return code;
	}

}
