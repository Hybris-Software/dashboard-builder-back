#!/usr/bin/env bash

/scripts/docker/wait_for_it.sh $DB_HOST:$DB_PORT -s -- $@