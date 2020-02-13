import fileinput

# check whether or not lights are off or on
# if lights are on, return True
# otherwise, return False
def all_off(states):
    for state in states.values():
        if state:
            return False
    return True

# change states of lights
def change_states(states, switch_dic, switch):
    for light_control in switch_dic[switch]:
        states[light_control] = not states[light_control]

# switch lights off
def optimize(switch_list, switch_order, switch_dic, states, step):
    # determine the current states of lights
    if all_off(states):
        global all_switch_order
        # determine how many steps are used to turn all lights off
        # and if the step does not stored, and initialize and store it
        if step not in all_switch_order:
            all_switch_order[step] = []
        all_switch_order[step].append(switch_order.copy())
        return
    elif len(switch_list) == 0:
        return
    step += 1

    # solution
    for switch in switch_list:
        switch_copy = switch_list.copy()
        switch_copy.remove(switch)
        switch_order.append(switch)
        change_states(states, switch_dic, switch)
        optimize(switch_copy, switch_order, switch_dic, states, step)
        change_states(states, switch_dic, switch)
        switch_order.pop()


line_num = 1
lines = []
switches = {}
initial_states = {}
all_switch_order = {}

for line in fileinput.input(): 
    lines.append(line.replace("\n", ""))

    if line_num % 2 == 0:
        input_error = False
        lights = lines[0].split(" ")
        edges = lines[1].split(" ")

        for light in lights:
            if len(light) != 1:
                input_error = True
            # initialize the state of the light
            initial_states[light] = True
            switches[light] = []
            switches[light].append(light)

        # check inputs
        for light in lights:
            for edge in edges:
                if edge != '' and len(edge) > 2:
                    input_error = True
                elif edge != '' and len(edge) == 1:
                    continue
                elif edge != '' and edge[0] == light:
                    switches[light].append(edge[1])

        if not input_error:
            optimize(lights, [], switches, initial_states, 0)
            all_switch_order = sorted(all_switch_order.items(), key=lambda x: x[0])
            if len(all_switch_order) == 0:
                print('Unresolved')
            else:
                print("Solution:"," ".join( i for i in all_switch_order[-1][1][0]))
        else:
            print('Input error')
        switches = {}
        initial_states = {}
        all_switch_order = {}
        lines = []
        print("---------------------------------------------------------")
    line_num += 1
