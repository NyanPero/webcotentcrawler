from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import click
import pandas as pd
import itertools
from io import StringIO
from pathlib import Path

def get_crawl_url_list(input_file):
    df = pd.read_json(StringIO(Path(input_file).read_text()), orient='records', lines=True)
    url_list = list(itertools.chain.from_iterable(list(df['extracted_url'])))
    return url_list

@click.command()
@click.option('--input-file')
@click.option('--output-dir')
@click.option('--user-agent')
@click.option('--simulate-os')
def check_twitter_suspend(input_file, output_dir, user_agent, simulate_os):

    url_list = get_crawl_url_list(input_file)
    file_name = input_file.split("/")[-1].replace('.jsonl','')
    settings = get_project_settings()

    # file out path
    settings.set('FEED_URI', output_dir+'{}_webcontent_{}.jsonl'.format(file_name, simulate_os))
    
    process = CrawlerProcess(settings)

    process.crawl('Crawler', url_list=url_list, user_agent=user_agent)
    process.start()

    
if __name__ == '__main__':
    check_twitter_suspend()