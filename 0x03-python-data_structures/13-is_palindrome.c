#include "lists.h"

int is_palindrome(listint_t **head)
{
    int stack[1024];
    int i = 0;
    listint_t *current, *rev;

    current = *head;
    rev = *head;
    if (head == NULL)
	return (1);

    while(rev && rev->next)
    {
	stack[i++] = current->n;
	rev = rev->next->next;
	current = current->next;
    }

    if (rev)
	current = current->next;

    while (current)
    {
	if (current->n != stack[--i])
	    return (0);
	current = current->next;
    }
    return (1);
}
