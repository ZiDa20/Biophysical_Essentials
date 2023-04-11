CREATE TABLE IF NOT EXISTS selected_meta_data(table_name VARCHAR, condition_column VARCHAR, conditions VARCHAR, analysis_function_id INTEGER, offline_analysis_id INTEGER);
CREATE TABLE IF NOT EXISTS global_meta_data(analysis_id INTEGER, experiment_name VARCHAR, experiment_label VARCHAR, species VARCHAR, genotype VARCHAR, sex VARCHAR, celltype VARCHAR, condition VARCHAR, individuum_id VARCHAR, PRIMARY KEY(analysis_id, experiment_name));
CREATE TABLE IF NOT EXISTS experiment_analysis_mapping(experiment_name VARCHAR, analysis_id INTEGER, UNIQUE(experiment_name, analysis_id));
CREATE TABLE IF NOT EXISTS experiment_series(experiment_name VARCHAR, series_name VARCHAR, series_identifier VARCHAR, discarded BOOLEAN, sweep_table_name VARCHAR, meta_data_table_name VARCHAR, pgf_data_table_name VARCHAR, series_meta_data VARCHAR, PRIMARY KEY(experiment_name, series_identifier));
CREATE TABLE IF NOT EXISTS results(analysis_id INTEGER, analysis_function_id INTEGER, sweep_table_name VARCHAR, specific_result_table_name VARCHAR);
CREATE TABLE IF NOT EXISTS analysis_functions(analysis_function_id INTEGER PRIMARY KEY DEFAULT(nextval('unique_offline_analysis_sequence')), function_name VARCHAR, lower_bound FLOAT, upper_bound FLOAT, analysis_series_name VARCHAR, analysis_id INTEGER, pgf_segment INTEGER);
CREATE TABLE IF NOT EXISTS sweep_meta_data(sweep_name VARCHAR, series_identifier VARCHAR, experiment_name VARCHAR, meta_data VARCHAR, PRIMARY KEY(sweep_name, series_identifier, experiment_name));
CREATE TABLE IF NOT EXISTS experiments(experiment_name VARCHAR PRIMARY KEY, labbook_table_name VARCHAR, image_directory VARCHAR);
CREATE TABLE IF NOT EXISTS analysis_series(analysis_series_name VARCHAR, "time" VARCHAR, recording_mode VARCHAR, analysis_id INTEGER, PRIMARY KEY(analysis_series_name, analysis_id));
CREATE TABLE IF NOT EXISTS filters(filter_criteria_name VARCHAR PRIMARY KEY, lower_threshold FLOAT, upper_threshold FLOAT, analysis_id INTEGER);
CREATE TABLE IF NOT EXISTS offline_analysis(analysis_id INTEGER PRIMARY KEY DEFAULT(nextval('unique_offline_analysis_sequence')), date_time TIMESTAMP, user_name VARCHAR, selected_meta_data VARCHAR);
CREATE TABLE IF NOT EXISTS "imon_meta_data_201229_07_Series1"("Parameter" VARCHAR, sweep_1 VARCHAR, sweep_2 VARCHAR, sweep_3 VARCHAR, sweep_4 VARCHAR, sweep_5 VARCHAR);




