#include "lists.h"

int check_cycle(listint_t *list)
{
    if(list->next) return 1;
    return 0;
}