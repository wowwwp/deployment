import requests
import os
import pandas as pd


def update_csv(transactions):
    '''Update the csv file with the generated text and duration'''
    df = pd.read_csv('./cv-valid-dev.csv')
    # Update the  csv file with the models prediction
    for key, value in transactions.items():
        response_dict = value[0]
        row = df['filename'] == key
        df.loc[row, 'duration'] = response_dict['duration']
        df.loc[row, 'generated_text'] = response_dict['transcription']
    df.to_csv('./cv-valid-dev.csv', index=False)


def post_req():
    '''Post request to the ASR API'''
    # Get all mp3 files in the directory
    url = 'http://localhost:8001/asr'
    all_files = os.listdir('../../cv-valid-dev')
    all_transcription = {}
    # Post request to the ASR API for the transcription and duration
    for file in all_files:
        output = requests.post(
            url, data={'file': os.path.join('../../cv-valid-dev', file)}, timeout=60)
        if output.status_code == 200:
            all_transcription[f"cv-valid-dev/{file}"] = output.json()
    return all_transcription


def main():
    transactions = post_req()
    update_csv(transactions)


if __name__ == '__main__':
    main()
