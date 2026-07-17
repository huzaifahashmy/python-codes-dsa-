#include <iostream>
using namespace std;

// =========================
// Node Definition
// =========================

class Node
{
public:
    int data;
    Node *next;

    Node(int value)
    {
        data = value;
        next = nullptr;
    }
};

// =========================
// Print Linked List
// =========================

void printList(Node *head)
{
    Node *temp = head;

    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }

    cout << "NULL" << endl;
}

// =========================
// Insert at Beginning
// =========================

void insertAtBeginning(Node *&head, int value)
{
    Node *newNode = new Node(value);

    newNode->next = head;
    head = newNode;
}

// =========================
// Insert at End
// =========================

void insertAtEnd(Node *&head, int value)
{
    Node *newNode = new Node(value);

    if (head == nullptr)
    {
        head = newNode;
        return;
    }

    Node *temp = head;

    while (temp->next != nullptr)
    {
        temp = temp->next;
    }

    temp->next = newNode;
}

// =========================
// Delete First Node
// =========================

void deleteBeginning(Node *&head)
{
    if (head == nullptr)
        return;

    Node *temp = head;

    head = head->next;

    delete temp;
}

// =========================
// Delete Last Node
// =========================

void deleteEnd(Node *&head)
{
    if (head == nullptr)
        return;

    if (head->next == nullptr)
    {
        delete head;
        head = nullptr;
        return;
    }

    Node *temp = head;

    while (temp->next->next != nullptr)
    {
        temp = temp->next;
    }

    delete temp->next;

    temp->next = nullptr;
}

// =========================
// Search
// =========================

bool search(Node *head, int key)
{
    Node *temp = head;

    while (temp != nullptr)
    {
        if (temp->data == key)
            return true;

        temp = temp->next;
    }

    return false;
}

// =========================
// Count Nodes
// =========================

int countNodes(Node *head)
{
    int count = 0;

    Node *temp = head;

    while (temp != nullptr)
    {
        count++;
        temp = temp->next;
    }

    return count;
}

// =========================
// Reverse Linked List
// =========================

void reverseList(Node *&head)
{
    Node *prev = nullptr;
    Node *curr = head;
    Node *next = nullptr;

    while (curr != nullptr)
    {
        next = curr->next;

        curr->next = prev;

        prev = curr;

        curr = next;
    }

    head = prev;
}

// =========================
// Main Function
// =========================

int main()
{
    Node *head = nullptr;

    // Insert at End
    insertAtEnd(head, 10);
    insertAtEnd(head, 20);
    insertAtEnd(head, 30);

    cout << "Initial List:" << endl;
    printList(head);

    // Insert at Beginning
    insertAtBeginning(head, 5);

    cout << "\nAfter inserting at beginning:" << endl;
    printList(head);

    // Insert at End
    insertAtEnd(head, 40);

    cout << "\nAfter inserting at end:" << endl;
    printList(head);

    // Search
    cout << "\nSearching for 20: ";

    if (search(head, 20))
        cout << "Found" << endl;
    else
        cout << "Not Found" << endl;

    // Count Nodes
    cout << "\nNumber of nodes: "
         << countNodes(head)
         << endl;

    // Delete Beginning
    deleteBeginning(head);

    cout << "\nAfter deleting first node:" << endl;
    printList(head);

    // Delete End
    deleteEnd(head);

    cout << "\nAfter deleting last node:" << endl;
    printList(head);

    // Reverse
    reverseList(head);

    cout << "\nAfter reversing:" << endl;
    printList(head);

    return 0;
}