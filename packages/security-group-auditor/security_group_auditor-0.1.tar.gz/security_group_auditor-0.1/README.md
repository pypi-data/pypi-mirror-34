# Security Group Auditor

A Python security group auditor that will scan all your AWS regions and
will return the security group rules in a CSV file to easily audit.

## Requirements
    - boto3==1.7.62
    - pandas==0.23.3
    - awscli

## Configuring awscli
- Install aws cli from pip
- Run `aws configure` and inject the `AWS_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY`
- Region can be `us-east-1` but not required

### How to use
- Clone the repo into your existing project or use it as a new project
- Create a new file `audit.py` and add the following code
    ```
    from security_group_auditor import security_group_auditor

    security_group_auditor(regions="(Required) ALL",
                       vpc_ids=["(Optional) list of vpc ids | None"],
                       protocol="(Optional) TCP | UDP | ICMP",
                       cidr=["(Optional) list of CIDR's that you want to search"],
                       user_id=["(Optional) list of AWS account ID's"],
                       sg_ids=["(Optional) list of security group ID's"],
                       audit_file_path="(Required) Path to .csv file where you want to store data. Ex: /home/user/data.csv")
    ```
- After executing you can see the csv file in the `audit_file_path` specified

### CSV Output Format:

`CIDR | Description | Group ID | Name | Port | Region | VPC_ID`