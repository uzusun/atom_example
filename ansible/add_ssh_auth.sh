#!/usr/bin/env bash

#ssh key 생성
sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no vagrant@192.168.0.16
sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no vagrant@192.168.0.17
sshpass -p vagrant ssh -T -o StrictHostKeyChecking=no vagrant@192.168.0.18
