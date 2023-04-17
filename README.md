# Getting Started

inside the API repo

`docker build -t my-flask-app .`

`docker run -p 5001:5001 my-flask-app`

You should then be able to access your Flask app by visiting http://localhost:5001 in your web browser / postman etc!

## How would I expand on that

### 1. Quality of life & better organization for the code
- Implement Swagger UI to provide a user-friendly interface for API documentation.
- Add data validation using a library like Pydantic to ensure that data sent to the API is valid and conforms to the expected data types.
- Refactor the codebase into modules or packages based on functionality similar to how Django breaks project into apps!
- Add unit tests to the codebase to ensure that the API is functioning as intended and to catch any regressions that might be introduced with future changes.

### 2. Additional improvements
- Adding rate limiting to the API to prevent abuse or excessive usage.
- Implementing robust monitoring and alerting using a tool like Sentry to be notified of errors or performance issues in real-time.

### 3. Scaling, how we can tackle supporting 1 million daily requests?
- Scaling the API horizontally using a load balancer and multiple instances of the application running in containers.
- Utilizing a container orchestration tool like Kubernetes to manage the deployment and scaling of the application.
- Compare k8s to running the API in lambdas (I'd prefer lambda if we needed to scale up and down frequently) 
    - I'll compare the response time and cost using an A/B test (of course, I'll need to estimate the pricing, but the real world is always different from our estimates).

## Sample API Call
Request 

```bash
curl --location 'http://127.0.0.1:5001/predict' \
--header 'Content-Type: application/json' \
--data '{
    "fecha_dato": "2016-06-28",
    "ncodpers": 15889,
    "ind_empleado": "F",
    "pais_residencia": "ES",
    "sexo": "V",
    "age": 56,
    "fecha_alta": "1995-01-16",
    "ind_nuevo": 0,
    "antiguedad": 256,
    "indrel": 1,
    "ult_fec_cli_1t": "",
    "indrel_1mes": 1,
    "tiprel_1mes": "A",
    "indresi": "S",
    "indext": "N",
    "conyuemp": "N",
    "canal_entrada": "KAT",
    "indfall": "N",
    "tipodom": 1,
    "cod_prov": 28,
    "nomprov": "MADRID",
    "ind_actividad_cliente": 1,
    "renta": 326124.9,
    "segmento": "01 - TOP"
}'
```

Response

```json
{
    "predictions": [
        [
            0.02228504978120327,
            0.009483921341598034,
            0.012643084861338139,
            0.010813886299729347,
            0.010360412299633026,
            0.011266155168414116,
            0.015922246500849724,
            0.021705755963921547,
            0.013277443125844002,
            0.028446529060602188,
            0.22157259285449982,
            0.01825362630188465,
            0.02464400604367256,
            0.016757681965827942,
            0.009829225949943066,
            0.13555818796157837,
            0.05160053074359894,
            0.02482762187719345,
            0.009937100112438202,
            0.03692570701241493,
            0.13185006380081177,
            0.1620391607284546
        ]
    ]
}
```