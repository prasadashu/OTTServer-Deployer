# OTTServer-Deployer
Ansible repo to deploy OTTServer

# Install Ansible
```shell
sudo yum install -y ansible
```

# Clone the repo
```shell
git clone -b dedicated_user https://github.com/prasadashu/OTTServer-Deployer.git
```

# How to execute playbook
```shell
ansible-playbook deploy_ottserver.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"
```