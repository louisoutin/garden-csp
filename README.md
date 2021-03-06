# Garden Layout Planner 
Garden Layout Planner using Greedy Algorithms (taken and adapted from greedypacker repo).

## Usage

Run the http server

```shell script
python app.py
```

Swagger documentation: http://127.0.0.1:8080/ui/

CURL example

```shell script
curl --location --request POST 'http://localhost:8080/layout/recommend' \
--header 'Content-Type: application/json' \
--data-raw '{
    "garden": {
        "width": 5,
        "height": 3
    },
    "vegetables_inventory": {
        "vegetables": [1,2]
    },
    "wanted_proposals": 1
}'
```

### Using docker
```shell script
# build app image
docker build -t garden-csp .
# run app container
docker run -p8080:8080 -t garden-csp
```

## Constraints

#### Alignment constraint
Enforce that vegetables are aligned on the layout.

#### Space filling constraint
Enforce a minimum filling ratio to be respected on the layout.
