# MediaCore PHP SDK

## Install

```bash
# from your PHP app (path repository)
composer config repositories.mediacore path /absolute/path/to/mediacore/sdk/php
composer require mediacore/sdk:@dev
```

Or copy `sdk/php` into your project and add the PSR-4 autoload from `composer.json`.

## Usage

```php
<?php
use MediaCore\Client;

$client = new Client('dev-api-key-change-me', 'http://localhost:8000');
$meta = $client->analyze('https://example.com/video.mp4');
$job = $client->download($meta['url'] ?? 'https://example.com/video.mp4');
$done = $client->wait($job['job_id']);
echo $done['status'], ' ', ($done['result_path'] ?? ''), PHP_EOL;
```
