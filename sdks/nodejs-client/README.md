# zerix-client

A Zerix App Service-API Client for Node.js applications.

## Installation

```bash
npm install zerix-client
```

## Usage

### Basic Client Usage

```javascript
import { ZerixClient } from 'zerix-client';

const apiKey = "your_api_key";
const client = new ZerixClient(apiKey);
```

### Completion Client

```javascript
import { CompletionClient } from 'zerix-client';

const client = new CompletionClient(apiKey);

// Create completion message
const response = await client.createCompletionMessage(
  { query: "What's the weather like today?" },  // inputs
  "user_123",                                   // user
  false,                                        // stream
  null                                         // files
);

// Using vision model with remote URL
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

### Chat Client

```javascript
import { ChatClient } from 'zerix-client';

const client = new ChatClient(apiKey);

// Create chat message
const response = await client.createChatMessage(
  {},                // inputs
  "Hello!",         // query
  "user_123",       // user
  false,            // stream
  null,             // conversation_id
  null              // files
);

// Get conversation list
const conversations = await client.getConversations("user_123");

// Get messages in a conversation
const messages = await client.getConversationMessages(
  "user_123",           // user
  "conversation_123"    // conversation_id
);

// Rename conversation
await client.renameConversation(
  "conversation_123",   // conversation_id
  "New Name",          // name
  "user_123",          // user
  false                // auto_generate
);

// Delete conversation
await client.deleteConversation("conversation_123", "user_123");
```

### Workflow Client

```javascript
import { WorkflowClient } from 'zerix-client';

const client = new WorkflowClient(apiKey);

// Run workflow
const response = await client.run(
  { input: "your input" },  // inputs
  "user_123",               // user
  false                     // stream
);

// Stop workflow
await client.stop("task_123", "user_123");
```

### File Operations

```javascript
import { ZerixClient } from 'zerix-client';

const client = new ZerixClient(apiKey);

// Upload file
const formData = new FormData();
formData.append('file', yourFile);
formData.append('user', 'user_123');
const response = await client.fileUpload(formData);

// Text to Audio
const audioResponse = await client.textToAudio(
  "Text to convert",    // text
  "user_123",          // user
  false                // streaming
);

// Audio to Text
const formData = new FormData();
formData.append('audio_file', yourAudioFile);
formData.append('user', 'user_123');
const textResponse = await client.audioToText(formData);
```

### Other Operations

```javascript
// Get application parameters
const parameters = await client.getApplicationParameters("user_123");

// Send message feedback
await client.messageFeedback("message_123", 1, "user_123");

// Get metadata
const meta = await client.getMeta("user_123");
```

## API Reference

The client provides the following main classes:

- `ZerixClient`: Base client with core functionality
- `CompletionClient`: For completion-related operations
- `ChatClient`: For chat-related operations
- `WorkflowClient`: For workflow-related operations

Each client class provides specific methods for interacting with different aspects of the Zerix.AI API.

## License

MIT
