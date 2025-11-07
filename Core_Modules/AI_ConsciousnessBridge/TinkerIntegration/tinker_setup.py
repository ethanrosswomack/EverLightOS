from tinker import TinkerClient

client = TinkerClient(api_key=YOUR_KEY)
model = client.load_model("llama-3.2-1B")
adapter =
client.create_lora_adapter(rank=16)