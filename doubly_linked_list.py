# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:20:08 2020

@author: mahesh
"""


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Doubly_linked_list:
    def __init__(self):
        self.head = None


    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
           cur = self.head
           cur.prev = new_node
           self.head = new_node
           new_node.next = cur


    def insert(self, prev_node, data):
        insert_status = False
        if self.head != None:
            new_node = Node(data)
            cur_node = self.head
            count = self.count()
            while count != 0:
                if cur_node.data == prev_node:
                    if count == 1:
                        new_node.prev = cur_node
                        cur_node.next = new_node
                    else:
                        new_node.next = cur_node.next
                        new_node.prev = cur_node
                        cur_node.next.prev = new_node
                        cur_node.next = new_node

                    insert_status = True
                    break

                cur_node = cur_node.next
                count -= 1

        return insert_status


    def delete(self, key):
        del_status = False
        if self.head != None:
            cur_node = self.head
            count = self.count()
            while count != 0:
                if cur_node.data == key:
                    if cur_node == self.head:
                        self.head = cur_node.next
                        cur_node = None
                    elif cur_node.next == None:
                        cur_node.prev.next = None
                        cur_node = None
                    else:
                        cur_node.prev.next = cur_node.next
                        cur_node.next.prev = cur_node.prev
                        cur_node = None

                    del_status = True
                    break

                cur_node = cur_node.next
                count -= 1

        return del_status


    def display(self):
        if self.head is not None:
            ll = []
            cur_node = self.head
            while cur_node != None:
                ll.append(cur_node.data)
                cur_node = cur_node.next

            print(ll)
        else:
            print('[List is empty]')


    def count(self):
        ll_len = 0
        cur_node = self.head
        while cur_node != None:
            ll_len += 1
            cur_node = cur_node.next

        return ll_len


if __name__ == "__main__":
    dll = Doubly_linked_list()
    while True:
        choice = int(input('''1. Add element(s) to list
2. Insert element after
3. Delete
4. Count
5. Exit
Enter your choose: '''))

        if choice == 1:
            print('\n----------------------------------------')
            arr_len = int(input('How many element(s) want to add: '))
            arr = []
            for i in range(arr_len):
                e = input(f'Enter element {i}: ')
                arr.append(e)

            for e in arr:
                dll.push(e)

            print('All element(s) added to the list!')
            dll.display()
            print('----------------------------------------\n')
        elif choice == 2:
            print('\n----------------------------------------')
            if dll.count() > 0:
                dll.display()
                data = input('Enter data to be inserted: ')
                prev_node = input('After element: ')
                data_inserted = dll.insert(prev_node, data)
                if data_inserted:
                    print('Data has been added.')
                    dll.display()
                else:
                    print(f'Element {prev_node} is not in the list. Try again!')
            else:
                print('List is empty, try again after adding some data.')

            print('----------------------------------------\n')
        elif choice == 3:
            print('\n----------------------------------------')
            if dll.count() > 0:
                dll.display()
                data = input('Enter data to be deleted: ')
                data_deleted = dll.delete(data)
                if data_deleted:
                    print('Data has been deleted.')
                    dll.display()
                else:
                    print(f'Element {data} is not in the list. Try again')
            else:
                print('List is empty, try again after adding some data.')

            print('----------------------------------------\n')
        elif choice == 4:
            print('\n----------------------------------------')
            count = dll.count()
            print(f'Total no of elements in list: {count}')
            print('----------------------------------------\n')
        elif choice == 5:
            break
        else:
            print('\nWrong choice. Try again.\n')