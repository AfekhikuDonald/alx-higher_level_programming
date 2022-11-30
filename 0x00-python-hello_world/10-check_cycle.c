#include "lists.h"


/**
 * check_cycle - checks if a linked list has a cycle
 * @list: the list to check
 * Return: 0 if there is no cycle else return 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);
	head = list;
	tail = list;
	while (head && tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;
		if (head == tail)
			return (1);
	}
	return (0);
}
