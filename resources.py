import logging
import json
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential



def process_rg_instance(group):
    """
    Get the relevant pieces of information from a ResourceGroup
    instance.
    """

    return {
        "Name": group.name,
        "Id": group.id,
        "Location": group.location,
        "Type": group.type,
        "Tags": group.tags,
        "Properties: Provisioning State: ": group.properties.provisioning_state \
            if group.properties and group.properties.provisioning_state else None,
    }


def list_rgs(credentials, subscription_id):
    """
    Get list of resource groups for the subscription id passed.
    """

    list_of_resource_groups = []

    with ResourceManagementClient(credentials, subscription_id) as rg_client:
        try:
            for i in rg_client.resource_groups.list():
                list_of_resource_groups.append(process_rg_instance(i)),

            for i in rg_client.resources.list():
                list_of_resource_groups.append(process_rg_instance(i)),

        except Exception as e:
            logging.error("encountered: {0}".format(str(e)))

    return json.dumps(list_of_resource_groups)


credential = DefaultAzureCredential()
print(list_rgs(credential,'b5f57abf-349d-414a-a5a2-9e560d398a25'))
