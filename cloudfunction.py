from google.cloud import storage

def gcf_move(event, context):
     gcf_cut("bucketexampleone", event["name"], "bucketexampletwo", event["name"])

def gcf_cut(bucket_name, blob_name, destination_bucket_name, destination_blob_name):
    
    
    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
         source_blob, destination_bucket, destination_blob_name
    )
    source_bucket.delete_blob(blob_name)

    print(
         "blob {} in bucket {} moved to blob {} in bucket {}.".format(
              source_blob.name,
              source_bucket.name,
              blob_copy.name, 
              destination_blob_name,
         )
    )
    
    
    