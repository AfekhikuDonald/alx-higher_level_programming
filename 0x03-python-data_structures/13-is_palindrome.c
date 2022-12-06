#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
list_len - finds the lenght of a string
@list: list to be checked
@Return: lenght
*/
size_t list_len(listint_t *list)
{
	size_t i = 0;

	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		i++;
		list = list->next;
	}
	return (i);
}


/**
is_palindrome - checks if a singly linked list is palindrome
@head: linked list
@Return: 0 if not a palindromw else 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *arr, j, k, i;

	temp = *head;
	k = list_len(temp);
	arr = (int *) malloc(sizeof(int) * k);
	if (arr == NULL)
		return (2);
	i = 0;
	while (temp != NULL)
	{
		arr[i] = temp->n;
		i++;
		temp = temp->next;
	}
	for (j = 0, i = k - 1; j < i; j++, i--)
	{
		if (arr[j] != arr[i])
		{
			return (0);
		}
	return (1);
}
