# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## 2.1.0 - 2018-02-19

### Added

- Slack announcements will now include any line that starts with `cc`.
  This can be used to ping stakeholders whenever your commit gets released.
  Use it like this:

  ```
  Add some foo bar feature

  Closes #123

  cc @john.doe, @analytics (might have impact on sales)
  ```
- Datadog events now include the target environment's name in a tag.
- The Slack integration got a bunch of automated tests.

### Changed

- The Slack message received some tiny cosmetic adjustments.
- Merge commits are now filtered from the changelog posted on Slack.
- Bumped Python dependency versions

### Fixed

- Fixed a long-standing bug that caused the Slack and Datadog hooks to fail
  when the deployment switched branches,
  and a changelog couldn't be generated.
  Now at least the new latest commit will be posted (along with an explanation,)
  and no exceptions will be thrown.
- And fixed another long-standing bug,
  where releasers' names would be repeated
  every time a new job updated the Slack message,
  like so: `Releaser: @john.doe & @john.doe & @john.doe & @john.doe`
- Exceptions and tracebacks will now be printed at the correct lines,
  not at the end of all output.
- The Sentry hook won't fail anymore
  if the URL's trailing slash is missing.

## 2.0.2 - 2018-01-22

### Fixed

- Datadog hook is now functional. 😩

## 2.0.1 - 2018-01-22

### Fixed

- Datadog hook is now properly initialized.

## 2.0.0 - 2018-01-22

### Added

- Send release events to Datadog with `--datadog-key` or `CRANE_DATADOG_KEY`.

### Changed

- Update from Alpine 3.5 to 3.7
- Bumped Python dependency versions

### Removed

Compatibility with v0.x option names.
These options were deprecated in v1.0.0 and are now not usable anymore.
The full list is as follows

- `--rancher-url` renamed to `--url`
- `--access` renamed to `--access-key`
- `--secret` renamed to `--secret-key`
- `--project` renamed to `--env`
- `--no-finish-upgrade` renamed to `--manual-finish`
- `RANCHER_PROJECT_ID` renamed to `RANCHER_ENV_ID`
- `RANCHER_SERVICE_ID` renamed to `RANCHER_SERVICE_NAME`
- `RANCHER_BATCH_SIZE` renamed to `CRANE_BATCH_SIZE`
- `RANCHER_BATCH_INTERVAL` renamed to `CRANE_BATCH_INTERVAL`
- `RANCHER_START_FIRST` renamed to `CRANE_START_FIRST`
- `RANCHER_SERVICE_IMAGE` renamed to `CRANE_NEW_IMAGE`
- `CRANE_NO_FINISH_UPGRADE` renamed to `CRANE_MANUAL_FINISH`

## 1.1.3 - 2017-10-16

### Fixed

- Default value of `--service`/`RANCHER_SERVICE_NAME` is now `['app']`
  as originally intended instead of `['a', 'p', 'p']`.

## 1.1.2 - 2017-10-13

### Fixed

- `--new-image`/`CRANE_NEW_IMAGE` marked as required,
  since the code was just erroring without it.

## 1.1.1 - 2017-10-11

### Fixed

- One line length static analysis violation.

## 1.1.0 - 2017-10-11

### Added

- Support for passing an auth token in generic webhooks
  with `--webhook-token` or `CRANE_WEBHOOK_TOKEN`.

## 1.0.0 - 2017-10-11

Complete project rewrite, but backwards compatibility with 0.x should be retained.

### Added

- A hooks/plugin system, which can be used to easily extend crane with code.
  - Sentry, Slack, and generic webhook hooks are included.

### Changed

- Output is now way more readable, and makes use of the hook system
  - And also includes cute emoticons
- Upgrade of multiple services now happens in parallel
- Failures are handled a bit more gracefully

### Deprecated

Some 0.x options and environment variables are still supported
but have been renamed and will be removed within the next few weeks.
Please pin to the `kiwicom/crane:1` image
if you don't want to update your configuration.

- `--rancher-url` renamed to `--url`
- `--access` renamed to `--access-key`
- `--secret` renamed to `--secret-key`
- `--project` renamed to `--env`
- `--no-finish-upgrade` renamed to `--manual-finish`
- `RANCHER_PROJECT_ID` renamed to `RANCHER_ENV_ID`
- `RANCHER_SERVICE_ID` renamed to `RANCHER_SERVICE_NAME`
- `RANCHER_BATCH_SIZE` renamed to `CRANE_BATCH_SIZE`
- `RANCHER_BATCH_INTERVAL` renamed to `CRANE_BATCH_INTERVAL`
- `RANCHER_START_FIRST` renamed to `CRANE_START_FIRST`
- `RANCHER_SERVICE_IMAGE` renamed to `CRANE_NEW_IMAGE`
- `CRANE_NO_FINISH_UPGRADE` renamed to `CRANE_MANUAL_FINISH`
