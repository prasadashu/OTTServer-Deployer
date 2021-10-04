# OTTServer-Deployer
The project is in association with https://github.com/official-srv-modak/OTTServer.

This is an Ansible repo to deploy OTTServer.

## How to deploy OTTServer?

### 1. Install Ansible
```shell
sudo yum install -y ansible
```

### 2. Clone the repo
```shell
git clone -b dedicated_user https://github.com/prasadashu/OTTServer-Deployer.git
```

### 3. Execute playbook
```shell
ansible-playbook deploy_ottserver.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"
```