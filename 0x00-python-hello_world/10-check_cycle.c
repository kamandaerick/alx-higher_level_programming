#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly-linked list has a cycle
 * @list: the singly-linked list
 * Return: Returns 0 if no cycle and 1 of there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
