#include "lists.h"

/**
 * check_cycle - check the code
 * @list: list input
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
  listint_t *l, *s;

  if(list == NULL)
    return(0);

  l = list;
  s = list;

  while(l && s)
    {
      l = l-> next;
      s = s->next->next;
      if(l == s)
	return(1);
    }
  return(0);
}
