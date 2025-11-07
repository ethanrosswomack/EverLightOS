---
conversation_id: "68ad2f7e-baf4-8332-837f-139894036f95"
title: "Cloudflare R2 Catalog Guide"
accounts: ["Account1_exports"]
models: []
tags: []
message_count: 19
---
# Cloudflare R2 Catalog Guide

##  — user


##  — system


##  — system


## 2025-08-26T03:52:36.344000Z — user
https://catalog.cloudflarestorage.com/74b94b7ffc15701b77e53f81bea03813/omniversal-s3

What is this and how do I use it

## 2025-08-26T03:52:38.545438Z — assistant


## 2025-08-26T03:52:39.011554Z — system


## 2025-08-26T03:52:39.041465Z — system


## 2025-08-26T03:52:39.052169Z — assistant


## 2025-08-26T03:52:39.155710Z — assistant


## 2025-08-26T03:52:42.086188Z — tool


## 2025-08-26T03:52:42.233159Z — assistant


## 2025-08-26T03:52:48.424059Z — tool


## 2025-08-26T03:52:49.349550Z — assistant
Short version: that URL is the **Cloudflare R2 Data Catalog** endpoint for your account and catalog named **`omniversal-s3`**. R2 Data Catalog turns an R2 bucket into an **Apache Iceberg** catalog so engines like **Spark/Databricks, PyIceberg, Snowflake (via external table/connector)** can discover tables and query data directly in-place—no copying to a separate warehouse. citeturn1search0turn1search2

Here’s how to use it (quick start):

1) **Enable the catalog (one-time)**
- In Cloudflare Dashboard: R2 → pick your bucket → **Settings → R2 Data Catalog → Enable**. Note the **Catalog URI** (it looks like your link) and **Warehouse name**. citeturn1search8

2) **Create an API token**
- Create a Cloudflare API token with R2 Data Catalog permissions; you’ll use it as a **Bearer** token to talk to the catalog. The “Getting started” guide walks through token creation. citeturn1search11

3) **Connect from your tool of choice**

- **Python (PyIceberg)**
  ```python
  from pyiceberg.catalog import load_catalog

  catalog = load_catalog(
      "omniversal",
      **{
        "uri": "https://catalog.cloudflarestorage.com/74b94b7ffc15701b77e53f81bea03813/omniversal-s3",
        "credential": "YOUR_API_TOKEN",  # Cloudflare API token
      }
  )

  # List namespaces and tables
  print(catalog.list_namespaces())
  print(catalog.list_tables(("default",)))

  # Create a table (example schema)
  from pyiceberg.schema import Schema
  from pyiceberg.types import NestedField, StringType, LongType

  schema = Schema(
      NestedField(1, "id", LongType(), required=True),
      NestedField(2, "name", StringType()),
  )
  catalog.create_table(("default", "people"), schema=schema)
  ```
  (Flow per Cloudflare’s “Getting started with Data Catalog”.) citeturn1search11

- **Apache Spark**
  ```sql
  -- In Spark (Scala/PySpark), configure an Iceberg REST catalog
  SET spark.sql.catalog.omniversal = org.apache.iceberg.spark.SparkCatalog;
  SET spark.sql.catalog.omniversal.type = rest;
  SET spark.sql.catalog.omniversal.uri = https://catalog.cloudflarestorage.com/74b94b7ffc15701b77e53f81bea03813/omniversal-s3;
  SET spark.sql.catalog.omniversal.oauth2.token = YOUR_API_TOKEN;

  -- Now use it
  SHOW NAMESPACES IN omniversal;
  CREATE NAMESPACE omniversal.default;
  CREATE TABLE omniversal.default.events (id BIGINT, ts TIMESTAMP, data STRING);
  INSERT INTO omniversal.default.events VALUES (1, current_timestamp(), 'hello');
  SELECT * FROM omniversal.default.events;
  ```
  (R2 Data Catalog exposes the **Iceberg REST** interface that Spark understands.) citeturn1search0

- **Databricks / Unity Catalog external location**
  Use Databricks’ instructions to connect to **Cloudflare R2** storage (S3-compatible) for data and point Iceberg **catalog** to the Cloudflare endpoint above. citeturn1search7

4) **Pricing note**
- The Data Catalog is (as of now) in **public beta** with no extra charge beyond normal R2 storage/ops; Cloudflare will give notice before charging. citeturn1search19

Why this matters for you
- You can keep datasets in your R2 bucket and **query them where they live** (Spark/Python), manage tables/versions/partitions with Iceberg, and avoid egress fees. citeturn1search2

If you want, tell me which bucket you enabled and what engine you want to use (Spark, PyIceberg, Snowflake). I’ll hand you the exact, copy-paste config for that stack.

## 2025-08-26T03:52:55.507844Z — assistant


## 2025-08-26T03:53:00.186822Z — assistant


## 2025-08-26T03:53:32.077000Z — user
can you make me an index.html file for https://s3.omniversalaether.app so that I can just go straight to the domain and browse all of the r2 files?

## 2025-08-26T03:53:33.194606Z — system


## 2025-08-26T03:53:33.240036Z — assistant
Got it — you want a simple **directory index** for your Cloudflare R2 bucket at `https://s3.omniversalaether.app`.  

⚠️ Important context:  
- R2 is S3-compatible storage, but **it doesn’t automatically serve directory listings**. If you just point a custom domain (like `s3.omniversalaether.app`) to your bucket, you’ll only be able to directly load files by their path (e.g., `…/myfile.json`), not browse the whole bucket.  
- To get a “file browser” feel, you need a static HTML app that calls the **R2 List Objects API** (or any S3-compatible “ListObjectsV2” request), then renders links. That HTML must run in the browser with valid credentials (signed URL / presigned request) or via a serverless worker proxy.  

Here’s a **bare-bones `index.html`** that uses client-side JavaScript + Cloudflare’s public R2 endpoint to show all objects if you expose them via a **public bucket policy** or a **Cloudflare Worker that lists objects**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Omniversal S3 Browser</title>
  <style>
    body { font-family: sans-serif; padding: 2em; }
    h1 { margin-bottom: 1em; }
    ul { list-style: none; padding-left: 0; }
    li { margin: 0.5em 0; }
    a { text-decoration: none; color: blue; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>Files in Omniversal S3</h1>
  <ul id="file-list"></ul>

  <script>
    async function loadFiles() {
      // ⚠️ Replace with your own Worker endpoint that calls R2 ListObjects
      const response = await fetch("/list");
      if (!response.ok) {
        document.getElementById("file-list").innerText = "Failed to load file list.";
        return;
      }
      const data = await response.json();
      const ul = document.getElementById("file-list");

      data.objects.forEach(obj => {
        const li = document.createElement("li");
        const link = document.createElement("a");
        link.href = obj.url;
        link.innerText = obj.key;
        li.appendChild(link);
        ul.appendChild(li);
      });
    }
    loadFiles();
  </script>
</body>
</html>
```

### How to make this work
1. **Set up a Cloudflare Worker (proxy)**  
   - The Worker should call the R2 S3 ListObjectsV2 API for your bucket (`bucket.list()` in Workers API) and return JSON like:
     ```json
     { "objects": [
       {"key": "file1.txt", "url": "https://s3.omniversalaether.app/file1.txt"},
       {"key": "folder/file2.jpg", "url": "https://s3.omniversalaether.app/folder/file2.jpg"}
     ]}
     ```
   - This avoids exposing credentials in the browser.

2. **Host `index.html`** at the root of your domain (`s3.omniversalaether.app`) so that visiting it runs the script, calls `/list`, and shows clickable links.

3. **Alternative (super simple, no JS)**  
   If you just want a static listing, you can’t get it directly from R2 unless you **generate the HTML yourself** (via a script or Worker that enumerates and renders the bucket). Cloudflare won’t give you a default Apache-style index page.

---

👉 Question for you: do you want me to  
- **(a)** give you the Worker script that lists your R2 files and pairs with this `index.html`,  
or  
- **(b)** generate a static HTML index of everything currently in your bucket (but you’d need to regenerate it when files change)?  

That determines whether you get a **live browser** vs. a **snapshot listing**. Which way do you want to go?

## 2025-08-26T03:53:33.468250Z — system

