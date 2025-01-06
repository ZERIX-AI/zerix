# zerix-client

A Zerix App Service-API Client for PHP applications.

## Installation

```bash
composer require zerix/zerix-client
```

## Usage

### Basic Client Usage

```php
use ZerixClient;

$api_key = "your_api_key";
$client = new ZerixClient($api_key);
```

### Completion Client

```php
use CompletionClient;

$client = new CompletionClient($api_key);

// Create completion message
$response = $client->create_completion_message(
    ['query' => "What's the weather like today?"],  // inputs
    'blocking',                                     // response_mode
    'user_123',                                    // user
    null                                           // files
);
```

### Chat Client

```php
use ChatClient;

$client = new ChatClient($api_key);

// Create chat message
$response = $client->create_chat_message(
    [],                 // inputs
    "Hello!",          // query
    "user_123",        // user
    "blocking",        // response_mode
    null,              // conversation_id
    null               // files
);

// Get conversation list
$conversations = $client->get_conversations(
    "user_123",        // user
    null,              // first_id
    null,              // limit
    null               // pinned
);

// Get messages in a conversation
$messages = $client->get_conversation_messages(
    "user_123",        // user
    "conversation_123" // conversation_id
);

// Rename conversation
$response = $client->rename_conversation(
    "conversation_123", // conversation_id
    "New Name",        // name
    false,             // auto_generate
    "user_123"         // user
);

// Delete conversation
$response = $client->delete_conversation("conversation_123", "user_123");

// Get message suggestions
$suggestions = $client->get_suggestions("message_123", "user_123");

// Stop message generation
$response = $client->stop_message("task_123", "user_123");

// Audio to text conversion
$audio_file = ['tmp_name' => '/path/to/file', 'name' => 'audio.mp3'];
$response = $client->audio_to_text($audio_file, "user_123");
```

### Workflow Client

```php
use WorkflowClient;

$client = new WorkflowClient($api_key);

// Run workflow
$response = $client->run(
    ["input" => "your input"],  // inputs
    "streaming",                // response_mode
    "user_123"                 // user
);

// Stop workflow
$response = $client->stop("task_123", "user_123");
```

### File Operations

```php
use ZerixClient;

$client = new ZerixClient($api_key);

// Upload file
$files = [
    'tmp_name' => '/path/to/file',
    'name' => 'example.jpg'
];
$response = $client->file_upload("user_123", $files);

// Text to Audio
$response = $client->text_to_audio(
    "Text to convert",    // text
    "user_123",          // user
    false                // streaming
);
```

### Other Operations

```php
// Get application parameters
$parameters = $client->get_application_parameters("user_123");

// Send message feedback
$response = $client->message_feedback("message_123", "like", "user_123");

// Get metadata
$meta = $client->get_meta("user_123");
```

## API Reference

The client provides the following main classes:

- `ZerixClient`: Base client with core functionality
- `CompletionClient`: For completion-related operations
- `ChatClient`: For chat-related operations
- `WorkflowClient`: For workflow-related operations

Each client class extends the base `ZerixClient` and provides specific methods for interacting with different aspects of the Zerix.AI API.

## License

MIT
