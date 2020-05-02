# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:20:08 2020

@author: mahesh
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_sll:
    def __init__(self):
        self.head = None
        self.last = None


    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.last = self.head
        else:
            cur_node = self.head
            last_node = self.last
            new_node.next = cur_node
            last_node.next = new_node
            self.head = new_node


    def insert(self, prev_node, data):
        insert_status = False
        if self.head is not None:
            new_node = Node(data)
            cur_node = self.head
            while True:
                if cur_node.data == prev_node:
                    new_node.next = cur_node.next
                    cur_node.next = new_node
                    insert_status = True
                    break

                cur_node = cur_node.next
                if cur_node == self.head:
                    break

        return insert_status


    def delete(self, key):
        del_status = False
        if self.head is not None:
            cur_node = self.head
            last_node = self.last
            count = self.count()
            if cur_node.data == key:
                if count == 1:
                    self.head = None
                    self.last = None
                else:
                    self.head = cur_node.next
                    last_node.next = self.head
                    cur_node = None

                del_status = True
            else:
                while True:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    if cur_node.data == key:
                        prev_node.next = cur_node.next
                        cur_node = None
                        del_status = True
                        break

                    if cur_node.next == self.head:
                        break

        return del_status


    def display(self):
        if self.head is not None:
            ll = []
            cur_node = self.head
            while True:
                e = cur_node.data
                ll.append(e)
                cur_node = cur_node.next
                if cur_node == self.head:
                    break
            
            print(ll)
        else:
            print('[List is empty]')


    def count(self):
        count = 0
        if self.head is not None:
            cur_node = self.head
            while True:
                count += 1
                cur_node = cur_node.next
                if cur_node == self.head:
                    break

        return count


if __name__ == "__main__":
    cll = Circular_sll()
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
                cll.push(e)

            print('All element(s) added to the list!')
            cll.display()
            print('----------------------------------------\n')
        elif choice == 2:
            print('\n----------------------------------------')
            if cll.count() > 0:
                cll.display()
                data = input('Enter data to be inserted: ')
                prev_node = input('After element: ')
                data_inserted = cll.insert(prev_node, data)
                if data_inserted:
                    print('Data has been addedd to the list.')
                    cll.display()
                else:
                    print(f'{prev_node} is not in the list, try again.')
            else:
                print('List is empty, try again after adding some data.')

            print('----------------------------------------\n')
        elif choice == 3:
            print('\n----------------------------------------')
            if cll.count() > 0:
                cll.display()
                data = input('Enter data to be deleted: ')
                data_deleted = cll.delete(data)
                if data_deleted:
                    print('Data has been deleted.')
                    cll.display()
                else:
                    print(f'Element {data} is not in the list. Try again.')
            else:
                print('List is empty, try again after adding some data.')

            print('----------------------------------------\n')
        elif choice == 4:
            print('\n----------------------------------------')
            count = cll.count()
            print(f'Total no of element(s) in list: {count}')
            print('----------------------------------------\n')
        elif choice == 5:
            break
        else:
            print('\nEnter correct choice no.\n')