# Product test code
```sh
curl -X POST "http://3.80.190.172:4000/graphql" \
-H "Content-Type: application/json" \
--data '{"query":"{ products { id name price available_units } }"}'
