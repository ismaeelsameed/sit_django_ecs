import boto3


class Ecs(object):
    region = 'us-west-1'
    definition_name = None
    container = None
    platform_name = None
    cluster = 'default'
    image = None
    aws_access_key_id = None
    aws_secret_access_key = None

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def register_task_definition(self, region, definition_name, container, hostname, port, image):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.register_task_definition(
            family=definition_name,
            containerDefinitions=[
                {
                    'name': container,
                    'image': image,
                    'cpu': 1024,
                    'memory': 2048,
                    'links': [],
                    'portMappings': [
                        {
                            'containerPort': 80,
                            'hostPort': port,
                            'protocol': 'tcp'
                        },
                        {
                            'containerPort': 18010,
                            'hostPort': 44300,
                            'protocol': 'tcp'
                        },
                        {
                            'containerPort': 18020,
                            'hostPort': 44100,
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
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.create_service(
            cluster=cluster,
            serviceName=definition_name,
            taskDefinition=definition_name,
            loadBalancers=[],
            desiredCount=1,
        )
        return response

    def run_service(self, region, definition_name, container, hostname, port, cluster, image):
        response = {}
        response['register_task_definition'] = self.register_task_definition(region, definition_name, container,
                                                                             hostname, port, image)
        response['create_service'] = self.create_service(region, definition_name, cluster)
        return response

    def delete_service(self, region, cluster, service_name):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.delete_service(
            cluster=cluster,
            service=service_name
        )
        return response

    def delete_task_defention(self, task_definition, region):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.deregister_task_definition(
            taskDefinition=task_definition
        )
        return response

    def list_services(self, cluster, region):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.list_services(
            cluster=cluster,
            nextToken='string',
            maxResults=100
        )
        return response

    def list_task_definitions(self, family, region, status):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.list_task_definitions(
            familyPrefix=family,
            status=status
        )
        return response

    # services is an array of services
    def cluster_info(self, region, cluster, services):
        client = boto3.client('ecs', region, aws_access_key_id=self.aws_access_key_id,
                              aws_secret_access_key=self.aws_secret_access_key)
        response = client.describe_services(
            cluster=cluster,
            services=services
        )
        return response

