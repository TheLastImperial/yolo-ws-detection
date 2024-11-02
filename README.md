# YOLO Web Service Detection

YOLO Web Service Detection is a REST API to send a image and get back all the objects found as a JSON.

## Routes detections

<details>
 <summary>
  <code>POST</code>
  <code><b>/detection</b></code>
  <code>(Detect objects on image.)</code>
 </summary>

##### Parameters

> | name    |  type     | data type  | description               |
> |---------|-----------|------------|---------------------------|
> | `image` |  required | File       | Image to detect objects.  |

##### Responses

> | http code     | content-type        | response                                                                           |
> |---------------|---------------------|------------------------------------------------------------------------------------|
> | `200`         | `application/json`  | `{prediction: {label: String, score: float, xyxy: number[4], xyxyn: number[4]}[]}` |

##### Example cURL

> ```javascript
>  curl -F image=@PATH_TO_IMAGE localhost/detection
> ```

</details>

## Using Docker

### Build docker image.

The docker image use `ultralytics/ultralytics:8.3.26` as base image with GPU support.

```bash
docker build -t imperial/yolo-ws-detection:1.0.0 .
```

You can change the base image tag with the `IMAGE_TAG` argument like the next command:

```bash
docker build -t imperial/yolo-ws-detection:1.0.0-cpu --build-arg IMAGE_TAG=8.3.26-cpu .
```

### Run the container.

```bash
docker run --rm -p 8080:80 imperial/yolo-ws-detection:1.0.0-cpu
```

Now you can do request to `localhost:8080/detection`.

> Note: The image default port is `80` but you can change it with the `-p` param.
