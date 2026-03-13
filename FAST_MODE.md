# OpenClaw Fast Mode Guide

> OpenClaw v2026.3.12 introduced Fast Mode for GPT-5.4 and Claude.

## What is Fast Mode?

Fast Mode optimizes API requests for speed:
- **GPT-5.4**: Request shaping for faster responses
- **Claude**: Maps to Anthropic `service_tier` for priority routing

## How to Enable

### CLI
```bash
/openclaw fast
```

### Control UI
Dashboard v2 → Settings → Fast Mode toggle

### Per-Model Config
```json
{
  "params": {
    "fastMode": true
  }
}
```

## When to Use Fast Mode

| Use Case | Recommended |
|----------|-------------|
| Quick Q&A | ✅ Yes |
| Code suggestions | ✅ Yes |
| Complex reasoning | ❌ No |
| Long documents | ❌ No |

## Trade-offs

- **Faster** response times
- **Lower** context awareness
- **More** token usage in some cases

## Captain vs Abdicator on Fast Mode

| Mode | Behavior |
|------|----------|
| **Captain** | Knows when to use fast vs full mode |
| **Architect** | Configures per-task defaults |
| **Abdicator** | Just enables it everywhere |

> The first two are using AI. The third is being used by AI.

---

*Updated for OpenClaw v2026.3.12*
