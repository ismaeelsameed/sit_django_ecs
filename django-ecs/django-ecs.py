import boto3


class Ecs(object):
    region = 'us-west-1'
    definition_name = None
    container = 'edx-cypress'
    platform_name = None
    cluster = 'default'
    image = 'appsembler/edx-lite'

    def __init__(self):
        pass

    def register_task_definition(self, region, definition_name, container, hostname, port):
        client = boto3.client('ecs', region)
        response = client.register_task_definition(
            family=definition_name,
            containerDefinitions=[
                {
                    'name': container,
                    'image': self.image,
                    'cpu': 512,
                    'memory': 1024,
                    'links': [],
                    'portMappings': [
                        {
                            'containerPort': 80,
                            'hostPort': port,
                            'protocol': 'tcp'
                        },
                    ],
                    'essential': True,
                    'entryPoint': [],
                    'command': [],
                    'environment': [],
                    'mountPoints': [],
                    'volumesFrom': [],
                    'hostname': hostname,
                    'dnsServers': [],
                    'dnsSearchDomains': [],
                    'extraHosts': [],
                    'dockerSecurityOptions': [],
                    'dockerLabels': {},
                    'ulimits': [],
                },
            ],
            volumes=[]
        )
        return response

    def create_service(self, region, definition_name, cluster):
        client = boto3.client('ecs', region)
        response = client.create_service(
            cluster=cluster,
            serviceName=definition_name,
            taskDefinition=definition_name,
            loadBalancers=[],
            desiredCount=1,
        )
        return response

    def run_service(self, region, definition_name, container, hostname, port, cluster):
        response = {}
        response['register_task_definition'] = self.register_task_definition(region, definition_name, container,
                                                                             hostname, port)
        response['create_service'] = self.create_service(region, definition_name, cluster)
        return response
