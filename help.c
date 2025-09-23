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
#include "help.h"

void print_help(){
    printf("Error: Missing arguments.\n");
    printf("Seven argument are required:\n");
    printf("Example: ./labolsa <name> <companies> <users> <orders> <stock_value> <n_stocks> <cash> <max_iter>\n");
    printf("Where:\n");
    printf("name [max 8 characters]: Market code.\n");
    printf("companies [integer]: Number of Publicly Trades Companies in the Market.\n");
    printf("users [integer]: Number dof clientes in the Market.\n");
    printf("ordes [integer]: Number of orders allowed in the market by cycle.\n");
    printf("stock_value [float]: Individual price for each stock.\n");
    printf("n_stocks [integer]: Number of stocks maximum for each company.\n");
    printf("cash [float]: Initial cash for each user.\n");
    printf("max_iter [integer]: Number of iterations .\n");
}
