#!/bin/bash
ip addr del $1/32 dev dummy0
