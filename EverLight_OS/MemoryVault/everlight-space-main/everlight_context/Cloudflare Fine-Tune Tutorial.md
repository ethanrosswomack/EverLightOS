---
conversation_id: "68399c79-3010-8011-a7cd-738de6b61b95"
title: "Cloudflare Fine-Tune Tutorial"
accounts: ["Account2_exports"]
models: []
tags: []
message_count: 7
---
# Cloudflare Fine-Tune Tutorial

##  — system


##  — user


## 2025-05-30T11:54:32.896379Z — user
https://developers.cloudflare.com/workers/tutorials/create-finetuned-chatgpt-ai-models-with-r2/

## 2025-05-30T11:54:34.982073Z — assistant


## 2025-05-30T11:54:35.074705Z — tool


## 2025-05-30T11:54:35.074944Z — assistant
The Cloudflare tutorial on creating fine-tuned OpenAI models with R2 provides a comprehensive guide to integrating Cloudflare Workers, R2 object storage, and the OpenAI API to build custom AI applications.

### Overview

This tutorial demonstrates how to:

1. Create a Cloudflare Worker application.
2. Upload a fine-tuning dataset to R2.
3. Bind the R2 bucket to your Worker.
4. Initialize your Worker application using the Hono framework.
5. Read files from R2 and upload them to OpenAI.
6. Create fine-tuned models via the OpenAI API.
7. List all fine-tune jobs.
8. Deploy your application.
9. View the fine-tune job status and use the model.

### Prerequisites

Before starting, ensure you have:

- A Cloudflare account with access to R2.
- An OpenAI API key.
- A fine-tune document structured as JSON Lines.

### Key Steps

**1. Create a Worker Application**

Use the `c3` CLI to scaffold a new Cloudflare Workers project:

```bash
npm create cloudflare@latest -- finetune-chatgpt-model
cd finetune-chatgpt-model
```


Choose the "Hello World Starter" template with TypeScript.

**2. Upload a Fine-Tune Document to R2**

Create an R2 bucket and upload your fine-tune dataset:

```bash
npx wrangler r2 bucket create <BUCKET_NAME>
npx wrangler r2 object put <PATH> -f <FILE_NAME>
```


Replace `<BUCKET_NAME>`, `<PATH>`, and `<FILE_NAME>` with your specific details.

**3. Bind Your Bucket to the Worker**

Update your `wrangler.toml` file to bind the R2 bucket:

```toml
[[r2_buckets]]
binding = 'MY_BUCKET'
bucket_name = '<YOUR_BUCKET_NAME>'
```


**4. Initialize Your Worker Application**

Install the Hono framework and OpenAI Node API library:

```bash
npm install hono openai
```


Replace the contents of `src/index.ts` with the provided code in the tutorial, ensuring you replace `<MY_BUCKET>` with your binding name.

**5. Read R2 Files and Upload Them to OpenAI**

Implement functionality in your Worker to read the fine-tune document from R2 and upload it to OpenAI using their API.

**6. Create Fine-Tuned Models**

Use the OpenAI API to create a new fine-tuned model based on your uploaded dataset.

**7. List All Fine-Tune Jobs**

Implement a route in your Worker to list all fine-tune jobs, allowing you to monitor their status.

**8. Deploy Your Application**

Deploy your Worker application using Wrangler:

```bash
npx wrangler deploy
```


**9. View the Fine-Tune Job Status and Use the Model**

After deployment, you can view the status of your fine-tune jobs and utilize the fine-tuned model in your applications.

For detailed instructions and code examples, refer to the full tutorial on the Cloudflare Developers website: linkturn0search0.

If you need assistance with any specific step or have questions about customizing this setup for your project, feel free to ask! 

## 2025-05-30T11:54:45.243378Z — assistant

