# Random IP Generator as Digital Ocean function

## Deploying the Function

```bash
git clone git@github.com:ihuro/randomips-do-function.git
doctl serverless deploy random-ips-do-function --remote-build
```

## Using the Function

```bash
doctl serverless functions invoke randomips/generate
```