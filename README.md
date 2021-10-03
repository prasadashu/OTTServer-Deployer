# OTTServer-Deployer
Ansible repo to deploy OTTServer

# Install Ansible
sudo yum install -y ansible

# Clone the repo
git clone -b dedicated_user https://github.com/prasadashu/OTTServer-Deployer.git

# How to execute playbook
ansible-playbook deploy_ottserver.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"