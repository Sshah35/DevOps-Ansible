# ansible
ansible project

There are three types of playbooks in each project: webserver, nfsserver and dbserver. 
All three playbooks do the same tasks.
For example: In project webserver, we have mywebservers.yml mywebserver.optimized.yml webserverrole.yml.
mywebservers.yml is the straightforward playbook derived from mywebserver.txt outline.
mywebserver.optimized.yml is optimized virsion of the previous playbook. Changes includes using of variables and handlers.
webserverrole.ym is the role based playbook which include all folders in the redhat.apachewebser folder hiararchy. running webserverrole.ym is enough to trigger the roles.
This logical architecture is enforced on other projects as well.

These project consists of two separate playbooks: mywebserver.optimized.yml and webserverrole.yml. 
Mywebserver.optimized.yml is single playbook that installs apachewebserver on the remote system. creates client.example.com virtual host and copies compressed index.html file. It copies servers.conf configuration file and add httpd to firewall. 
Webserverrole.yml is the Master playbook that runs all roles in the redhat.apachewebserver. This playbook does the same jobs as mywebserver.optimized.yml. 

nfsserver.optimized.yml file contains notify section that won't trigger handlers unless the module prior to notify is successful. Make sure that prevous command is successful when testing the playbook.

when testing dbserver playbook, delete all configuration files after removing the mariadb-server and mariadb packages from client. Use rm -rf /var/lib/mysql and rm /etc/my.cnf. If you don't delete previous files, password for the root will stay. Unless you remember the previous password you wont be able to change password for the root. Also, previous database files will stay, which cause an error when creating new one with the same name. So, delete previous config files.

These projects are customized and completed by folowing the linuxacademy.com projects in the "Using Ansible for Configuration Management and Deployments" course. 
