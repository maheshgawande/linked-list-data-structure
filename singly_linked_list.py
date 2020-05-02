# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:20:08 2020

@author: mahesh
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single_linked_list:
    def __init__(self):
        self.head = None


    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur_node = self.head
            new_node.next = cur_node
            self.head = new_node
            cur_node = None


    def insert(self, prev_node, data):
        insert_status = False
        if self.head != None:
            new_node = Node(data)
            cur_node = self.head
            count = self.count()
            while count != 0:
                if cur_node.data == prev_node:
                    if count == 1:
                        cur_node.next = new_node
                    else:
                        new_node.next = cur_node.next
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
            if cur_node.data == key:
                self.head = cur_node.next
                cur_node = None
                del_status = True
            else:
                while True:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    if cur_node.data == key:
                        if cur_node.next is None:
                            prev_node.next = None
                            cur_node = None
                        else:
                            prev_node.next = cur_node.next
                            cur_node = None

                        del_status = True                        
                        break

        return del_status


    def display(self):
        if self.head is not None:
            ll = []
            cur_node = self.head
            ll.append(cur_node.data)
            while cur_node.next != None:
                cur_node = cur_node.next
                ll.append(cur_node.data)
    
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
    sll = Single_linked_list()
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
                sll.push(e)

            print('Element(s) has been added to the list.')
            sll.display()
            print('----------------------------------------\n')
        elif choice == 2:
            print('\n----------------------------------------')
            if sll.count() > 0:
                sll.display()
                data = input('Enter data to be inserted: ')
                prev_node = input('After element: ')
                data_inserted = sll.insert(prev_node, data)
                if data_inserted:
                    print('Data has been added.')
                    sll.display()
                else:
                    print(f'Element {prev_node} is not in the list. Try again!')
            else:
                print('List is empty, try again after adding some data.')

            print('----------------------------------------\n')
        elif choice == 3:
            print('\n----------------------------------------')
            if sll.count() > 0:
                sll.display()
                data = input('Data to be deleted: ')
                data_deleted = sll.delete(data)
                if data_deleted:
                    print("Data has been deleted.")
                    sll.display()
                else:
                    print(f'Element {data} is not in the list. Try again.')
            else:
                print('List is empty, try again after adding some data first.')

            print('----------------------------------------\n')
        elif choice == 4:
            print('\n----------------------------------------')
            count = sll.count()
            print(f'Total no of elements in list: {count}')
            print('----------------------------------------\n')
        elif choice == 5:
            break
        else:
            print('\nWrong choice. Try again.\n')