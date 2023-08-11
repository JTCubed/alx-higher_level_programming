#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *a, *c;

  a = malloc(sizeof(listint_t));
  if(a == NULL)
    return(NULL);

  a->n = number;
  a->next = NULL;
  c = *head;
  
  if(!head || (*head)->n >= number)
    {
      a->next = *head;
      *head = a;
      return (a);
}
  while (c->next && c->next->n < number)
    {
      c = c->next;
    }

  a->next = c->next;
  c->next = a;

  return(a);
}
