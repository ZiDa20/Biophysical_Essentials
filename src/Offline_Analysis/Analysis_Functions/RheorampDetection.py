## not implemented yet

"""
def plot_rheoramp_event_counts(self, parent_widget, result_list, number_of_sweeps):
    canvas = self.handle_plot_widget_settings(parent_widget)
    meta_data_groups = self.get_meta_data_groups_for_results(result_list, number_of_sweeps)
    meta_data_types = list(dict.fromkeys(meta_data_groups))
    plot_matrix = []

    for meta_type in meta_data_types:
        type_specific_series_pos = [i for i, x in enumerate(meta_data_groups) if x == meta_type]
        sweep_1 = []
        sweep_2 = []
        sweep_3 = []
        sweep_4 = []
        for pos in type_specific_series_pos:
            sweep_1.append(result_list[pos * 4][0])
            sweep_2.append(result_list[pos * 4 + 1][0])
            sweep_3.append(result_list[pos * 4 + 2][0])
            sweep_4.append(result_list[pos * 4 + 3][0])

        sweep_1 = [0 if i is None else i for i in sweep_1]
        sweep_2 = [0 if i is None else i for i in sweep_2]
        sweep_3 = [0 if i is None else i for i in sweep_3]
        sweep_4 = [0 if i is None else i for i in sweep_4]

        plot_matrix.append(sweep_1)
        plot_matrix.append(sweep_2)
        plot_matrix.append(sweep_3)
        plot_matrix.append(sweep_4)
        # for pos in type_specific_series_pos:
    ax = canvas.figure.subplots()

    plot = ax.boxplot(plot_matrix,  # notch=True,  # notch shape
                      vert=True,  # vertical box alignment
                      patch_artist=True)



def rheoramp_analysis(self):
    print("not implemented")

"""