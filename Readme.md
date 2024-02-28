## Build the image

```
docker build --no-cache -t whisper-app . 
```

## Run the container

```
docker run --rm -v "$(pwd):/videos" whisper-app /videos/Your\ Video.mkv base.en
```