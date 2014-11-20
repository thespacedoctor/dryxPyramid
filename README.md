# dryxPyramid

`dryxPyramid` is a python package containing some basic, reusable code for Pyramid Webapps. It contains:

## Renderers

`dryxPyramid` contains some new and overriding renderers that allow for the download of files using `filename=myfilename` in the query string.

* csv (`format=csv`)
* json (`format=json`)
* plain text tables (`format=plain_table`)
* plain text (`format=plain_text`)

## API

| **Resource**  | **Post** | **Get** | **Put** | **Delete** | 
| :------------ | :----------- | :----------- | :----------- | :----------- |
| **/download**     | Not Allowed  | Download requested data  | Not Allowed  | Not Allowed  | 

### Reserved Query String Parameters

| Parameter Key | Description | Some Common Values |
| :------ | :------- | :------- |
| format | The format to display the data in | json, csv, plain_table, plain_text |
| filename | Download the data in the specified `format` with this filename | |

