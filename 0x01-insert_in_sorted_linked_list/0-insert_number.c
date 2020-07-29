#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert - insert node at start of list
 * @head: pointer to head of list
 * @n: value of the new node
 *
 * Return: pointer to new node
 */

 listint_t *insert_node(listint_t **head, int number){
    listint_t *current;
    listint_t *new;
    unsigned int n; /* number of nodes */

    if (!head)
		return (NULL);

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;

    if (*head == NULL) { 
        *head = new;
        new->next = NULL;
        return (new);
    }

    if (current->next == NULL) {
        current->next = new;
        new->next = NULL;
    }
    else {
        while (current->next != NULL) {
            if (current->n <= number ) {
                current = current->next;
            } else {
            current->preview = new;
            new->next = current;
        }
    }
    return (new);
 }