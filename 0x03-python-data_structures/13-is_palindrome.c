#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

listint_t *reverse(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse - reverse a linked list
 * @head: head of list to rev
 * Return: reversed list
 */

listint_t *reverse(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return(*head);
}

/**
 * is_palindrome - check if a list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if true 0 if false
 */

int is_palindrome(listint_t **head){
	int size = 0, i;
	listint_t *copy, *rev, *mid, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	copy = *head;
	while (copy)
	{
		size++;
		copy = copy->next;
	}
	copy = *head;

	mid = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		mid = mid->next;

	if ((size % 2) == 0 && mid->n != mid->next->n)
		return (0);

	mid = mid->next->next;
	rev = reverse(&mid);
	tmp = rev;

	while (rev)
	{
		if (copy->n != rev->n)
			return (0);;
		copy = copy->next;
		rev = rev->next;
	}
	reverse(&tmp);

	return (1);
}
