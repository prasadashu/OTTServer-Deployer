# OTTServer-Dockerized-Deployer
The project is in association with https://github.com/official-srv-modak/OTTServer.
<p align="center"><img src="./docs/modakflix_banner.png" width="550"/></p>


Repository to deploy containerized OTTServer through Ansible.

## How to deploy OTTServer?

- Install Ansible in RedHat based distros.
```shell
sudo yum install -y ansible
```

- Clone this repo.
```shell
git clone https://github.com/prasadashu/OTTServer-Deployer.git
```

- Execute the playbook.
```shell
ansible-playbook deploy_dockerized_ottserver.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}"
```

- Access the home page through `port 5000`.

## Repository File Structure

```
.
├── deploy_dockerized_ottserver.yml
├── host_vars
│   └── db_web_server.yml
├── inventory
│   └── inventory.txt
├── library
│   └── custom_debug.py
├── mariadb
│   └── Dockerfile
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── php-apache-web
│   └── Dockerfile
├── README.md
├── roles
│   ├── firewall_setup
│   │   └── tasks
│   │       └── main.yml
│   ├── python_dependency
│   │   └── tasks
│   │       └── main.yml
│   ├── setup_dependencies
│   │   └── tasks
│   │       └── main.yml
│   ├── setup_scripts
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       ├── db.php.j2
│   │       └── path.php.j2
│   └── spin_up_docker
│       └── tasks
│           └── main.yml
├── templates
│   └── docker-compose.yml.j2
└── TO_DO.txt

```

## Repository details

- Docker is configured to run three services.
    - `web` service to run the **web server**.
    - `db` service to run the **db server**.
    - `nginx` service to run the **load balancer**.
 
- By default, three web containers are set to spin up when the server is deployed.
- These web containers are being load balanced through an `NginX` container.
- The `NginX` container is running on `port 5000` and so should be the port to access the home page.

- One can check the running containers in the background using the command below.
```shell
docker ps
```

- Firewall has been enabled as part of the deployment process.

- Firewall enabled ports can be viewed using the below command.
```shell
firewall-cmd --list-all
```

- Scaling up of containers can be achieved through the command below.
```shell
docker-compose up -d --scale <service_name_1>=<number of containers> <service_name_1>=<number of containers>
```
- An example to scale web server containers to 5.
```shell
docker-compose up -d --scale web=5
```

## Configuration details

- The deployment can be configured at `host_vars/db_web_server.yml`.

- `ansible_connection` is set to `local`.
    - Other possible value `ssh`
    - Do not use `winrm` as the repo is configured for RedHat based distros.
    
- The Linux user, group and password for OTTServer admin can be changed.
    - `flix_admin` to change the Linux user.
    - `flix_admin_group` to change the Linux group.
    - `flix_admin_pass` to change the Linux user password.
    
- The database user and credentials can be configured.
    - `mysql_db` to change the DB name.
    - `mysql_user` to change the DB user.
    - `mysql_password` to change the DB user password.
    - `mysql_root_password` to change the DB root password.
    
- The hosted path for the server can be changed through `path_server`.

- A password salt value can be changed through `password_salt`.


## Encrypting using Ansible Vault
The file `host_vars/db_web_server.yml` containing all the credentials is set in plain text format for display purposes. However, this file can be encrypted using Ansible Vault.

- To encrypt the file use the command
```shell
ansible-vault encrypt host_vars/db_web_server.yml
```

- To view the encrypted file use the command
```shell
ansible-vault view host_vars/db_web_server.yml
```

- To run the playbook with the encrypted vault file
```shell
ansible-playbook deploy_dockerized_ottserver.yml -i inventory/inventory.txt --extra-vars "{'host':'db_web_server'}" --ask-vault-pass
```

## Version details
The below tech stack versions have been used to test the project:-

- OS: `CentOS Linux release 7.7.1908 (Core)`

- Ansible: `ansible 2.9.25`

- Web **Dockerfile** base image: `php:7.2-apache`
    - Apache: `2.4.38 (Debian)`
    - PHP: `7.2.34 (cli)`
    
- DB **Dockerfile** base image: `mariadb:10`
    - MariaDB: `mariadb  Ver 15.1 Distrib 10.6.4-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2`

- NginX **Dockerfile** base image: `nginx:1.21`
    - NginX: `nginx/1.21.3`
    
- Docker compose: `docker-compose version 1.29.2`

- Docker version: `Docker version 19.03.6, build 369ce74a3c`
