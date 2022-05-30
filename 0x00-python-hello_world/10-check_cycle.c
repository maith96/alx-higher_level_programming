#include "lists.h"
/**
*check_cycle - Checks whether a linked list has cycle
*@list: linked list
*Return: 0 if has no cycle and 1 otherwise
*/
int check_cycle(listint_t *list)
{
    if(list->next) return (1);
    return(0);
}