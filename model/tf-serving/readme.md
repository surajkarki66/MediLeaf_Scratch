# To run locally:

- `docker pull tensorflow/serving`

# To start docker container: 

- `docker run -it -v /home/rgrupesh/nHack/tf:/tf_serving -p 8601:8601 --entrypoint bin/bash tensorflow/serving`

# To serve model:

- `tensorflow_model_server --rest_api_port=8601 --model_name=vgg_model --model_base_path=/tf_serving/model/`
