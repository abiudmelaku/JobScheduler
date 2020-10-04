import Func_IO
func = Func_IO.Func_IO()
counter = 0
arr = []

class Node:

    def __init__(self, key , name , duration):
        self.data = key;
        self.name = name
        self.duration = duration
        self.right_child = None
        self.left_child = None;
class BSTDemo:

    def __init__(self):
        self.root = None
    def insert(self, key , time_Exists):
        if(self.root == None):
            self.root = key
            if not time_Exists:
                self.read_write(self.root, "w")
        else:
            self._insert(self.root , key , time_Exists)


    def _insert(self, curr, key , time_Exists):
        if(key.data < curr.data and func.calculate_duration(key.data , key.duration) < curr.data ):
            if (curr.left_child == None):
                curr.left_child = key
                if not time_Exists:
                    self.read_write(key , "w")
            else:
                self._insert(curr.left_child , key , time_Exists)


        elif(key.data > curr.data and key.data > func.calculate_duration(curr.data , curr.duration)):

            if (curr.right_child == None):
                curr.right_child = key
                if not  time_Exists:
                  self.read_write(key,"w")
            else:
                self._insert(curr.right_child , key , time_Exists)
        else:
            print("Duplicate time schedual !!!! Please edit your time schedule  ")
            return

    def in_order(self):
        global counter;
        global arr
        counter = 0;
        arr = []
        print("        Time                 Duration               Schedule Name     ")
        print("________________________________________________________________")

        return self._in_order(self.root)

    def _in_order(self, curr):
        global  counter;
        global arr;
        if curr:
            self._in_order(curr.left_child)
            counter += 1
            print(f"{str(counter)})    {func.convert12(curr.data)}       {func.convert12(curr.data)}  - {func.convert12(func.calculate_duration(curr.data , curr.duration)[:-3])}          {curr.name}")
            arr.append(curr.data)
            self._in_order(curr.right_child)
        return arr;


    def pre_order(self):
        global arr;
        arr = []
        '''root, left, right'''
        return  self._pre_order(self.root)


    def _pre_order(self, curr):
        global arr;
        if(curr):
            arr.append(curr)
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)
        return arr;

    def post_order(self):
        '''left, right, root'''
        self._post_order(self.root)

    def _post_order(self, curr):
        if (curr):
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data)

    def find_val(self, key):
        return self._find_val(self.root , key)


    def _find_val(self, curr, key):
        if(curr):
            if(key ==  curr.data):
                return curr
            elif (key > curr.data):
                return self._find_val(curr.right_child , key)
            else:
               return self._find_val(curr.left_child, key)
        return False
    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
         return self._delete_val(self.root, None, None, key)


    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else:
            print(f"{key} not found in Tree")
            return False
        return True

    def read_write(self, key, rw):
        try:
            if rw == "w":
                with(open("jobscheduler.txt", "a")) as file:
                    file.write(f"{key.data},{key.duration},{key.name}.\n")
            elif rw == "r":
                with open("jobscheduler.txt") as file:
                    r = file.read()
                    if r == "":
                        return False
                    else:
                        file.seek(0)
                        for line in file:
                            x = line.split(",")


            else:
                pass;


        except IOError:
            print("Storage file deleted by someone on your side !!!!")




