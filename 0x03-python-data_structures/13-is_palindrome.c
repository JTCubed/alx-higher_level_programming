#include "lists.h"

int is_palindrome(listint_t **head)
{
    int i;
    listint_t *current, *rev;

    current = *head;
    rev = *head;
    if (head == NULL)
	return (1);

    while(rev && rev->next)
    {
	rev = rev->next->next;
	current = current->next;
    }
}
