from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.models import SearchIndexerDataSourceConnection
from azure.search.documents.indexes.models import SqlIntegratedChangeTrackingPolicy
from azure.search.documents.indexes import SearchIndexerClient
# Azure Cognitive Search endpoint and admin key
endpoint = 'https://dlpractice.search.windows.net'
admin_key = '37jMB2DPlxnGcEbeDnB66vlnXpbOwCFSJVOU7yU8uPAzSeA66uzd'

# Define the Azure SQL data source connection
data_source_name = 'dlpractice'
connection_string = "Server=tcp:case-study-poc.database.windows.net,1433;Initial Catalog=case-study-db;Persist Security Info=False;User ID=dbadmin;Password=db@admin12345;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"

data_source = SearchIndexerDataSourceConnection(
    name="dlpractice",
    type="azuresql",
    connection_string=connection_string,
    container={"name": "case_studies"}
)

# Create the data source

credential = AzureKeyCredential(admin_key)
data_source_client = SearchIndexerClient(endpoint=endpoint, credential=credential)
data_source_client.create_data_source_connection(data_source)
