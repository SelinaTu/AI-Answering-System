"""Example CLI for the AI Food Advisor."""
import argparse

from .menu_processor import extract_menu_text, enrich_menu_text
from .preferences import get_preferences


def main():
    parser = argparse.ArgumentParser(description="AI Food Advisor")
    parser.add_argument('image', help='Path to menu image')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    parser.add_argument('--voice', action='store_true', help='Capture preferences via microphone')
    args = parser.parse_args()

    print('Extracting menu text...')
    menu_text = extract_menu_text(args.image, region_name=args.region)
    print('Menu Text:')
    print(menu_text)

    print('\nEnriching menu with Amazon Bedrock...')
    enriched = enrich_menu_text(menu_text, region_name=args.region)
    print(enriched)

    print('\nCollecting your preferences...')
    prefs = get_preferences(use_voice=args.voice)
    print('Recorded preferences:')
    for k, v in prefs.items():
        print(f"{k}: {v}")


if __name__ == '__main__':
    main()
