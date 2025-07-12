import boto3

class BedrockClient:
    """Wrapper for interacting with Amazon Bedrock models."""

    def __init__(self, region_name: str):
        self.bedrock = boto3.client('bedrock-runtime', region_name=region_name)

    def generate_text(self, prompt: str, model_id: str = 'anthropic.claude-v2'):  # default model
        response = self.bedrock.invoke_model(
            modelId=model_id,
            body=bytes(prompt, 'utf-8')
        )
        # Bedrock returns a JSON with a 'completion' field
        return response['body'].read().decode('utf-8')
