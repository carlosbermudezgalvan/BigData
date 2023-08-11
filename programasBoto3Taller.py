import boto3

def codigo_prueba():
        client = boto3.client('s3', 'us-east-1')
        print(client.list_buckets())

# Listar unicamente los nombres de los buckets
def list_s3_buckets_names():
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        bucket_name = [bucket['Name'] for bucket in response['Buckets']]
        for bucket in bucket_name:
                print("\t",bucket)
        return bucket_name

# Listar unicamente los nombres de los archivos de cada bucket
def list_files_in_buckets(bucket_name):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=bucket_name)
        file_names = [obj['Key'] for obj in response.get('Contents',[])]
        return file_names

# Cargar arhivo a un bucket
def upload_file_to_bucket(bucket_name, file_path, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_path
    s3.upload_file(file_path, bucket_name, object_name)

# Descargar archivo desde un bucket
def download_file_from_bucket(bucket_name, object_name, local_file_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, object_name, local_file_path)


if __name__ == "__main__":
        print("BUckets names")
        buckets = list_s3_buckets_names()
        print("---------------------")
        print("Files in  buckets")
        print("---------------------")
        for bucket in buckets:
                print("Nombre de bucket:",bucket)
                print("Archivos:")
                files = list_files_in_buckets(bucket)
                for file in files:
                        print("\t",file)
        # Cargar archivo al bucket
        bucket_name = 'carlosbucketsss'
        file_path = 'archivo_para_subir.txt'
        upload_file_to_bucket(bucket_name, file_path)

        #Descargar archivo desde le bucket
        object_name = 'carlosbucketsss/archivo_para_subir.txt'  # Reemplaza con el nombre del archivo en S3
        local_file_path = '/home/ubuntu/python-project/descarga.txt'  # Ruta donde deseas guardar el archivo descargado

        download_file_from_bucket(bucket_name, object_name, local_file_path)
        print("Archivo descargado exitosamente.")