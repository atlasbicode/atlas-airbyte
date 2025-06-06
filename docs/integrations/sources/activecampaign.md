# ActiveCampaign

## Sync overview

This source can sync data from the [ActiveCampaign API](https://developers.activecampaign.com/reference/overview). At present this connector only supports full refresh syncs meaning that each time you use the connector it will sync all available records from scratch. Please use cautiously if you expect your API to have a lot of records.

## This Source Supports the Following Streams

- campaigns
- contacts
- lists
- deals
- segments
- forms

### Features

| Feature           | Supported?\(Yes/No\) | Notes |
| :---------------- | :------------------- | :---- |
| Full Refresh Sync | Yes                  |       |
| Incremental Sync  | No                   |       |

### Performance considerations

The connector has a rate limit of 5 requests per second per account.

## Getting started

### Requirements

- ActiveCampaign account
- ActiveCampaign API Key

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                             | Subject        |
| :------ | :--------- | :------------------------------------------------------- | :------------- |
| 0.2.14 | 2025-05-17 | [60626](https://github.com/airbytehq/airbyte/pull/60626) | Update dependencies |
| 0.2.13 | 2025-05-10 | [59872](https://github.com/airbytehq/airbyte/pull/59872) | Update dependencies |
| 0.2.12 | 2025-05-03 | [59306](https://github.com/airbytehq/airbyte/pull/59306) | Update dependencies |
| 0.2.11 | 2025-04-26 | [58745](https://github.com/airbytehq/airbyte/pull/58745) | Update dependencies |
| 0.2.10 | 2025-04-19 | [58273](https://github.com/airbytehq/airbyte/pull/58273) | Update dependencies |
| 0.2.9 | 2025-04-12 | [57654](https://github.com/airbytehq/airbyte/pull/57654) | Update dependencies |
| 0.2.8 | 2025-04-05 | [57168](https://github.com/airbytehq/airbyte/pull/57168) | Update dependencies |
| 0.2.7 | 2025-03-29 | [56626](https://github.com/airbytehq/airbyte/pull/56626) | Update dependencies |
| 0.2.6 | 2025-03-22 | [56092](https://github.com/airbytehq/airbyte/pull/56092) | Update dependencies |
| 0.2.5 | 2025-03-08 | [55357](https://github.com/airbytehq/airbyte/pull/55357) | Update dependencies |
| 0.2.4 | 2025-03-01 | [54855](https://github.com/airbytehq/airbyte/pull/54855) | Update dependencies |
| 0.2.3 | 2025-02-22 | [54227](https://github.com/airbytehq/airbyte/pull/54227) | Update dependencies |
| 0.2.2 | 2025-02-15 | [47196](https://github.com/airbytehq/airbyte/pull/47196) | Update dependencies |
| 0.2.1 | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196) | Bump source-declarative-manifest version |
| 0.2.0 | 2024-08-02 | [42987](https://github.com/airbytehq/airbyte/pull/42987) | Refactor connector to manifest-only format |
| 0.1.11 | 2024-07-27 | [42677](https://github.com/airbytehq/airbyte/pull/42677) | Update dependencies |
| 0.1.10 | 2024-07-20 | [42337](https://github.com/airbytehq/airbyte/pull/42337) | Update dependencies |
| 0.1.9 | 2024-07-13 | [41702](https://github.com/airbytehq/airbyte/pull/41702) | Update dependencies |
| 0.1.8 | 2024-07-10 | [41577](https://github.com/airbytehq/airbyte/pull/41577) | Update dependencies |
| 0.1.7 | 2024-07-10 | [41326](https://github.com/airbytehq/airbyte/pull/41326) | Update dependencies |
| 0.1.6 | 2024-07-06 | [40873](https://github.com/airbytehq/airbyte/pull/40873) | Update dependencies |
| 0.1.5 | 2024-06-27 | [38224](https://github.com/airbytehq/airbyte/pull/38224) | Make connector compatable with the builder |
| 0.1.4 | 2024-06-25 | [40327](https://github.com/airbytehq/airbyte/pull/40327) | Update dependencies |
| 0.1.3 | 2024-06-22 | [40046](https://github.com/airbytehq/airbyte/pull/40046) | Update dependencies |
| 0.1.2 | 2024-06-04 | [38989](https://github.com/airbytehq/airbyte/pull/38989) | [autopull] Upgrade base image to v1.2.1 |
| 0.1.1 | 2024-05-21 | [38511](https://github.com/airbytehq/airbyte/pull/38511) | [autopull] base image + poetry + up_to_date |
| 0.1.0 | 2022-10-25 | [18335](https://github.com/airbytehq/airbyte/pull/18335) | Initial commit |

</details>
