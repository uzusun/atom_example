#!/usr/bin/env bash

#ssh key 생성
sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no vagrant@192.168.0.230
sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no vagrant@192.168.0.231
#sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no root@192.168.0.230
#sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no root@192.168.0.231
