# crane

A GitLab CI ready image for Rancher upgrades.

## How to use

- Deploy your application on Rancher manually
- Get a Rancher API key
  - click the `API` button in the environment your app is in, then `Add Environment API key`
  - name it `gitlab/group/project deployment`, or similar
- Go to your application on Rancher, and note the project (environment) ID
  - Example URL: <https://example.com/env/1a81/apps/stacks/1e551/services/1s1456/containers>
    - Project ID: `1a81`, environment ID, starts with `1a`
- Add the Rancher keys as secret variables in the project
  - add the `RANCHER_URL` with the base path of Rancher
  - `RANCHER_ACCESS_KEY`, `RANCHER_SECRET_KEY`, from the keys you created in the API section
  - `RANCHER_PROJECT_ID`, the environment ID
  - <https://gitlab.skypicker.com/group/project/variables>
    
- Edit `.gitlab-ci.yml`


```
stages:
 [...]
 - deploy

variables:
  IMAGE_COMMIT: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

[...]

production:
  stage: deploy
  image: registry.skypicker.com:5005/simone/crane
  variables:
    GIT_STRATEGY: none
  script:
    - crane --new-image $IMAGE_COMMIT --stack locations --service app --service updater
  environment:
    name: production
    url: https://your-app.example.com/                      # Change to the URL of your app, or remove if none
  when: manual
```

## Environment variables and command flags

| CLI flag                | Environment variable        | Required | Default |
| ----------------------- | --------------------------- | -------- | ------- |
| `--rancher-url`         | `RANCHER_URL`               | Yes      |         |
| `--access`              | `RANCHER_ACCESS_KEY`        | Yes      |         |
| `--secret`              | `RANCHER_SECRET_KEY`        | Yes      |         |
| `--project`             | `RANCHER_PROJECT_ID`        | Yes      |         |
| `--service`             | `RANCHER_SERVICE_ID`        | Yes      |         |
| `--new-image`           | `RANCHER_SERVICE_IMAGE`     | No       | None    |
| `--batch-size`          | `RANCHER_BATCH_SIZE`        | No       | 1       |
| `--batch-interval`      | `RANCHER_BATCH_INTERVAL`    | No       | 2       |
| `--start-first`         | `RANCHER_START_FIRST`       | No       | False   |
| `--sidekick`            | `RANCHER_SIDEKICK_NAME`     | No       | None    |
| `--sleep-after-upgrade` | `CRANE_SLEEP_AFTER_UPGRADE` | No       | 60      |
| `--no-finish-upgrade`   | `CRANE_NO_FINISH_UPGRADE`   | No       | False   |
