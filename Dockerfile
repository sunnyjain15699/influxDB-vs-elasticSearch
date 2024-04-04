docker run \
 --name influxdb2 \
 --publish 8086:8086 \
 --mount type=volume,source=influxdb2-data,target=/var/lib/influxdb2 \
 --mount type=volume,source=influxdb2-config,target=/etc/influxdb2 \
 --env DOCKER_INFLUXDB_INIT_MODE=setup \
 --env DOCKER_INFLUXDB_INIT_USERNAME=admin \
 --env DOCKER_INFLUXDB_INIT_PASSWORD=Sunny@15699 \
 --env DOCKER_INFLUXDB_INIT_ORG=influxdb \
 --env DOCKER_INFLUXDB_INIT_BUCKET=doc \
 influxdb:2

