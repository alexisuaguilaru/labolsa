/**
    <labolsa> Montecarlo model of market stocks
    Copyright (C) 2024  Victor De la Luz 
                        <vdelaluz@enesmorelia.unam.mx>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

VERSION Beta (10/22/2024)
**/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "help.h"
#include "user.h"
#include "stock.h"
#include "market.h"
#include "engine.h"
#include "order.h"
#include "common.h"

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1
#define EX_USAGE 64

// NOTE: The user not update the price of the order after the first execution. We need to create a new function to ask to the user if wants to update price after each execution ends.

int main(int argn, char **argv){
  User *user;
  Stock *stock;
  Market *market;
  char code[8];
  int i,j,k,n,N,M,P;
  int n_stocks_by_number;
  float stock_value , cash_for_each_user , memory_used;
  
  //printf("%i\n",argn);
  if (argn == 8){
    if (sscanf(argv[2],"%i", &M) <= 0){print_help();return EX_USAGE;};
    if (sscanf(argv[3],"%i", &N) <= 0){print_help();return EX_USAGE;};
    if (sscanf(argv[4],"%i", &P) <= 0){print_help();return EX_USAGE;};
    if (sscanf(argv[5],"%f",&stock_value) <= 0){print_help();return EX_USAGE;}
    if (sscanf(argv[6],"%i",&n_stocks_by_number) <= 0){print_help();return EX_USAGE;}
    if (sscanf(argv[7],"%f",&cash_for_each_user) <= 0){print_help();return EX_USAGE;}
    if (strlen(argv[1]) > 8){print_help();return EX_USAGE;}
    market = newMarket(argv[1],M,N,P);
    //user = malloc(sizeof(User)*N);
    //stock = malloc(sizeof(Stock)*M);
    printf("%i\n",M);    
    printf("#Labolsa simulator ver 20240909_1105\n");
    printf("# GNU/GPL License\n");
    printf("# By: Victor De la Luz <vdelaluz@enesmorelia.unam.mx>\n");
    // Creating stocks
    printf("#Generating %i companies... ",M);
    for(i=0; i < M; i++){
      sprintf(code,"%s%i",argv[1],i);
      addStock(market,newStock(code,stock_value,n_stocks_by_number));      
      //stock[i] = newStock(code,100.0);
    }
    printf("#Ready!\n");
     
    printf("#Generating %i users... ",N);
    for(i=0; i < N; i++){
      addUser(market,newUser(i,cash_for_each_user));
    }
    printf("#Ready!\n");
     //printf("%s:%f\n",stock[0].code,stock[0].price);
    memory_used = (float)(sizeof(User)*N+sizeof(Stock)*M)/1e6; 
    printf("#Memory used: %f Mb \n",memory_used);
    //print_divergence(market);
    // create the OPIs of our model. We create a random asignator of OPIS for all the users.
    srand(time(NULL));
    k=0;
    printf("#Computing IOPs...\n");
    do{
      for(int i=0; i < market->index_user;i++){
	j = (int)randomValue(0.0, (float)market->index_stock);
	  n = (int)((market->users[i].money/market->stocks[j].price)*randomValue(0.0, 1.0));
	  //printf("INFO: n= %i\n",n);
	  if (n < 1) n = 1;
	  //printf("INFO1:%s\n",market->stocks[j].code);
	buy_OPI(&market->stocks[j],&market->users[i],n,market->stocks[j].price);
      }
      k++;

      //printMarket(market);
      
    }while(remain_stocks(*market) > 0);

    printf("#IOPs iterations: %i\n",k);
    //print_divergence(market);
    //printMarket(market);

    printf("#Running Montecarlo...\n");
    for(int i=0; i < 1000; i++){
      printf("#%i:",i);
      montecarlo(market);
      printJapaneseCandle(market);
      //printOrders(market);
      //printMarket(market);
      //print_divergence(market);
    }
    
    //printMarket(market);
    print_divergence(market);
    //free(user);
    //free(stock);
    closeMarket(market);
  }else{
    print_help();
    EX_USAGE;
  }
  return EXIT_SUCCESS;
}
