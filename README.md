# License Plate Repository

[<img src="https://img.shields.io/badge/author-Lucas Faria-yellow?style=flat-square"/>](https://github.com/LucasAlbFar)

API to receive German license plates, store them in a database and retrieve data by two endpoints.

## Endpoints:
* POST /plate
  * Payload: 
    * plate: German license plate;
* GET /plate
* GET /search-plate
  * Parameters: 
    * key: German license plate;
    * levenshtein: Levenshtein distance;

## Environment requirements:
[requirements.txt](https://github.com/LucasAlbFar/license_plate_repo/blob/main/src/requirements.txt)

## Docker compose image buiding:
* Linux command:
  * sudo docker-compose up -d

## Contato:
[<img src="https://img.shields.io/badge/LucasFaria-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lucasalbfar/)
[<img src="https://img.shields.io/badge/lucasalbfar@gmail.com-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:lucasalbfarw@gmail.com)
