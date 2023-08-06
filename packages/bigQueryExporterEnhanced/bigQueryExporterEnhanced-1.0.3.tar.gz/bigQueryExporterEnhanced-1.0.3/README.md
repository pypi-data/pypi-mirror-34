# Credit
This repository is forked from
https://github.com/IcarusSO/bigQueryExporter

# Change Log (Compare with original version)
### query_to_local()
- Create a temp table with a random hash on BQ as output table, so that simultaneous execution of the function will not overwrite each other.
- Remove the temp table after the execution. (May also set keep_temp_table=True if you wish to keep them).

# bigQueryExporter
Export query data from google bigquery to local machine

#### Installation
    pip install bigQueryExporterEnhanced

#### Example
    # In order to install this package as a drop in replacement,
    # class name is kept as BigQueryExporter.

    from bigQueryExport import BigQueryExporter
    bigQueryExporter = BigQueryExporter(project_name, dataset_name, bucket_name)
    export_path = query_to_local(query)
    
    # or with the options
    export_path = query_to_local(query, 
                                 job_name='simple_query', 
                                 data_dir_path='out/',
                                 keep_temp_table=False,
                                 overwrite_output_folder=True)
    
    

#### Requirement
- Your server/ local machine should have the right to access the project
- Right should be granted following the insturction on [Google SDK](https://cloud.google.com/sdk/docs/)
- Execute the following command

    gcloud auth application-default login
