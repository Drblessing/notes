#!/usr/bin/env python3
# Open daily brief of websites in browser
import webbrowser
import argparse
from enum import Enum


class DailyBrief:
    """Opens a daily brief of cool stuff in the browser."""

    # List of urls to open
    class ContentType(Enum):
        DAILY = 1
        NEWS = 2
        RESEARCH = 3
        BLOGS = 4

    URLS_DAILY = [
        "https://companiesmarketcap.com/assets-by-market-cap/",
        "https://www.coingecko.com/",
        "https://github.com/trending",
        "https://cryptofees.info/",
        "https://eigenphi.io/",
        "https://cryptocurrencyalerting.com/coin-listing-events.html",
        "https://transparency.flashbots.net/",
        "https://twitter.com/CoinbaseAssets",
        "https://ultrasound.money/",
        "https://clientdiversity.org/#distribution",
        "https://defillama.com/",
    ]

    URLS_NEWS = [
        "https://rekt.news",
        "https://weekinethereumnews.com/",
        "https://www.xda-developers.com/",
        "https://www.visualcapitalist.com",
        "https://physicsworld.com",
        "https://arstechnica.com/",
        "https://www.investopedia.com",
    ]

    URLS_RESEARCH = [
        "https://forum.soliditylang.org/",
        "https://ethresear.ch/",
        "https://collective.flashbots.net/latest",
    ]

    URLS_BLOGS = [
        "https://dbless.dev",
        "https://cmichel.io",
        "https://simonelnahas.com/",
        "https://www.saianeesh.com/",
        "https://hackernoon.com/exit-liquidity",
    ]

    CONTENT_DICT = {
        ContentType.DAILY: URLS_DAILY,
        ContentType.NEWS: URLS_NEWS,
        ContentType.RESEARCH: URLS_RESEARCH,
        ContentType.BLOGS: URLS_BLOGS,
    }

    def parse_args(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser(
            description="A python script that opens a daily brief of cool stuff in the browser."
        )
        parser.add_argument(
            "-n",
            "--news",
            action="store_true",
            help="Opens news sites.",
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="%(prog)s 1.0",
            help="Show program's version number and exit.",
        )

        parser.add_argument(
            "--research",
            "-r",
            action="store_true",
            help="Opens research sites.",
        )

        parser.add_argument(
            "--blogs",
            "-b",
            action="store_true",
            help="Opens blogs.",
        )

        args = parser.parse_args()

        return args

    def __init__(self):
        args = self.parse_args()
        if args.news:
            self.content = self.ContentType.NEWS
        elif args.research:
            self.content = self.ContentType.RESEARCH
        elif args.blogs:
            self.content = self.ContentType.BLOGS
        else:
            self.content = self.ContentType.DAILY

    def open_list(self, list):
        """Opens a list of urls in the browser."""
        for url in list:
            webbrowser.open_new_tab(url)

    def run(self):
        self.open_list(self.CONTENT_DICT[self.content])


if __name__ == "__main__":
    DailyBrief().run()
