# Zerix SDKs

Official Zerix API SDKs for multiple programming languages.

## Available SDKs

- [Node.js SDK](#nodejs-sdk)
- [Python SDK](#python-sdk)
- [PHP SDK](#php-sdk)

## Node.js SDK

### Installation

```bash
npm install zerix-client
```

### Basic Usage

```javascript
import { ZerixClient } from 'zerix-client';

const apiKey = "your_api_key";
const client = new ZerixClient(apiKey);
```

[View detailed Node.js SDK documentation](nodejs-client/README.md)

## Python SDK

### Installation

```bash
pip install zerix-client
```

### Basic Usage

```python
from zerix_client import ZerixClient

api_key = "your_api_key"
client = ZerixClient(api_key)
```

[View detailed Python SDK documentation](python-client/README.md)

## PHP SDK

### Installation

```bash
composer require zerix/zerix-client
```

### Basic Usage

```php
use ZerixClient;

$api_key = "your_api_key";
$client = new ZerixClient($api_key);
```

[View detailed PHP SDK documentation](php-client/README.md)

## Common Features

All SDKs support the following features:

### Completion Operations
- Create completion messages
- Support for vision models
- Streaming and blocking response modes

### Chat Operations
- Create chat messages
- Manage conversations
- Message history
- Suggestions and feedback

### Workflow Operations
- Run workflows
- Stop workflow tasks
- Manage workflow responses

### File Operations
- File upload
- Text to Audio conversion
- Audio to Text conversion
- Vision model support

### Other Operations
- Application parameters
- Message feedback
- Metadata retrieval

## Example Use Cases

### Vision Model Usage

```javascript
// Node.js
const response = await client.createCompletionMessage(
  { query: "Describe this image" },
  "user_123",
  false,
  [{
    type: "image",
    transfer_method: "remote_url",
    url: "your_image_url"
  }]
);
```

```python
# Python
files = [{
    "type": "image",
    "transfer_method": "remote_url",
    "url": "your_image_url"
}]
response = client.create_completion_message(
    inputs={"query": "Describe the picture."},
    response_mode="blocking",
    user="user_id",
    files=files
)
```

```php
// PHP
$response = $client->create_completion_message(
    ["query" => "Describe this image"],
    "blocking",
    "user_123",
    [{
        "type" => "image",
        "transfer_method" => "remote_url",
        "url" => "your_image_url"
    }]
);
```

### Streaming Chat

```javascript
// Node.js
const response = await client.createChatMessage(
  {},
  "Hello!",
  "user_123",
  true  // Enable streaming
);
```

```python
# Python
chat_response = chat_client.create_chat_message(
    inputs={},
    query="Hello",
    user="user_id",
    response_mode="streaming"
)
```

```php
// PHP
$response = $client->create_chat_message(
    [],
    "Hello!",
    "user_123",
    "streaming"
);
```

## API Reference

All SDKs provide the following main classes:

- `ZerixClient`: Base client with core functionality
- `CompletionClient`: For completion-related operations
- `ChatClient`: For chat-related operations
- `WorkflowClient`: For workflow-related operations

## License

MIT
