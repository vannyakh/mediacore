<?php

declare(strict_types=1);

namespace MediaCore;

/**
 * Thin MediaCore PHP client for the permitted download API.
 *
 * Install: composer require mediacore/sdk:@dev  (path repo) or
 *   composer config repositories.mediacore path ../sdk/php && composer require mediacore/sdk:@dev
 */
final class Client
{
    private string $baseUrl;
    private string $apiKey;

    public function __construct(string $apiKey, string $baseUrl = 'http://localhost:8000')
    {
        $this->apiKey = $apiKey;
        $this->baseUrl = rtrim($baseUrl, '/');
    }

    /** @return array<string, mixed> */
    public function analyze(string $url): array
    {
        return $this->request('POST', '/v1/analyze', ['url' => $url]);
    }

    /** @return array<string, mixed> */
    public function download(string $url, string $format = 'original'): array
    {
        return $this->request('POST', '/v1/download', ['url' => $url, 'format' => $format]);
    }

    /** @return array<string, mixed> */
    public function job(string $jobId): array
    {
        return $this->request('GET', '/v1/jobs/' . rawurlencode($jobId));
    }

    /**
     * @return array<string, mixed>
     */
    public function wait(string $jobId, float $timeout = 120.0, float $interval = 0.5): array
    {
        $deadline = microtime(true) + $timeout;
        $last = [];
        while (microtime(true) < $deadline) {
            $last = $this->job($jobId);
            $status = (string) ($last['status'] ?? '');
            if (in_array($status, ['completed', 'failed', 'cancelled'], true)) {
                return $last;
            }
            usleep((int) ($interval * 1_000_000));
        }
        throw new \RuntimeException("job {$jobId} did not finish within {$timeout}s");
    }

    /** @return list<array<string, mixed>> */
    public function providers(): array
    {
        /** @var list<array<string, mixed>> $rows */
        $rows = $this->request('GET', '/v1/providers');
        return $rows;
    }

    /**
     * @param array<string, mixed>|null $body
     * @return array<string, mixed>|list<array<string, mixed>>
     */
    private function request(string $method, string $path, ?array $body = null): array
    {
        $ch = curl_init($this->baseUrl . $path);
        if ($ch === false) {
            throw new \RuntimeException('curl_init failed');
        }
        $headers = [
            'Content-Type: application/json',
            'X-API-Key: ' . $this->apiKey,
        ];
        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_CUSTOMREQUEST => $method,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT => 60,
        ]);
        if ($body !== null) {
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body, JSON_THROW_ON_ERROR));
        }
        $raw = curl_exec($ch);
        $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if ($raw === false) {
            $err = curl_error($ch);
            curl_close($ch);
            throw new \RuntimeException('request failed: ' . $err);
        }
        curl_close($ch);
        if ($code >= 400) {
            throw new \RuntimeException("API {$code}: {$raw}");
        }
        /** @var array<string, mixed>|list<array<string, mixed>> $decoded */
        $decoded = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        return $decoded;
    }
}
