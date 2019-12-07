#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
image_name=$DOCKER_USER/miph:$TAG
echo $image_name
docker build -f Dockerfile -t $image_name .
docker push $image_name
