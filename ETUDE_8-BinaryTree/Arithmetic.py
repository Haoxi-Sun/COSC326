import fileinput
import re

## Node for a binary tree
class Node:
    def __init__(self, value, operations):
        # stores calculated value
        self.node_val = value
        # stores operations 
        self.operations = operations
        # next addition node
        self.add_node = None
        # next multiply node
        self.multiply_node = None 
        # add the calculated value 
        self.add_value = 0
    
        ### these variables are for normal order
        # stores the value in the previous node temporarily
        self.temp_add_value = 0
        # stores multiply value
        self.multiply_value = 0
        # add and multiply values, and get an end value
        self.end_value = 0


## left to Right Arthmetic
class ArthmeticLR:
    def __init__(self, input_numbers, target_result):
        # numbers the user inputs
        self.numbers = input_numbers
        # target result
        self.result = target_result
        # operations list
        self.operation_list = []
        # root node
        self.root_node = Node(self.numbers[0], self.operation_list)
        # if the result cannot be matched
        if self.check_min_max(): 
            print("L " + str(self.result) +  " impossible")
        elif not self.create_node_link(self.root_node, 1):
            print("L " + str(self.result) +  " impossible")

    # calculate the min result and max result
    # if the target result it out of range between min and max,
    # return True
    def check_min_max(self):
        min_num = self.numbers[0]
        max_num = self.numbers[0]
        for i in range(1, len(self.numbers)):
            if min_num == 1:
                min_num *= self.numbers[i]
            if max_num == 1:
                max_num += self.numbers[i] 
            elif self.numbers[i] == 1:
                min_num *= self.numbers[i]
                max_num += self.numbers[i]
            else:
                min_num += self.numbers[i]
                max_num *= self.numbers[i]
        if self.result > max_num or self.result < min_num: 
            return True
    
    # create node link
    # if return True, add an operator into the operation list
    # in this binary tree, do addition first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def create_node_link(self, node, position):
        # addition node
        if self.link_add_node(node, position):
            return True
        # multiply node
        elif self.link_multiply_node(node, position):
            return True

    # add adiition nodes into the tree
    def link_add_node(self, node, position):
        if position == len(self.numbers):
            return False
        
        if position == (len(self.numbers)-1):
            # take the node.operatins in a subtree
            operations = node.operations.copy()
             # append addition operation
            operations.append("+")
            # create the last addition node
            node.add_node = Node(node.node_val + self.numbers[position], operations)
            # if the target result can be matched
            # print out the result and process and return True
            if (node.node_val + self.numbers[position]) == self.result:
                output_str = "L " + str(self.result) + " " + str(self.numbers[0])
                for i in range(len(self.numbers)-1):
                    output_str = output_str + " " + operations[i] + " " + str(self.numbers[i+1])
                print(output_str)
                return True
        else:
            # larger then target result
            if node.node_val + self.numbers[position] > self.result:
                return False
            # append addition operation
            operations = node.operations.copy()
            operations.append("+")
            # add a calculated value into a node in a addition subtree 
            node.add_node = Node(node.node_val + self.numbers[position], operations)
            # link to the node
            if self.create_node_link(node.add_node, position+1):
                return True
            else:
                return False

    # create a multiply node
    # if addition cannot get the target value
    # do multiply
    def link_multiply_node(self, node, position):
        if position == len(self.numbers):
            return False
        elif position == (len(self.numbers)-1):
            # append multiply operation
            operations = node.operations
            operations.append("*")
            # create a multiply node
            node.multiply_node = Node(node.node_val * self.numbers[position], operations)
            # if the target value can be matched
            # print out the result and process
            # and return True
            if (node.node_val*self.numbers[position]) == self.result:
                output_str = "L " + str(self.result) + " " + str(self.numbers[0])
                for i in range(len(self.numbers)-1):
                    output_str = output_str + " " + operations[i] + " " + str(self.numbers[i+1])
                print(output_str)
                return True
        else:
            # larger than target result
            if node.node_val * self.numbers[position] > self.result:
                return False
            # append multiply operation
            operations = node.operations
            operations.append("*")
            # create multiply node
            node.multiply_node = Node(node.node_val * self.numbers[position], operations)
            # link nodes in the tree
            if self.create_node_link(node.multiply_node, position+1):
                return True
            else:
                return False
        
## calculate as an normal order
class ArthmeticN:
    def __init__(self, input_numbers, target_result):
        self.numbers = input_numbers
        self.result = target_result
        self.operation_list = []
        self.root_node = Node(self.numbers[0], self.operation_list)

        # if the result cannot be matched
        if self.check_min_max(): 
            print("N " + str(self.result) +  " impossible")
        elif not self.create_node_link(self.root_node, 1):
            print("N " + str(self.result) +  " impossible")

    # calculate the min result and max result
    # if the target result it out of range between min and max,
    # return True
    def check_min_max(self):
        min_num = self.numbers[0]
        max_num = self.numbers[0]
        for i in range(1, len(self.numbers)):
            if min_num == 1:
                min_num *= self.numbers[i]
            if max_num == 1:
                max_num += self.numbers[i] 
            elif self.numbers[i] == 1:
                min_num *= self.numbers[i]
                max_num += self.numbers[i]
            else:
                min_num += self.numbers[i]
                max_num *= self.numbers[i]
        if self.result > max_num or self.result < min_num: 
            return True
    
    # create node link
    # if return True, add an operator into the operation list
    # in this binary tree, do addition first                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def create_node_link(self, node, position):
        # addition node
        if self.link_add_node(node, position):
            return True
        # multiply node
        if self.link_multiply_node(node, position):
            return True

    # link add node
    def link_add_node(self, node, position):

        # initialize the temp_add_value
        if (node.add_value == 0) and (node.multiply_value == 0):
            node.temp_add_value = node.node_val
        
        if position >= len(self.numbers):
            return False

        elif position == (len(self.numbers)-1):
            # append addition operation
            operations = node.operations.copy()
            operations.append("+")
            node.add_node = Node(self.numbers[position], operations)
            # caculate end value
            node.add_node.end_value = node.add_value + node.temp_add_value + self.numbers[position] + node.multiply_value
            # if the targer result can be matched
            if node.add_node.end_value == self.result:
                # print the result and process
                output_str = "N " + str(self.result) + " " + str(self.numbers[0])
                for i in range(len(self.numbers)-1):
                    output_str = output_str + " " + operations[i] + " " + str(self.numbers[i+1])
                print(output_str)
                return True
        else:
            # larger than target result
            if (node.add_value + node.temp_add_value + self.numbers[position] + node.multiply_value) >  self.result:
                return False
            # append addition operation
            operations = node.operations.copy()
            operations.append("+")
            node.add_node = Node(self.numbers[position], operations)
            # caculate add value into temp_add_value
            node.add_node.add_value = node.add_value + node.temp_add_value + node.multiply_value
            node.add_node.multiply_value = 0
            node.add_node.temp_add_value = self.numbers[position]
            if self.create_node_link(node.add_node, position+1):
                return True
            else:
                return False


    # link multiply node
    def link_multiply_node(self, node, position):
        if position >= len(self.numbers):
            return False
        elif position == (len(self.numbers)-1):

            operations = node.operations.copy()
            operations.append("*")
            node.multiply_node = Node(self.numbers[position], operations)
            # caculate multiply value
            if node.multiply_value == 0:
                node.multiply_node.multiply_value = node.node_val * self.numbers[position]
            else:
                node.multiply_node.multiply_value = node.multiply_value * self.numbers[position]
            # caculate end value from root to the last node
            node.multiply_node.end_value = node.add_value + node.multiply_node.multiply_value
            # if the target value can be matched
            if node.multiply_node.end_value == self.result:
                # output string
                output_str = "N " + str(self.result) + " " + str(self.numbers[0])
                for i in range(len(self.numbers)-1):
                    output_str = output_str + " " + operations[i] + " " + str(self.numbers[i+1])
                print(output_str)
                return True
        else:
            # larger than target result
            if (node.add_value + node.multiply_value * self.numbers[position]) > self.result:
                return False
             # append multiply operation
            operations = node.operations.copy()
            operations.append("*")
            node.multiply_node = Node(self.numbers[position], operations)
            # caculate multiply value
            if node.multiply_value == 0:
                node.multiply_node.multiply_value = node.node_val * self.numbers[position]
            else:
                node.multiply_node.multiply_value = node.multiply_value * self.numbers[position]
            # add value into multiply_node for next multiply
            node.multiply_node.add_value = node.add_value
            if self.create_node_link(node.multiply_node, position+1):
                return True
            else:
                return False

if __name__ == "__main__":
    lines = []
    line_num = 1
    for line in fileinput.input():
        lines.append(line.replace("\n",""))
        if line_num % 2 == 0:
            number_line = lines[0]
            target_line = lines[1]

            # there are extra spaces between two numbers
            number_line = re.sub("\s\s+"," ", number_line)
            target_line = re.sub("\s\s+"," ", target_line)

            numbers = [int(x) for x in number_line.split(" ")]
            target_number = int(target_line.split(" ")[0])
            Arthmetic_type = target_line.split(" ")[1]

            if "L" == Arthmetic_type:
                ArthmeticLR(numbers, target_number)
            elif "N" == Arthmetic_type:
                ArthmeticN(numbers, target_number)
            lines = []
        line_num += 1
