FROM php:7.2-apache
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN apt-get update && apt-get upgrade -y
RUN groupadd flix_admin_group
RUN useradd -ms /bin/bash flix_admin
RUN usermod -a -G flix_admin_group flix_admin
WORKDIR /var/www/html/