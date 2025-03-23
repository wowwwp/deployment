# deployment

The deployment url is http://13.54.117.136:3000. 

## Set-up

### Pre-requsites
1) Docker
2) Docker Compose

### asr-api
1) Navigate to the `asr` folder
2) Run `docker build -t asr-api .` command
3) If build is successful, run `docker run -p 127.0.0.1:8001:8001 asr-api`
4) The flask app is accessible at `http://localhost:8001`. To test the app, run `curl http://localhost:8001/ping`. The expected output is `pong`

### elastic-backend
1) Navigate to the `elastic-backend` directory

#### To start the elasticsearch cluster
1) Run `docker compose up`. Ror older docker versions, use `docker-compose up`

#### To create an index
1) Run `docker build -t cv-index-load .` to build the image
2) Next, run `docker run cv-index-load`
3) Run `curl -X GET "localhost:9200/_cat/indices?v"`. 

### search-ui
1) Navigate to the `search-ui` directory
2) Run `docker build -t search-ui-image .` to build the image. **Ensure the image is named search-ui-image**
3) Run `docker compose up`. For older docker versions, use `docker-compose up`
4) If successful, UI will run on `http://localhost:3000`
