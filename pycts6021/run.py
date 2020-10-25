#!/usr/bin/env python3
# Instantiate a new BlobServiceClient using a connection string
from azure.storage.blob import BlobServiceClient
# pycts602api.py must be somewhere in PATH
from pycts602api import CTS602API
import time
from datetime import datetime

now = datetime.now()

blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=nilan;AccountKey=v2ALtj3EtoroxJT923jTC0yFqg0c+aHPbXdis12+W2HDGLxr78olbnimLxi1POcYkc2tHCMyF7EWjquPqx2I9w==;EndpointSuffix=core.windows.net')
container_client = blob_service_client.get_container_client("nilan")

#container_client.create_container()
#times = now.strftime("%H_%M_%S")
#blob_client = container_client.get_blob_client(time)

m = CTS602API('/dev/ttyUSB0') # change appropriately

while True:
	data = m.get_realtime_data()

# print out humidity (%)
#blob_client.upload_blob(data, blob_type="PageBlob")

	#container_client.create_container()
	times = now.strftime("%H_%M_%S")
	blob_client = container_client.get_blob_client(times)
	blob_client.upload_blob(str(data),blob_type="BlockBlob")
	time.sleep(600)

#blob_client.upload_blob(str(data),blob_type="AppendBlob")
	print "ran"
