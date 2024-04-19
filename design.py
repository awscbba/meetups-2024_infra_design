from diagrams import Diagram, Cluster, Edge

from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
# from diagrams.aws.network import APIGateway
from diagrams.aws.network import Route53



with Diagram("ToDo Notes Service", show=False, direction="TB") as design:
    
    with Cluster("AWS Virtual Private Network"):
        vpc = VPC("Private Cloud")
        dns = Route53("dns")
        
        with Cluster("Public Subnet"):
            lb = ELB("Load Balancer")
    
        with Cluster("Private Subnet") as ps:
            #db = RDS("MySQL")
            instances = [EC2("Node 1"),
                         EC2("Node 2"),
                         EC2("Node 3")]
    
        dns >> Edge(xlabel="tcp/http") >> lb >> instances # - db

design
