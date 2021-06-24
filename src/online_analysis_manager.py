from tkinter import filedialog
from shutil import copyfile
import heka_reader
import tkinter.ttk as ttk
import re
import numpy as np



class OnlineAnalysisManager:
    def __init__(self):
        self.bundle = None
        self.metadata = []
        self._dat_file_name = ""
        self.meta_data_identifiers = ["CSlow"]

        ''' Once a file has been read in live mode, it's content will be safed as a STATE in the variable _node_list_state. 
        The STATE will be updated as long as the experiment is running and new series recordings will be appendet. 
        Additionally the discarded series will be safed to provide any later re-selection'''

        self._node_list_STATE = []
        self._discardet_nodes_STATE = []
        self._pgf_info_STATE= []

        self.stimulation_count = 0
        self.channel_count = 0
        self.stim_channel_count = 0

        self._data_view_STATE = 0


    @property
    def data_view_STATE(self):
        return self._data_view_STATE

    @data_view_STATE.setter
    def data_view_STATE(self, val):
        self._data_view_STATE = val

    @property
    def node_list_STATE(self):
        return self._node_list_STATE

    @node_list_STATE.setter
    def node_list_STATE(self, val):
        self._node_list_STATE = val

    @property
    def dat_file_name(self):
        return self._dat_file_name

    @dat_file_name.setter
    def dat_file_name(self, val):
        self._dat_file_name = val


    def read_dat_tree_structure(self,treeview,mode):
        '''Main function to orchestrate the reading of a dat file, will return a treeview'''

        self.tree= treeview
        # a list to provide node information tuple [node_type, node_name]
        node_list = []
        pgf_list = []

        #TODO mode for the offline Analyis  --> should get the file from the dropdown!

        if mode=='new':
            if self.dat_file_name =="": # implemented for testing purporses
                self.selected_file = filedialog.askopenfilename()
            else:
                print("Already stated the file for testing purposes")
                self.selected_file = self.dat_file_name
            self.path_elements = self.selected_file.split("/")
            self._dat_file_name = self.path_elements[len(self.path_elements) - 1]
            self.bundle = heka_reader.Bundle(self.selected_file)


            '''node list is a triple of data: node type, node name, node item object e.g. ['Group1','E4',item object .. ]'''
            node_list = self.update_data_structure([],self.bundle,self.tree, node_list)
            pgf_list =  self.update_pgf_structure([],self.bundle,self.tree, pgf_list)
        else:
            node_list= self.node_list_STATE
            pgf_list = self._pgf_info_STATE


        self._pgf_info_STATE = pgf_list
        return self.built_tree_from_list(self.tree, node_list,1)
        # a manual stack-like list which will hold the node types of all sorted notes


    def built_tree_from_list(self,treeview,node_list, mode):
        self.manual_stack = []
        self.tree= treeview
        self.node_list = node_list

        # initialization of the root item
        if node_list:
            self.tree.insert("","0",self.node_list[1][0],text=self.node_list[1][1])
            self.manual_stack.append(self.node_list[1][0])

            # fill the tree iterativly
            for node_number in range(2,len(self.node_list)):

                current_tuple = self.node_list[node_number]
                self.parent = self.get_parent(self.manual_stack,current_tuple[0])
                self.prepared_values=[]
                #print(self.parent)

                if self.parent:

                    # only put information to the traces yet
                    #if "Trace" in current_tuple[0]:
                    self.prepared_values=self.get_values_from_parent_id(self.parent+"_"+self.node_list[node_number][0])

                    self.gui_output = current_tuple[1]

                    # handle sweeps: they have no name - so "sweepX" will be printed
                    if not self.gui_output:
                         self.gui_output=current_tuple[0]

                    self.iid = self.parent+"_"+self.node_list[node_number][0]
                    self.tree.insert(self.parent, 'end', self.iid ,
                                     values=self.prepared_values,text=self.gui_output)

                    self.metadata.append([self.iid,self.node_list[node_number][2]])

                    # put the current element to the stack
                    self.manual_stack.append(current_tuple[0])

                else:
                    self.tree.insert("", "0", self.node_list[node_number][0], text=self.node_list[node_number][1])
                    self.manual_stack.append(self.node_list[node_number][0])

            if mode:
                self.node_list_STATE = self.node_list

        return self.tree


    def get_values_from_parent_id(self,parent):
        '''A function to cast the parent id into a value encoding. This will be needed to read the data from the bundle. '''
        self.numbers = [int(s) for s in re.findall(r'\d+',parent)] # list of integers

        # adaption to offline analysis: it will be assumed that there is always only one group per file in offline analysis.
        # Therefore the group identification number is exchanged by the title of the file (e.g. Group210111_11.dat instead of Group1).
        # since the title might contain underscore(s) ("_") more than 4 numbers might be detected.

        p = 1 #  --> "Group in Series"

        if "Trace" in parent:
            p = 4
        else:
            if "Sweep" in parent:
                p=3
            else:
                if "Series" in parent:
                    p=2


        l = len(self.numbers)
        if  l == p: #4 because of structure: (Group,Series,Sweep,Trace) -> typical result from online analysis
            start_pos = 0
        else:
            start_pos= l - p
            '''file_name = []
            for s in range(0,start_pos):
                file_name = file_name +str(self.numbers[s])
            '''
            self.numbers[start_pos]=1

        for s in range(start_pos,len(self.numbers)):
                self.numbers[s]=self.numbers[s]-1

        ret_val = self.numbers[start_pos:len(self.numbers)]
        return ret_val




    def get_parent(self,stack,current):
        '''function to identify the parent node by it's id:
        each node will gt an unique id, structure is well known yet: each group has many series, a series has many Sweeps, a sweep has 2 traces'''
        s_index = 0

        # groups are allways level 1
        if "Group" in current:
            return ""

        # series have a group the belong to
        if "Series" in current:
            if "Group" in stack[len(stack)-1]:
                return stack[len(stack) - 1]  # group name
            else:
                for i in range(0, len(stack)):
                    if "Group" in stack[i]:
                        s_index = i
                return stack[s_index]

        # multiple sweeps belong to 1 series
        if "Sweep" in current:
                for i in range(0,len(stack)):
                    if "Series" in stack[i]:
                        s_index=i
                self.series = stack[s_index]

                for i in range(0, len(stack)):
                    if "Group" in stack[i]:
                        s_index = i
                return stack[s_index]+"_"+self.series

        # exact 2 traces exist for each sweep
        if "Trace" in current:
            for i in range(0, len(stack)):
                if "Series" in stack[i]:
                    s_index = i
            self.series = stack[s_index]
            s_index = 0
            for i in range(0, len(stack)):
                if "Group" in stack[i]:
                    s_index = i

            if "Sweep" in stack[len(stack)-1]:
                    return stack[s_index] + "_" + self.series +"_" +stack[len(stack)-1]
            else:
                    return stack[s_index] + "_" + self.series +"_" +stack[len(stack) - 2]

    def update_data_structure(self, index, bundle, dat_file_structure, node_list):
        root = bundle.pul
        node = root
        '''select the last node '''
        for i in index:
            node = node[i]
        node_type = node.__class__.__name__
        if node_type.endswith('Record'):
            node_type = node_type[:-6]
        try:
            node_type += str(getattr(node, node_type + 'Count'))
        except AttributeError:
            pass
        try:
            node_label = node.Label
        except AttributeError:
            node_label = ''
        metadata = []
        try:
            metadata.append(node)
        except Exception as e:
            metadata.append(node)
        # @TODO check if [node instead of metadata works better
        node_list.append([node_type, node_label, metadata])
        for i in range(len(node.children)):
            self.update_data_structure(index + [i], bundle, dat_file_structure, node_list)
        return node_list

    def update_pgf_structure(self, index, bundle, dat_file_structure, node_list):
        """Recursively read tree information from the bundle's embedded .pul file
        """
        # ToDO --> implement the pgf so that the metadata of the pgf can be returned for each Series !!
        root = bundle.pgf  ### here return to pul if you want everything to work again as before
        node = root
        #print("Node content:")
        for i in index:
            node = node[i]
            #print(node)
        node_type = node.__class__.__name__
        #print("Node type:")
        #print(node_type)
        if node_type.endswith('PGF'):
            node_type = node_type[:-3]
        if node_list:
            previous_node_type = node_list[len(node_list) - 1][0]
            if ("StimChannel" in previous_node_type) & ("Stimulation" in node_type):
                self.stim_channel_count = 0
            if ("Channel" in previous_node_type) & ("Stimulation" in node_type):
                self.channel_count = 0
        try:
            node_type += str(getattr(node, node_type + 'Count'))  # is not provided in the pgf structure
        except AttributeError:
            if node_type == "Stimulation":
                self.stimulation_count = self.stimulation_count + 1
                node_type = "Stimulation" + str(self.stimulation_count)
            if node_type == "Channel":
                self.channel_count = self.channel_count + 1
                node_type = "Channel" + str(self.channel_count)
            if node_type == "StimChannel":
                self.stim_channel_count = self.stim_channel_count + 1
                node_type = "StimChannel" + str(self.stim_channel_count)
            pass
        try:
            node_label = node.EntryName
            #print(node_label)
        except AttributeError:
            node_label = ''
        #print("Notated node type:")
        #print(node_type)
        metadata = []
        # for  i in range(len(node.children)):
        try:
            metadata.append(node)
        except Exception as e:
            metadata.append(node)
        # print(node_type)
        # print(node_label)
        # print(metadata)
        node_list.append([node_type, node_label, metadata])
        #print("children")
        #print(len(node.children))
        for i in range(len(node.children)):
            #print("entered children " + str(i))
            self.update_pgf_structure(index + [i], bundle, dat_file_structure, node_list)
        # print(node_list)  # print out the new pgf node list
        return node_list


    def get_pgf_voltage(self,node_info):
        elems = node_info.split("_")
        grp_pos = re.match(r"([a-z]+)([0-9]+)", elems[0] , re.I)
        stim_pos = re.match(r"([a-z]+)([0-9]+)", elems[1] , re.I)

        pgf_stim = "Stimulation"+str(stim_pos[2])
        stim_chan_list = []
        scl_begin = 0
        for i in self._pgf_info_STATE:
            if i[0]==pgf_stim:
                    scl_begin = self._pgf_info_STATE.index(i)

        v_holding = self._pgf_info_STATE[scl_begin+1][2][0].Holding

        for i in range(scl_begin+1,len(self._pgf_info_STATE)):

            if "StimChannel" in self._pgf_info_STATE[i][0]:
                stim_chan_list.append(self._pgf_info_STATE[i])

            if "Stimulation" in self._pgf_info_STATE[i][0]:
                break

        # stim_chan_list hold's all StimChannel nodes now
        signal_duration = 0
        for i in stim_chan_list:
            signal_duration = signal_duration + i[2][0].Duration # time in s


        array = [int(grp_pos[2])-1, int(stim_pos[2])-1, 0, 0]

        data = self.read_data_from_dat_file(array,self.bundle)

        pgf_sig = []

        # will stay empty if no increment will be detected
        # if increment will be detected, start- and end-point of the interval as well as start- and end-value of incrementation
        step_protokoll=[]

        for i in stim_chan_list:

            start_point =len(pgf_sig)
            end_point = len(pgf_sig)+round((i[2][0].Duration*len(data[1]))/signal_duration)

            for a in range(start_point,end_point):
                v = i[2][0].Voltage
                if v==0:
                    pgf_sig.append(v_holding)
                else:
                    pgf_sig.append(v)

            if i[2][0].DeltaVIncrement:
                tmp = []
                tmp.append(start_point)
                tmp.append(end_point)
                tmp.append(pgf_sig[start_point-1])
                tmp.append(pgf_sig[len(pgf_sig)-1])
                tmp.append(i[2][0].DeltaVIncrement)
                step_protokoll.append(tmp)

        # @TODO you can not display multiple step intervals. For now, only 1 step interval is recognized (e.g. in IV)
        help_lst = []
        if step_protokoll:
            n_h = self._pgf_info_STATE[scl_begin][2][0]
            nos = n_h.NumberSweeps
            #print("step_protokoll")
            #print(step_protokoll)

            tmp = step_protokoll[0]


            for i in range(0,nos):
                modified_pgf = pgf_sig[:]
                #print("val")
                #print(str(tmp[2]+i*tmp[4]))

                modified_pgf[tmp[0]:tmp[1]]=[tmp[2]+i*tmp[4]] * (tmp[1]-tmp[0])
                #print(str(modified_pgf[tmp[0]:tmp[1]]))

                help_lst.append(modified_pgf)

        time = np.linspace(0, len(self.data) - 1, len(self.data))
        if help_lst:
            #print("return_list")
            return time,help_lst
        else:
            return time,[pgf_sig]

    def read_data_from_dat_file(self,source_array,bundle):
        data_bundle = bundle
        #else:
            #data_bundle = self.bundle

        self.data = data_bundle.data[source_array]
        #print(self.data)
        self.time = np.linspace(0,len(self.data)-1, len(self.data))
        return(self.time,self.data)
        #time = np.linspace(trace.XStart, trace.XStart + trace.XInterval * (len(data) - 1), len(data))

    def read_series_from_dat_file(self,tree,item_id):
        '''A function to iteratively read the containing sweeps of a series. The series will be selected in the treeview'''
        print(item_id)
        return (len(tree.get_children(item_id)))

    def get_Ymin_metadata(self,item_id):
        return self.get_metadata(item_id,'Ymin')

    def get_Ymax_metadata(self, item_id):
        return self.get_metadata(item_id, 'Ymax')

    def get_XStart_metadata(self, item_id):
        return self.get_metadata(item_id, 'XStart')

    def get_XInterval_metadata(self, item_id):
        return self.get_metadata(item_id, 'XInterval')

    def get_metadata(self,item_id,metadata_identifier):
        self.modified_iid = item_id
        for i in range(0, len(self.metadata)):
            if self.metadata[i][0] == self.modified_iid:
                self.meta_list = self.metadata[i][1]
                return self.meta_list[0].get_fields()[metadata_identifier]



    def get_series_recording_mode(self,item_id):
        '''A recording mode can only be extracted from traces. Therefore the first trace in a series will be evaluated
        and it's recording mode will be returned as the recording mode (string representation) of the entire series
         item_id-> identifier of the clicked item (should be a series in this case'''
        self.modified_iid = item_id + "_Sweep1_Trace1"
        for i in range(0,len(self.metadata)):
           if self.metadata[i][0]==self.modified_iid:
               self.meta_list = self.metadata[i][1]
               self.recording_mode = self.meta_list[0].get_fields()['RecordingMode']

               if str(self.recording_mode)=="b'\\x03'":
                   return('Voltage Clamp')

               if str(self.recording_mode)=="b'\\x04'":
                   return("Current Clamp")


    def get_list_of_series_identifiers(self,node_list):
        list_of_series_indentifiers = []
        for n in node_list:
            if "Series" in n[0]:
                list_of_series_indentifiers.append(n[0])
        return list_of_series_indentifiers

    def get_list_of_series_names(self,node_list):
        list_of_series= []
        for n in node_list:
            if "Series" in n[0]:
                list_of_series.append(n[1])
        return list_of_series

    def retrieve(self,node_object):
        self._discardet_nodes_STATE,self._node_list_STATE= self.change_series_treeview(node_object, self._discardet_nodes_STATE, self._node_list_STATE)

    def discard(self,node_object):
        self._node_list_STATE,self._discardet_nodes_STATE= self.change_series_treeview(node_object,self._node_list_STATE,self._discardet_nodes_STATE)

    def change_series_treeview (self,node_object,list_a,list_b):
        '''move a series from list_a to the concerning position in list b'''

        if "Series" in node_object:
            identifier_sub_parts  = node_object.split('_')

            ''' find index of parent node, series node and the number of children in the nodelist of the series that is aimed to be discarded '''
            for n in list_a:
                if n[0]==identifier_sub_parts [0]:
                    parent_node_index = list_a.index(n)

                if n[0]==identifier_sub_parts [1]:
                    series_node_index = list_a.index(n)

            series_amount_list_elements = self.get_series_amount_of_list_elements(list_a,series_node_index)

            '''remove the series taht is aimed to be discarded from the data tree view'''
            new_data_list = list_a[0:series_node_index] + list_a[series_node_index+series_amount_list_elements:len(list_a)]

            '''add the series that is aimed to be discarded to the discarded tree view'''


            if list_b:
                ''' if the treeview isn't empty any more find the correct position to insert the new series'''

                '''find a list of all series (e.g. [Series1,Series3]) in the discarded tree and according to the series numbers - find the correct position for the new discarded series to be inserted'''
                series_identifier_list = self.get_list_of_series_identifiers(list_b)
                insert_after = "" # string of the nody type (e.g. 'Series1')
                series_position = re.match(r"([a-z]+)([0-9]+)", identifier_sub_parts[1], re.I)
                for n in series_identifier_list:
                    tmp_series = re.match(r"([a-z]+)([0-9]+)", n, re.I)
                    if int(series_position[2])-int(tmp_series[2]) > 0:
                        insert_after = n

                if insert_after:
                    p_temp = self.get_list_position_by_node_type(list_b,insert_after)
                    c_temp = self.get_series_amount_of_list_elements(list_b,p_temp)
                    insert_position = p_temp+c_temp
                else:
                    insert_position=2 #  0= pulsed, 1= group, 2 would be 1st series

                if len(list_a)==insert_position:
                    # append to the end
                    helper_list = list_b + list_b[series_node_index:series_node_index + series_amount_list_elements]

                else:
                    # append anywhere in between
                    helper_list = list_b[0:insert_position] + list_a[
                    series_node_index:series_node_index + series_amount_list_elements] + list_b[insert_position:len(list_b)]



            else:
                # write to the empty list for the first time
                helper_list = [list_a[0]] + [list_a[parent_node_index]]+ list_a[series_node_index:series_node_index + series_amount_list_elements]


            return new_data_list, helper_list


    def get_discarded_data_tree(self,treeview,mode):
        return self.built_tree_from_list(treeview,self._discardet_nodes_STATE, 0)


    def get_series_amount_of_list_elements(self,list,series_list_index):
        '''takes a list position of the series of interest as input and will return the number of children until the next series starts '''

        for n in list[series_list_index+1:len(list)]:
            # returns as soon as the first series is found
            if "Series" in n[0]:
                return list.index(n)-series_list_index

        # returns if no more series was found
        return len(list)-series_list_index

    def get_list_position_by_node_type(self,list,node_type):

        for n in list:
            if n[0]==node_type:
                return list.index(n)


    def write_series_and_metadata_to_labbook(self, additional_meta_data = None):
        # generate a list of data to be written in the labbbook
        table_list = []
        list_of_series_names = self.get_list_of_series_names(self._node_list_STATE)
        list_of_series_types = self.get_list_of_series_identifiers(self._node_list_STATE)
        for i in list_of_series_types:
            series_identifiers,series_metadata = self.get_labbook_metadata(i,additional_meta_data)
            #print(series_metadata)
            #print(list_of_series_names[list_of_series_types.index(i)])
            tmp_list=([list_of_series_names[list_of_series_types.index(i)]] + series_metadata)
            table_list.append(tmp_list)
        print(table_list)

        return series_identifiers, table_list


    def get_labbook_metadata(self,series_identifier,additional_meta_data=None):

        if additional_meta_data:
            for i in additional_meta_data:
                if i not in self.meta_data_identifiers:
                    self.meta_data_identifiers.append(str(i))

        print(self.meta_data_identifiers)
        meta_data_values = []
        item_id = "Group1_"+series_identifier + "_Sweep1_Trace1"
        for i in self.meta_data_identifiers:
            meta_data_values.append(self.get_metadata(item_id,i))
            #print(i)
            #print(self.get_metadata(item_id,i))
            #print(meta_data_values)

        return self.meta_data_identifiers,meta_data_values
