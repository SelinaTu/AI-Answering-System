import boto3
from .bedrock_utils import BedrockClient


def extract_menu_text(image_path: str, region_name: str = 'us-east-1') -> str:
    """Use Amazon Textract to extract text from menu images."""
    textract = boto3.client('textract', region_name=region_name)
    with open(image_path, 'rb') as document:
        image_bytes = document.read()

    response = textract.analyze_document(
        Document={'Bytes': image_bytes},
        FeatureTypes=['FORMS']
    )

    text = ''
    for block in response.get('Blocks', []):
        if block['BlockType'] == 'LINE':
            text += block['Text'] + '\n'
    return text


def enrich_menu_text(menu_text: str, region_name: str = 'us-east-1') -> str:
    """Use Amazon Bedrock to add calorie estimates and ingredient info."""
    prompt = (
        "You are a helpful food assistant. "
        "Analyze the following menu items and add estimated calories, "
        "ingredients, and flavor profiles.\n\n" + menu_text
    )
    client = BedrockClient(region_name)
    return client.generate_text(prompt)
