FROM ubuntu:16.04

RUN apt-get update && apt-get install -y wget && cd /root &&                  \
    wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&\
    dpkg -i /root/erlang-solutions_1.0_all.deb && rm -f /root/erlang-solutions_1.0_all.deb &&\
    apt-get update
RUN apt-get install -y openssh-server sudo python python-setuptools net-tools  \
    iproute2 vim init-system-helpers bash-completion sssd sssd-ldap sssd-krb5  \
    libpam-modules libpam-runtime libpam-ldap libpam-krb5 libpam-sss           \
    libpam-passwdqc libnss-ldapd libnss-sss python-sss python-ldap ldap-utils  \
    libpython2.7-stdlib passwd libkrb5-3 krb5-user krb5-k5tls libsmbclient     \
    libsmbclient-dev auth-client-config auditd libaudit-dev libaudit-common    \
    language-pack-en iputils-ping module-init-tools                            \
    erlang=1:19.3-1 erlang-base-hipe=1:19.3-1 erlang-runtime-tools=1:19.3-1    \
    erlang-asn1=1:19.3-1 erlang-syntax-tools=1:19.3-1 erlang-dev=1:19.3-1      \
    erlang-appmon=1:19.3-1 erlang-common-test=1:19.3-1 erlang-corba=1:19.3-1   \
    erlang-crypto=1:19.3-1 erlang-debugger=1:19.3-1 erlang-dialyzer=1:19.3-1   \
    erlang-diameter=1:19.3-1 erlang-edoc=1:19.3-1 erlang-eldap=1:19.3-1        \
    erlang-erl-docgen=1:19.3-1 erlang-et=1:19.3-1 erlang-eunit=1:19.3-1        \
    erlang-ic=1:19.3-1 erlang-inets=1:19.3-1 erlang-inviso=1:19.3-1            \
    erlang-megaco=1:19.3-1 erlang-observer=1:19.3-1 erlang-odbc=1:19.3-1       \
    erlang-os-mon=1:19.3-1 erlang-os-mon=1:19.3-1 erlang-parsetools=1:19.3-1   \
    erlang-percept=1:19.3-1 erlang-public-key=1:19.3-1 erlang-reltool=1:19.3-1 \
    erlang-snmp=1:19.3-1 erlang-ssh=1:19.3-1 erlang-ssl=1:19.3-1               \
    erlang-test-server=1:19.3-1 erlang-toolbar=1:19.3-1 erlang-tools=1:19.3-1  \
    erlang-tv=1:19.3-1 erlang-typer=1:19.3-1 erlang-webtool=1:19.3-1           \
    erlang-wx=1:19.3-1  erlang-xmerl=1:19.3-1 erlang-mnesia=1:19.3-1           \
    erlang-pman=1:19.3-1 erlang-gs=1:19.3-1  erlang-examples=1:19.3-1          \
    erlang-ic-java=1:19.3-1 erlang-src=1:19.3-1

ADD deps/* /var/tmp/deps/
RUN cd /var/tmp/deps/elementtree-1.2-20040618; python setup.py install &&      \
    cd /var/tmp/deps/meld3-1.0.2; python setup.py install &&                   \
    cd /var/tmp/deps/supervisor-3.3.1; python setup.py install &&              \
    rm -rf /var/tmp/deps

## Generate a random password for root user for better security.
RUN passwd -l root

## Create a bluedata system user
RUN useradd -r -m -s /bin/bash bluedata; mkdir /home/bluedata/.ssh;            \
      chmod go-rx /home/bluedata/.ssh; chown -R bluedata:bluedata /home/bluedata
RUN echo 'Defaults:bluedata !requiretty\n\nbluedata ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/bluedata

## Don't require tty for any sudo commands.
RUN sed -i  's/Defaults    requiretty/#Defaults    requiretty/' /etc/sudoers

# RHEL is missing /sbin in the path. But, its okay to redefine for CentOS too.
ENV PATH $PATH:/sbin

## Limits configuration.
ADD ./limits-90-nproc.conf /etc/security/limits.d/90-nproc.conf

## Configuring SSH server.
RUN mkdir /var/run/sshd
RUN echo "y" | ssh-keygen -P '' -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN echo "y" | ssh-keygen -P '' -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN sed -i '/pam_loginuid.so/c session    optional     pam_loginuid.so'  /etc/pam.d/sshd
RUN sed -i '/^#PermitRootLogin yes$/d; $a PermitRootLogin no' /etc/ssh/sshd_config

RUN mkdir -p /etc/bluedata
ADD base_img_version /etc/bluedata/base_img_version
RUN chown -R bluedata:bluedata /etc/bluedata

## Configure supervisord
ADD supervisord.conf /etc/

## BlueData Management expects the supervisord to be at /usr/bin
RUN ln -sf /usr/local/bin/supervisord /usr/bin/supervisord

## Start default services (sshd, rsyslog etc.) at container bootup.
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
