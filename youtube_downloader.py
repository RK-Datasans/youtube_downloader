import os
import pandas as pd
from pytube import YouTube

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path)
        print(f"Downloaded: {url}")
        return "Done"
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")
        return f"Failed: {e}"

def process_excel_file(file_path):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Check if 'Status' column exists; if not, create it
    if 'Status' not in df.columns:
        df['Status'] = ""

    # Create output directory if it doesn't exist
    output_dir = "youtube-download"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through the URLs in the Excel file
    for index, row in df.iterrows():
        if pd.isna(row['Status']) or row['Status'] != "Done":
            url = row['URL']
            print(f"Processing: {url}")
            status = download_video(url, output_dir)
            df.at[index, 'Status'] = status
    
    # Save the updated Excel file
    df.to_excel(file_path, index=False)
    print("Excel file updated successfully.")

# Path to your Excel file
excel_file = "video_urls.xlsx"

# Call the processing function
process_excel_file(excel_file)
