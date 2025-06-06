# Harness

## Overview

The Harness source is migrated from [Faros
AI](https://github.com/faros-ai/airbyte-connectors/tree/main/sources/harness-source).
Please file any support requests on that repo to minimize response time from the
maintainers. The source supports both Full Refresh and Incremental syncs. You
can choose if this source will copy only the new or updated data, or all rows in
the tables and columns you set up for replication, every time a sync is run.

### Output schema

Only one stream is currently available from this source:

- [Organization](https://apidocs.harness.io/tag/Organization#operation/getOrganizationList)

If there are more endpoints you'd like Faros AI to support, please [create an
issue.](https://github.com/faros-ai/airbyte-connectors/issues/new)

### Features

| Feature           | Supported? |
| :---------------- | :--------- |
| Full Refresh Sync | Yes        |
| Incremental Sync  | No         |
| SSL connection    | No         |
| Namespaces        | No         |

### Performance considerations

The Harness source should not run into Harness API limitations under normal
usage. Please [create an
issue](https://github.com/faros-ai/airbyte-connectors/issues/new) if you see any
rate limit issues that are not automatically retried successfully.

## Getting started

### Requirements

- Harness Account Id
- Harness API Key
- Harness API URL, if using a self-hosted Harness instance

Please follow the [their documentation for generating a Harness API
Key](https://ngdocs.harness.io/article/tdoad7xrh9-add-and-manage-api-keys#harness_api_key).

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                                   | Subject                                              |
| :------ | :--------- | :------------------------------------------------------------- | :--------------------------------------------------- |
| 0.2.10 | 2025-05-24 | [60735](https://github.com/airbytehq/airbyte/pull/60735) | Update dependencies |
| 0.2.9 | 2025-05-10 | [59259](https://github.com/airbytehq/airbyte/pull/59259) | Update dependencies |
| 0.2.8 | 2025-04-26 | [58803](https://github.com/airbytehq/airbyte/pull/58803) | Update dependencies |
| 0.2.7 | 2025-04-19 | [58194](https://github.com/airbytehq/airbyte/pull/58194) | Update dependencies |
| 0.2.6 | 2025-04-12 | [57723](https://github.com/airbytehq/airbyte/pull/57723) | Update dependencies |
| 0.2.5 | 2025-04-05 | [57084](https://github.com/airbytehq/airbyte/pull/57084) | Update dependencies |
| 0.2.4 | 2025-03-29 | [56676](https://github.com/airbytehq/airbyte/pull/56676) | Update dependencies |
| 0.2.3 | 2025-03-22 | [56037](https://github.com/airbytehq/airbyte/pull/56037) | Update dependencies |
| 0.2.2 | 2025-03-08 | [55506](https://github.com/airbytehq/airbyte/pull/55506) | Update dependencies |
| 0.2.1 | 2025-03-01 | [43874](https://github.com/airbytehq/airbyte/pull/43874) | Update dependencies |
| 0.2.0 | 2024-10-05 | [46485](https://github.com/airbytehq/airbyte/pull/46485) | Migrate to Manifest-only |
| 0.1.10 | 2024-08-03 | [43172](https://github.com/airbytehq/airbyte/pull/43172) | Update dependencies |
| 0.1.9 | 2024-07-27 | [42735](https://github.com/airbytehq/airbyte/pull/42735) | Update dependencies |
| 0.1.8 | 2024-07-20 | [42221](https://github.com/airbytehq/airbyte/pull/42221) | Update dependencies |
| 0.1.7 | 2024-07-13 | [41851](https://github.com/airbytehq/airbyte/pull/41851) | Update dependencies |
| 0.1.6 | 2024-07-10 | [41426](https://github.com/airbytehq/airbyte/pull/41426) | Update dependencies |
| 0.1.5 | 2024-07-09 | [41101](https://github.com/airbytehq/airbyte/pull/41101) | Update dependencies |
| 0.1.4 | 2024-07-06 | [40788](https://github.com/airbytehq/airbyte/pull/40788) | Update dependencies |
| 0.1.3 | 2024-06-25 | [40464](https://github.com/airbytehq/airbyte/pull/40464) | Update dependencies |
| 0.1.2 | 2024-06-22 | [40051](https://github.com/airbytehq/airbyte/pull/40051) | Update dependencies |
| 0.1.1 | 2024-05-20 | [38392](https://github.com/airbytehq/airbyte/pull/38392) | [autopull] base image + poetry + up_to_date |
| 0.1.0 | 2023-10-10 | [31103](https://github.com/airbytehq/airbyte/pull/31103) | Migrate to low code |
| 0.1.23  | 2021-11-16 | [153](https://github.com/faros-ai/airbyte-connectors/pull/153) | Add Harness source and Faros destination's converter |

</details>
