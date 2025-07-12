"""Example CLI for the AI Food Advisor."""
import argparse

from .menu_processor import extract_menu_text, enrich_menu_text


def main():
    parser = argparse.ArgumentParser(description="AI Food Advisor")
    parser.add_argument('image', help='Path to menu image')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    args = parser.parse_args()

    print('Extracting menu text...')
    menu_text = extract_menu_text(args.image, region_name=args.region)
    print('Menu Text:')
    print(menu_text)

    print('\nEnriching menu with Amazon Bedrock...')
    enriched = enrich_menu_text(menu_text, region_name=args.region)
    print(enriched)


if __name__ == '__main__':
    main()
