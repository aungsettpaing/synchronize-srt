## synchronize-srt
Python program for synchronizing movie SRT file

## Introduction
This program approximately re-synchronizes the SRT file if the subtitle is not synchronized
with the movie. This program will create a new file with adjusted time.

## How to run
This program can be run with the following command: <br>
    ```python Main.py directory operation milliseconds``` <br>
    <i><small>where, <br>
    <b>Main.py</b>     : refers to this program <br>
    <b>directory</b>   : directory of the srt file <br>
    <b>operation</b>   : {prev or next} prev is to delay and next is to speed up <br>
    <b>milliseconds</b>    : total duration you would like to delay or speed up <br></small></i>
<br>
<b>Example 1</b>, If you want to delay the srt file for 5 seconds (5000 in milliseconds), then <br>
    ```python Main.py D://your directory//file.srt prev 5000``` <br> <br>

<b>Example 2</b>, If you want to speed up the srt files for 3 seconds (3000 in milliseconds), then <br>
    ```python Main.py D://your directory//file.srt next 3000```
