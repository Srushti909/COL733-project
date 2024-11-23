#!/bin/bash

gcloud functions deploy FibonacciPrimeChecker \
    --runtime python39 \
    --trigger-http \
    --allow-unauthenticated \
    --source .
